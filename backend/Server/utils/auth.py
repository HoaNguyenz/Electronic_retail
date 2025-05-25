import pymssql
from database import get_db_connection
import bcrypt

def hash_password(password):
    """Hash the password securely using bcrypt."""
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode(), salt).decode()

def verify_password(password, hashed_password):
    """Verify the password against the stored hash."""
    return bcrypt.checkpw(password.encode(), hashed_password.encode())

def register_user(first_name, last_name, email, phone, address, city, state, zip_code, password, user_type):
    """Register a new user in the MSSQL database."""
    conn = get_db_connection()
    cursor = conn.cursor()

    hashed_pw = hash_password(password)
    try:
        # Insert into Users table
        cursor.execute("""
            INSERT INTO Users (FirstName, LastName, Email, Phone, Address, City, State, ZipCode, RegistrationDate, Password, UserType)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, GETDATE(), %s, %s);
        """, (first_name, last_name, email, phone, address, city, state, zip_code, hashed_pw, user_type))
        
        # Get the newly created UserID
        cursor.execute("SELECT SCOPE_IDENTITY();")
        user_id = cursor.fetchone()[0]

        # Insert into Admin or Customer table based on UserType
        customer_id = None
        admin_id = None
        if user_type == 'Admin':
            cursor.execute("INSERT INTO Admin (UserID, Role) VALUES (%s, %s);", (user_id, 'Default Role'))
            cursor.execute("SELECT AdminID FROM Admin WHERE UserID = %s;", (user_id,))
            admin_id = cursor.fetchone()[0]
        elif user_type == 'Customer':
            cursor.execute("INSERT INTO Customer (UserID) VALUES (%s);", (user_id,))
            cursor.execute("SELECT CustomerID FROM Customer WHERE UserID = %s;", (user_id,))
            customer_id = cursor.fetchone()[0]

        conn.commit()
        response = {
            "message": "User registered successfully",
            "email": email,
            "name": f"{first_name} {last_name}"
        }
        if customer_id:
            response["customer_id"] = customer_id
        if admin_id:
            response["admin_id"] = admin_id
        return response
    except pymssql.Error as e:
        conn.rollback()
        return {"error": f"Database error: {str(e)}"}
    finally:
        conn.close()

def authenticate_user(email, password):
    """Authenticate a user by verifying their password."""
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        # Fetch user details from Users table
        cursor.execute("SELECT UserID, Password, UserType, FirstName, LastName FROM Users WHERE Email = %s;", (email,))
        user = cursor.fetchone()

        if user and verify_password(password, user[1]):
            user_id = user[0]
            user_type = user[2]
            response = {
                "message": "Login successful",
                "user_type": user_type,
                "email": email,
                "name": f"{user[3]} {user[4]}"
            }
            if user_type == 'Customer':
                cursor.execute("SELECT CustomerID FROM Customer WHERE UserID = %s;", (user_id,))
                customer = cursor.fetchone()
                if customer:
                    response["customer_id"] = customer[0]
            elif user_type == 'Admin':
                cursor.execute("SELECT AdminID FROM Admin WHERE UserID = %s;", (user_id,))
                admin = cursor.fetchone()
                if admin:
                    response["admin_id"] = admin[0]
            return response
        return {"message": "Invalid credentials"}
    except pymssql.Error as e:
        return {"error": f"Database error: {str(e)}"}
    finally:
        conn.close()