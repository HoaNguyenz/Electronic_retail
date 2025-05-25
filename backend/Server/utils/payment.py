from database import get_db_connection
from datetime import datetime

def makePayment(customer_id, order_id, payment_method):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        # 1. Check if the order exists and belongs to the customer, and is in 'In cart' status
        cursor.execute("""
            SELECT TotalAmount, Status FROM Orders
            WHERE OrderID = %s AND CustomerID = %s
        """, (order_id, customer_id))
        order = cursor.fetchone()
        if not order:
            return {"error": "Order not found", "status": 404}
        total_amount, status = order
        if status != "In Cart":
            return {"error": "Order is not in cart or already paid", "status": 400}

        # 2. Update order status to 'Completed' and set OrderDate to now
        cursor.execute("""
            UPDATE Orders
            SET Status = %s, OrderDate = %s
            WHERE OrderID = %s
        """, ("Completed", datetime.now(), order_id))

        # 3. Insert payment record
        cursor.execute("""
            INSERT INTO Payment (OrderID, PaymentDate, PaymentMethod, Amount, PaymentStatus)
            VALUES (%s, %s, %s, %s, %s)
        """, (order_id, datetime.now(), payment_method, total_amount, "Paid"))

        conn.commit()
        return {"message": "Payment successful", "status": 200}
    except Exception as e:
        return {"error": "Database error", "details": str(e), "status": 500}
    finally:
        conn.close()