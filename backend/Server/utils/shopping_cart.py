from database import get_db_connection
from utils.order import get_or_create_cart


def add_product_to_cart(customer_id, order_id, product_id, quantity):
    try:
        conn = get_db_connection()
        cursor = conn.cursor(as_dict=True)

        # Get or create the "In Cart" order for the customer
        confirm_order_id = get_or_create_cart(customer_id, order_id)
        print(confirm_order_id, order_id)

        # Check if the product exists and has enough stock
        cursor.execute("SELECT QuantityInStock FROM Inventory WHERE ProductID = %s", (product_id,))
        product = cursor.fetchone()
        if not product:
            return {"error": "Product not found", "status": 404}
        if product["QuantityInStock"] < quantity:
            return {"error": "Insufficient stock", "status": 400}

        # Add the product to the cart
        cursor.execute("""
            INSERT INTO OrderItem (OrderID, ProductID, Quantity, UnitPrice)
            VALUES (%s, %s, %s, (SELECT Price FROM Product WHERE ProductID = %s))
        """, (confirm_order_id, product_id, quantity, product_id))
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

        # Step 1: Fetch the current quantity and product ID for the order item
        cursor.execute(
            "SELECT ProductID, Quantity FROM OrderItem WHERE OrderItemID = %s",
            (order_item_id,)
        )
        result = cursor.fetchone()
        if not result:
            return {"error": "Order item not found", "status": 404}

        product_id, current_quantity = result

        # Step 2: Fetch current stock
        cursor.execute(
            "SELECT QuantityInStock FROM Inventory WHERE ProductID = %s",
            (product_id,)
        )
        inventory_result = cursor.fetchone()
        if not inventory_result:
            return {"error": "Inventory record not found", "status": 404}

        quantity_in_stock = inventory_result[0]

        # Step 3: Calculate the quantity difference
        difference = new_quantity - current_quantity

        # Step 4: Check if the inventory allows the update
        if difference > 0 and quantity_in_stock < difference:
            return {"error": "Insufficient stock", "status": 400}

        # Step 5: Update Inventory
        cursor.execute(
            "UPDATE Inventory SET QuantityInStock = QuantityInStock - %s WHERE ProductID = %s",
            (difference, product_id)
        )

        # Step 6: Update OrderItem
        cursor.execute(
            "UPDATE OrderItem SET Quantity = %s WHERE OrderItemID = %s",
            (new_quantity, order_item_id)
        )

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

        # Retrieve the product ID, quantity, and order ID before deleting
        cursor.execute("SELECT ProductID, Quantity, OrderID FROM OrderItem WHERE OrderItemID = %s", (order_item_id,))
        order_item = cursor.fetchone()

        if not order_item:
            return {"error": "Order item not found", "status": 404}

        product_id, quantity, order_id = order_item

        # Remove the product from the cart
        cursor.execute("DELETE FROM OrderItem WHERE OrderItemID = %s", (order_item_id,))
        
        # Update inventory
        cursor.execute("UPDATE Inventory SET QuantityInStock = QuantityInStock + %s WHERE ProductID = %s", (quantity, product_id))

        # Check if the order has any remaining items
        cursor.execute("SELECT COUNT(*) FROM OrderItem WHERE OrderID = %s", (order_id,))
        remaining_items = cursor.fetchone()[0]

        # If no items remain, delete the order
        if remaining_items == 0:
            cursor.execute("DELETE FROM Orders WHERE OrderID = %s", (order_id,))

        conn.commit()
        return {"message": "Product removed from cart and inventory updated successfully", "status": 200}
    
    except Exception as e:
        return {"error": "Database error", "details": str(e), "status": 500}
    
    finally:
        conn.close()