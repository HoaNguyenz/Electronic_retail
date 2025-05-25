from database import get_db_connection
from datetime import date

def fetch_products(category_id=None, min_price=None, max_price=None, brand=None, rating=None, category_name=None):
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
        if category_name:
            query += " AND p.CategoryID = (SELECT CategoryID FROM Category WHERE CategoryName = %s)"
            params.append(category_name)
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

def fetch_categories():
    conn = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor(as_dict=True)
        cursor.execute("SELECT CategoryName FROM Category")
        categories = cursor.fetchall()
        return [category["CategoryName"] for category in categories]
    except Exception as e:
        return {'success': False, 'error': str(e)}
    
def get_product_imgs():
    conn = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor(as_dict=True)
        cursor.execute("SELECT TOP 5 Marketting_Img FROM Product WHERE Marketting_Img IS NOT NULL")        
        links = cursor.fetchall()
        # Return the list of image URLs
        return [link["Marketting_Img"] for link in links]
    except Exception as e:
        return {'success': False, 'error': str(e)}
    finally:
        if conn:
            conn.close()

def get_product_detail(product_id):
    """
    Fetch all relevant data of a product for adding to cart.
    Returns product info, inventory, average rating, and supplier name.
    """
    conn = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor(as_dict=True)

        # Fetch product details, category, supplier, and average rating
        cursor.execute("""
            SELECT 
                p.ProductID,
                p.Name,
                p.Description,
                p.Price,
                p.CategoryID,
                c.CategoryName,
                p.SupplierID,
                s.Name AS SupplierName,
                p.WarrantyPeriod,
                p.Marketting_Img,
                ISNULL(i.QuantityInStock, 0) AS QuantityInStock,
                ISNULL(i.ReorderLevel, 0) AS ReorderLevel,
                ISNULL(r.AvgRating, 0) AS AvgRating
            FROM Product p
            LEFT JOIN Category c ON p.CategoryID = c.CategoryID
            LEFT JOIN Supplier s ON p.SupplierID = s.SupplierID
            LEFT JOIN Inventory i ON p.ProductID = i.ProductID
            LEFT JOIN (
                SELECT ProductID, AVG(Rating) AS AvgRating
                FROM Review
                WHERE ProductID = %s
                GROUP BY ProductID
            ) r ON p.ProductID = r.ProductID
            WHERE p.ProductID = %s
        """, (product_id, product_id))
        
        product = cursor.fetchone()
        if not product:
            return {"success": False, "error": "Product not found."}

        # Optionally, fetch recent reviews (limit 3)
        cursor.execute("""
            SELECT TOP 3 r.Rating, r.Comment, r.ReviewDate, cu.CustomerID
            FROM Review r
            JOIN Customer cu ON r.CustomerID = cu.CustomerID
            WHERE r.ProductID = %s
            ORDER BY r.ReviewDate DESC
        """, (product_id,))
        reviews = cursor.fetchall()
        product["reviews"] = reviews
        return {"success": True, "product": product}
    except Exception as e:
        return {"success": False, "error": str(e)}
    finally:
        if conn:
            conn.close()