from database import get_db_connection

def create_category(category_name, parent_category_id=None):
    conn = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        query = "INSERT INTO Category (CategoryName, ParentCategoryID) VALUES (%s, %s)"
        cursor.execute(query, (category_name, parent_category_id))
        conn.commit()
        return {"success": True, "message": "Category created successfully."}
    except Exception as e:
        return {"success": False, "error": str(e)}
    finally:
        if conn:
            conn.close()

def create_supplier(name, contact_name, phone, email, address):
    conn = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        query = """
            INSERT INTO Supplier (Name, ContactName, Phone, Email, Address)
            VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(query, (name, contact_name, phone, email, address))
        conn.commit()
        return {"success": True, "message": "Supplier created successfully."}
    except Exception as e:
        return {"success": False, "error": str(e)}
    finally:
        if conn:
            conn.close()

def create_product(name, description, price, category_id, supplier_id, warranty_period):
    conn = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        query = """
            INSERT INTO Product (Name, Description, Price, CategoryID, SupplierID, WarrantyPeriod)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (name, description, price, category_id, supplier_id, warranty_period))
        conn.commit()
        return {"success": True, "message": "Product created successfully."}
    except Exception as e:
        return {"success": False, "error": str(e)}
    finally:
        if conn:
            conn.close()

def update_product(product_id, name=None, description=None, price=None, category_id=None, supplier_id=None, warranty_period=None):
    conn = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        fields = []
        params = []
        if name is not None:
            fields.append("Name = %s")
            params.append(name)
        if description is not None:
            fields.append("Description = %s")
            params.append(description)
        if price is not None:
            fields.append("Price = %s")
            params.append(price)
        if category_id is not None:
            fields.append("CategoryID = %s")
            params.append(category_id)
        if supplier_id is not None:
            fields.append("SupplierID = %s")
            params.append(supplier_id)
        if warranty_period is not None:
            fields.append("WarrantyPeriod = %s")
            params.append(warranty_period)
        if not fields:
            return {"success": False, "error": "No fields to update."}
        query = f"UPDATE Product SET {', '.join(fields)} WHERE ProductID = %s"
        params.append(product_id)
        cursor.execute(query, params)
        conn.commit()
        return {"success": True, "message": "Product updated successfully."}
    except Exception as e:
        return {"success": False, "error": str(e)}
    finally:
        if conn:
            conn.close()

def remove_product(product_id):
    conn = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        query = "DELETE FROM Product WHERE ProductID = %s"
        cursor.execute(query, (product_id,))
        conn.commit()
        return {"success": True, "message": "Product removed successfully."}
    except Exception as e:
        return {"success": False, "error": str(e)}
    finally:
        if conn:
            conn.close()