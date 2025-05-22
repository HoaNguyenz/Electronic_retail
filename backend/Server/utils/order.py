import datetime
from database import get_db_connection

def get_or_create_cart(customer_id, order_id=None):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        # Validate that the CustomerID exists in the Customer table
        cursor.execute("SELECT CustomerID FROM Customer WHERE CustomerID = %s", (customer_id,))
        customer = cursor.fetchone()
        if not customer:
            raise Exception(f"CustomerID {customer_id} does not exist in the Customer table.")

        # If order_id is provided, check if it exists and belongs to the customer
        if order_id:
            cursor.execute("""
                SELECT OrderID FROM Orders 
                WHERE OrderID = %s AND CustomerID = %s AND Status = 'In Cart'
            """, (order_id, customer_id))
            existing_order = cursor.fetchone()
            if existing_order:
                return existing_order[0]  # Return the existing OrderID

        # If no valid order_id is provided, check if an "In Cart" order already exists for the customer
        cursor.execute("""
            SELECT OrderID FROM Orders 
            WHERE CustomerID = %s AND Status = 'In Cart'
        """, (customer_id,))
        order = cursor.fetchone()

        if order:
            return order[0]  # Return the existing OrderID

        # Create a new "In Cart" order if none exists
        order_date = datetime.date.today()
        cursor.execute("""
            INSERT INTO Orders (CustomerID, OrderDate, Status, TotalAmount) 
            OUTPUT INSERTED.OrderID
            VALUES (%s, %s, %s, %s);
        """, (customer_id, order_date, 'In Cart', 0))
        new_order_id = cursor.fetchone()[0]
        conn.commit()
        return new_order_id

    except Exception as e:
        raise Exception(f"Error retrieving or creating cart: {str(e)}")
    finally:
        conn.close()

def process_order(customer_id, order_id, payment_method):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        # Check if the order exists and belongs to the customer
        cursor.execute("""
            SELECT Status FROM Orders 
            WHERE OrderID = %s AND CustomerID = %s
        """, (order_id, customer_id))
        order = cursor.fetchone()

        if not order:
            return {"error": "Order not found or does not belong to the customer", "status": 404}

        # Check if the order status is "In Cart"
        if order[0] != "In Cart":
            return {"error": "Order is not in 'In Cart' status", "status": 400}

        # Check if there are any order items associated with the order
        cursor.execute("""
            SELECT ProductID, Quantity, UnitPrice 
            FROM OrderItem 
            WHERE OrderID = %s
        """, (order_id,))
        cart_items = cursor.fetchall()

        if not cart_items:
            return {"error": "No items in the cart to process", "status": 400}

        # Calculate total amount
        total_amount = sum(item["Quantity"] * item["UnitPrice"] for item in cart_items)

        # Update the order status and total amount
        cursor.execute("""
            UPDATE Orders 
            SET Status = 'Processing', TotalAmount = %s 
            WHERE OrderID = %s
        """, (total_amount, order_id))

        # Deduct quantities from inventory
        for item in cart_items:
            cursor.execute("""
                UPDATE Inventory 
                SET QuantityInStock = QuantityInStock - %s 
                WHERE ProductID = %s
            """, (item["Quantity"], item["ProductID"]))

        # Create payment entry
        payment_date = datetime.date.today()
        cursor.execute("""
            INSERT INTO Payment (OrderID, PaymentDate, PaymentMethod, Amount, PaymentStatus) 
            VALUES (%s, %s, %s, %s, %s)
        """, (order_id, payment_date, payment_method, total_amount, 'Pending'))

        conn.commit()
        return {"message": "Order processed successfully", "order_id": order_id, "status": 200}

    except Exception as e:
        return {"error": "Database error", "details": str(e), "status": 500}

    finally:
        conn.close()

def cancel_order(order_id):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        # Check if the order exists
        cursor.execute("SELECT OrderID FROM Orders WHERE OrderID = %s", (order_id,))
        order = cursor.fetchone()

        if not order:
            return {"error": "Order not found", "status": 404}

        # Check if the order is already processed
        cursor.execute("SELECT Status FROM Orders WHERE OrderID = %s", (order_id,))
        status = cursor.fetchone()[0]

        if status != "In Cart":
            return {"error": "Order cannot be canceled as it is not in 'In Cart' status", "status": 400}

        # Delete the order
        cursor.execute("DELETE FROM Orders WHERE OrderID = %s", (order_id,))
        conn.commit()

        return {"message": "Order canceled successfully", "status": 200}

    except Exception as e:
        return {"error": "Database error", "details": str(e), "status": 500}
    finally:
        conn.close()

def get_order_data(order_id, customer_id):
    try:
        conn = get_db_connection()
        cursor = conn.cursor(as_dict=True)

        # Fetch order and items, including product name
        cursor.execute("""
            SELECT o.OrderID, o.CustomerID, o.Status, o.TotalAmount, 
                   oi.ProductID, p.Name AS ProductName, oi.Quantity, oi.UnitPrice
            FROM Orders o
            JOIN OrderItem oi ON o.OrderID = oi.OrderID
            JOIN Product p ON oi.ProductID = p.ProductID
            WHERE o.OrderID = %s AND o.CustomerID = %s
        """, (order_id, customer_id))
        order_details = cursor.fetchall()

        if not order_details:
            return {"error": "Order not found or does not belong to the customer", "status": 404}

        # Format the response as described
        response = {
            "order_id": order_details[0]["OrderID"],
            "customer_id": order_details[0]["CustomerID"],
            "status": order_details[0]["Status"],
            "total_amount": float(order_details[0]["TotalAmount"]),
            "items": [
                {
                    "product_id": item["ProductID"],
                    "name": item["ProductName"],
                    "quantity": item["Quantity"],
                    "unit_price": float(item["UnitPrice"])
                } for item in order_details
            ]
        }
        return response

    except Exception as e:
        return {"error": "Database error", "details": str(e), "status": 500}
    finally:
        conn.close()

def get_order_history(customer_id):
    try:
        conn = get_db_connection()
        cursor = conn.cursor(as_dict=True)

        cursor.execute("""
            SELECT OrderID, TotalAmount, Status
            FROM Orders
            WHERE CustomerID = %s
            ORDER BY OrderID DESC
        """, (customer_id,))
        orders = cursor.fetchall()

        # Format as a list of dicts
        history = [
            {
                "order_id": order["OrderID"],
                "total": float(order["TotalAmount"])
            }
            for order in orders
        ]
        return history

    except Exception as e:
        return {"error": "Database error", "details": str(e), "status": 500}
    finally:
        conn.close()