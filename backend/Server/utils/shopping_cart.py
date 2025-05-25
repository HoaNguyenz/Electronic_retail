from database import get_db_connection
from utils.order import get_or_create_cart


# Helper function
def recalculate_order_total(cursor, order_id):
    cursor.execute("""
        UPDATE Orders
        SET TotalAmount = (
            SELECT COALESCE(SUM(Quantity * UnitPrice), 0)
            FROM OrderItem
            WHERE OrderID = %s
        )
        WHERE OrderID = %s
    """, (order_id, order_id))


def add_product_to_cart(customer_id, order_id, product_id, quantity):
    try:
        conn = get_db_connection()
        cursor = conn.cursor(as_dict=True)

        confirm_order_id = get_or_create_cart(customer_id, order_id)
        print(confirm_order_id, order_id)

        cursor.execute("SELECT QuantityInStock FROM Inventory WHERE ProductID = %s", (product_id,))
        product = cursor.fetchone()
        if not product:
            return {"error": "Product not found", "status": 404}
        if product["QuantityInStock"] < quantity:
            return {"error": "Insufficient stock", "status": 400}

        cursor.execute("""
            INSERT INTO OrderItem (OrderID, ProductID, Quantity, UnitPrice)
            VALUES (%s, %s, %s, (SELECT Price FROM Product WHERE ProductID = %s))
        """, (confirm_order_id, product_id, quantity, product_id))

        cursor.execute("""
            UPDATE Inventory
            SET QuantityInStock = QuantityInStock - %s
            WHERE ProductID = %s
        """, (quantity, product_id))

        recalculate_order_total(cursor, confirm_order_id)

        conn.commit()
        return {"message": "Product added to cart successfully", "status": 200}
    except Exception as e:
        return {"error": "Database error", "details": str(e), "status": 500}
    finally:
        conn.close()


def update_cart_item(order_item_id, new_quantity):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT ProductID, Quantity, OrderID FROM OrderItem WHERE OrderItemID = %s",
            (order_item_id,)
        )
        result = cursor.fetchone()
        if not result:
            return {"error": "Order item not found", "status": 404}

        product_id, current_quantity, order_id = result

        cursor.execute(
            "SELECT QuantityInStock FROM Inventory WHERE ProductID = %s",
            (product_id,)
        )
        inventory_result = cursor.fetchone()
        if not inventory_result:
            return {"error": "Inventory record not found", "status": 404}

        quantity_in_stock = inventory_result[0]
        difference = new_quantity - current_quantity

        if difference > 0 and quantity_in_stock < difference:
            return {"error": "Insufficient stock", "status": 400}

        cursor.execute(
            "UPDATE Inventory SET QuantityInStock = QuantityInStock - %s WHERE ProductID = %s",
            (difference, product_id)
        )

        cursor.execute(
            "UPDATE OrderItem SET Quantity = %s WHERE OrderItemID = %s",
            (new_quantity, order_item_id)
        )

        recalculate_order_total(cursor, order_id)

        conn.commit()
        return {"message": "Cart updated successfully", "status": 200}

    except Exception as e:
        return {"error": "Database error", "details": str(e), "status": 500}
    finally:
        conn.close()



def remove_product_from_cart(order_item_id):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT ProductID, Quantity, OrderID FROM OrderItem WHERE OrderItemID = %s", (order_item_id,))
        order_item = cursor.fetchone()

        if not order_item:
            return {"error": "Order item not found", "status": 404}

        product_id, quantity, order_id = order_item

        cursor.execute("DELETE FROM OrderItem WHERE OrderItemID = %s", (order_item_id,))
        
        cursor.execute("UPDATE Inventory SET QuantityInStock = QuantityInStock + %s WHERE ProductID = %s", (quantity, product_id))

        # Check if there are remaining items in the order
        cursor.execute("SELECT COUNT(*) FROM OrderItem WHERE OrderID = %s", (order_id,))
        remaining_items = cursor.fetchone()[0]

        if remaining_items == 0:
            cursor.execute("DELETE FROM Orders WHERE OrderID = %s", (order_id,))
        else:
            recalculate_order_total(cursor, order_id)

        conn.commit()
        return {"message": "Product removed from cart and inventory updated successfully", "status": 200}
    
    except Exception as e:
        return {"error": "Database error", "details": str(e), "status": 500}
    
    finally:
        conn.close()


def get_cart_count(customer_id):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        # Find the "In cart" order for the customer
        cursor.execute("""
            SELECT OrderID FROM Orders
            WHERE CustomerID = %s AND Status = 'In cart'
        """, (customer_id,))
        order = cursor.fetchone()
        if not order:
            return {"count": 0, "status": 200}

        order_id = order[0]

        # Sum the quantity of all items in the cart
        cursor.execute("""
            SELECT COALESCE(SUM(Quantity), 0) FROM OrderItem
            WHERE OrderID = %s
        """, (order_id,))
        count = cursor.fetchone()[0]

        return {"count": count, "status": 200}
    except Exception as e:
        return {"error": "Database error", "details": str(e), "status": 500}
    finally:
        conn.close()

def get_cart_detail(customer_id):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        # Get all "In cart" orders for the customer
        cursor.execute("""
            SELECT OrderID FROM Orders
            WHERE CustomerID = %s AND Status = 'In cart'
        """, (customer_id,))
        orders = cursor.fetchall()
        if not orders:
            return {"orders": [], "status": 200}

        result_orders = []
        for order in orders:
            order_id = order[0]
            # Get all items in the cart with product details for this order
            cursor.execute("""
                SELECT 
                    oi.OrderItemID,
                    oi.ProductID,
                    p.Name,
                    p.Description,
                    p.Price,
                    oi.Quantity,
                    oi.UnitPrice,
                    p.Marketting_Img,
                    i.QuantityInStock
                FROM OrderItem oi
                JOIN Product p ON oi.ProductID = p.ProductID
                JOIN Inventory i ON p.ProductID = i.ProductID
                WHERE oi.OrderID = %s
            """, (order_id,))
            items = cursor.fetchall()

            cart = []
            for item in items:
                cart.append({
                    "order_item_id": item[0],
                    "product_id": item[1],
                    "name": item[2],
                    "description": item[3],
                    "price": float(item[4]),
                    "quantity": item[5],
                    "unit_price": float(item[6]),
                    "image": item[7],
                    "quantity_in_stock": item[8]
                })
            result_orders.append({
                "order_id": order_id,
                "cart": cart
            })
    
        return {"orders": result_orders, "status": 200}
    except Exception as e:
        return {"error": "Database error", "details": str(e), "status": 500}
    finally:
        conn.close()