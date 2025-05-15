* Root Endpoint: http://127.0.0.1:5000

0. User Registration and Authentication:

    ### User Registration
    - **Path**: `/register`
    - **Method**: `POST`
    - **Description**: Allows users (Admin or Customer) to register a new account.
    - **Request Body**:
      ```json
      {
          "first_name": "string",
          "last_name": "string",
          "email": "string",
          "phone": "string",
          "address": "string",
          "city": "string",
          "state": "string",
          "zip_code": "string",
          "password": "string",
          "user_type": "string" // "Admin" or "Customer"
      }
      ```
    - **Response**:
      - **Success**: 
        ```json
        {
            "message": "User registered successfully"
        }
        ```
      - **Error**:
        ```json
        {
            "error": "Database error",
            "details": "string"
        }
        ```

    ### User Login
    - **Path**: `/login`
    - **Method**: `POST`
    - **Description**: Allows users to log in to their account.
    - **Request Body**:
      ```json
      {
          "email": "string",
          "password": "string"
      }
      ```
    - **Response**:
      - **Success**:
        ```json
        {
            "message": "Login successful",
            "user_type": "string" // "Admin" or "Customer"
        }
        ```
      - **Failure**:
        ```json
        {
            "message": "Invalid credentials"
        }
        ```
      - **Error**:
        ```json
        {
            "error": "Database error",
            "details": "string"
        }
        ```
          
1. Product management (admin side): 
    - Description: Admins can add, update, and remove products from the catalog.
    - Insert product:
        + Path:
        + Method: 
    - Delete product:
    - Update product:

2. Product browsing and search:
    - **Path**: `/products`
    - **Method**: `GET`
    - **Description**: Allows customers to browse and search for products using various filters such as category, price range, brand, and rating.
    - **Query Parameters**:
        + category_id (optional): Filters products by category ID.
        + min_price (optional): Filters products with a price greater than or equal to the + specified value.
        + max_price (optional): Filters products with a price less than or equal to the specified value.
        + brand (optional): Filters products by brand name.
        + rating (optional): Filters products with an average rating greater than or equal to the specified value.
    - **Response**:
      - **Success**:
        ```json
        {
            "products": [
                {
                    "ProductID": "int",
                    "Name": "string",
                    "Description": "string",
                    "Price": "float",
                    "CategoryID": "int",
                    "SupplierID": "int",
                    "AvgRating": "float" // Average rating of the product
                },
                ...
            ]
        }
        ```
      - **Error**:
        ```json
        {
            "error": "Database error",
            "details": "string"
        }
        ```
    -  **Example**:
        + Get all products: 
                GET /products
        + Filter by category: 
                GET /products?category_id=1
        + Filter by price range:
                GET /products?min_price=100&max_price=500
        + Filter by brand:
                GET /products?brand=Samsung
        + Filter by rating
                GET /products?rating=4
        + Composite filter: 
                GET /products?min_price=100&max_price=500&brand=Samsung&rating=4

3. Shopping Cart Functionality
     - Description: Users can add, update quantities, and remove products from their cart.

4. Order Processing & Checkout
    - Join Query: Fetches data linking customers, cart items, and payment methods.
    - Description: Users can place orders and track status.

5. Payment Gateway Integration
    - Description: Customers can pay via multiple payment methods (credit card, PayPal, etc.).

6. Order History & Tracking
    - Subquery: Retrieve past orders for a customer.
    - Description: Displays detailed purchase history and order status updates.

7. Reviews & Ratings
    Aggregate Functions: Calculate average product rating.
    - Description: Customers can submit ratings and reviews for products.

8. Admin Analytics Dashboard
    Aggregate Functions: Generate sales reports based on revenue, popular products, and trends.

9. Promotions & Discounts
    - Description: 
        + Allows admins to create discount codes and special offers.
        + Users can apply promo codes at checkout.