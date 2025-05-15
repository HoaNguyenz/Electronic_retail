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
        if user_type == 'Admin':
            cursor.execute("INSERT INTO Admin (UserID, Role) VALUES (%s, %s);", (user_id, 'Default Role'))
        elif user_type == 'Customer':
            cursor.execute("INSERT INTO Customer (UserID) VALUES (%s);", (user_id,))

        conn.commit()
        return {"message": "User registered successfully"}
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
        cursor.execute("SELECT Password, UserType FROM Users WHERE Email = %s;", (email,))
        user = cursor.fetchone()

        if user and verify_password(password, user[0]):
            return {"message": "Login successful", "user_type": user[1]}
        return {"message": "Invalid credentials"}
    except pymssql.Error as e:
        return {"error": f"Database error: {str(e)}"}
    finally:
        conn.close()