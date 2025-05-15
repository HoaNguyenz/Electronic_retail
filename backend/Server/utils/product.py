from database import get_db_connection

def fetch_products(category_id=None, min_price=None, max_price=None, brand=None, rating=None):
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
        if category_id:
            query += " AND p.CategoryID = %s"
            params.append(category_id)
        if min_price:
            query += " AND p.Price >= %s"
            params.append(min_price)
        if max_price:
            query += " AND p.Price <= %s"
            params.append(max_price)
        if brand:
            query += " AND p.SupplierID = (SELECT SupplierID FROM Supplier WHERE Name = %s)"
            params.append(brand)
        if rating:
            query += " AND r.AvgRating >= %s"
            params.append(rating)

        conn = get_db_connection()
        cursor = conn.cursor(as_dict=True)
        cursor.execute(query, params)
        products = cursor.fetchall()
        conn.close()

        return {"success": True, "products": products}

    except Exception as e:
        return {"success": False, "error": str(e)}
