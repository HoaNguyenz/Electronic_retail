from database import get_db_connection
from datetime import date

def fetch_products(category_id=None, min_price=None, max_price=None, brand=None, rating=None):
    conn = None
    try:
        query = """
            SELECT p.*, r.AvgRating 
            FROM Product p 
            LEFT JOIN (
                SELECT ProductID, AVG(Rating) AS AvgRating 
                FROM Review 
                GROUP BY ProductID
            ) r ON p.ProductID = r.ProductID 
            WHERE 1=1
        """
        params = []
        if category_id is not None:
            query += " AND p.CategoryID = %s"
            params.append(category_id)
        if min_price is not None:
            query += " AND p.Price >= %s"
            params.append(min_price)
        if max_price is not None:
            query += " AND p.Price <= %s"
            params.append(max_price)
        if brand:
            query += " AND p.SupplierID = (SELECT SupplierID FROM Supplier WHERE Name = %s)"
            params.append(brand)
        if rating is not None:
            query += " AND r.AvgRating >= %s"
            params.append(rating)

        conn = get_db_connection()
        cursor = conn.cursor(as_dict=True)
        cursor.execute(query, params)
        products = cursor.fetchall()
        return {"success": True, "products": products}
    except Exception as e:
        return {"success": False, "error": str(e)}
    finally:
        if conn:
            conn.close()

def rate_product(product_id, customer_id, rating, comment=None):
    conn = None
    try:
        if not (1 <= int(rating) <= 5):
            return {"success": False, "error": "Rating must be between 1 and 5."}
        conn = get_db_connection()
        cursor = conn.cursor()
        query = """
            INSERT INTO Review (CustomerID, ProductID, Rating, Comment, ReviewDate)
            VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(query, (customer_id, product_id, rating, comment, date.today()))
        conn.commit()
        return {"success": True, "message": "Review submitted successfully."}
    except Exception as e:
        return {"success": False, "error": str(e)}
    finally:
        if conn:
            conn.close()