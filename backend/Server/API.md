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
    - **Success** (Customer):
        ```json
        {
            "message": "User registered successfully",
            "email": "string",
            "name": "string",
            "customer_id": "int"
        }
        ```
    - **Success** (Admin):
        ```json
        {
            "message": "User registered successfully",
            "email": "string",
            "name": "string",
            "admin_id": "int"
        }
        ```
    - **Error**:
        ```json
        {
            "error": "Database error: ...details..."
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
    - **Success** (Customer):
        ```json
        {
            "message": "Login successful",
            "user_type": "Customer",
            "email": "string",
            "name": "string",
            "customer_id": "int"
        }
        ```
    - **Success** (Admin):
        ```json
        {
            "message": "Login successful",
            "user_type": "Admin",
            "email": "string",
            "name": "string",
            "admin_id": "int"
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
            "error": "Database error: ...details..."
        }
        ```
    1. Product management (admin side): 
    - **Description**: Admins can add, update, and remove products from the catalog.

    ### Insert Product
    - **Path**: `/admin/add_product`
    - **Method**: `POST`
    - **Request Body**:
        ```json
        {
            "name": "string",
            "description": "string",
            "price": "float",
            "category_id": "int",
            "supplier_id": "int",
            "warranty_period": "int"
        }
        ```
    - **Response**:
        - **Success**:
        ```json
        {
            "success": true,
            "message": "Product created successfully."
        }
        ```
        - **Error**:
        ```json
        {
            "success": false,
            "error": "Error message"
        }
        ```

    ### Update Product
    - **Path**: `/admin/update_product`
    - **Method**: `POST`
    - **Request Body**:
        ```json
        {
            "product_id": "int",           // Required
            "name": "string",              // Optional
            "description": "string",       // Optional
            "price": "float",              // Optional
            "category_id": "int",          // Optional
            "supplier_id": "int",          // Optional
            "warranty_period": "int"       // Optional
        }
        ```
    - **Response**:
        - **Success**:
        ```json
        {
            "success": true,
            "message": "Product updated successfully."
        }
        ```
        - **Error**:
        ```json
        {
            "success": false,
            "error": "Error message"
        }
        ```

    ### Delete Product
    - **Path**: `/admin/remove_product`
    - **Method**: `POST`
    - **Request Body**:
        ```json
        {
            "product_id": "int"
        }
        ```
    - **Response**:
        - **Success**:
        ```json
        {
            "success": true,
            "message": "Product removed successfully."
        }
        ```
        - **Error**:
        ```json
        {
            "success": false,
            "error": "Error message"
        }
        ```

2. Product browsing and search:
    - **Path**: `/products`
    - **Method**: `GET`
    - **Description**: Allows customers to browse and search for products using various filters such as category, price range, brand, and rating.
    - **Query Parameters**:
        + category_id (optional): Filters products by category ID.
        + category_name (optional): Filters products by category name.
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
                or 
                GET /products?category_name=Mobile_phone
        + Filter by price range:
                GET /products?min_price=100&max_price=500
        + Filter by brand:
                GET /products?brand=Samsung
        + Filter by rating
                GET /products?rating=4
        + Composite filter: 
                GET /products?min_price=100&max_price=500&brand=Samsung&rating=4

3. Shopping Cart Functionality
    
     #### **Add Product to Cart**
    - **Path**: `/shoppingcart/add`
    - **Method**: `POST`
    - **Description**: Adds a product to the user's shopping cart.
    - **Request Body**:
        ```json
        {
            "customer_id": "int",
            "order_id": "int",
            "product_id": "int",
            "quantity": "int"
        }
        ```
    - **Response**:
        - **Success**:
            ```json
            {
                "message": "Product added to cart successfully"
            }
            ```
        - **Error**:
            ```json
            {
                "error": "Product not found or insufficient stock",
                "status": 400
            }
            ```
        - **Database Error**:
            ```json
            {
                "error": "Database error",
                "details": "string",
                "status": 500
            }
            ```

    #### **Update Product Quantity in Cart**
    - **Path**: `/shoppingcart/update`
    - **Method**: `POST`
    - **Description**: Updates the quantity of a product in the user's shopping cart.
    - **Request Body**:
        ```json
        {
            "order_item_id": "int",
            "quantity": "int"
        }
        ```
    - **Response**:
        - **Success**:
            ```json
            {
                "message": "Cart updated successfully"
            }
            ```
        - **Error**:
            ```json
            {
                "error": "Invalid input or database error",
                "details": "string",
                "status": 500
            }
            ```

    #### **Remove Product from Cart**
    - **Path**: `/shoppingcart/remove`
    - **Method**: `POST`
    - **Description**: Removes a product from the user's shopping cart.
    - **Request Body**:
        ```json
        {
            "order_item_id": "int"
        }
        ```
    - **Response**:
        - **Success**:
            ```json
            {
                "message": "Product removed from cart successfully"
            }
            ```
        - **Error**:
            ```json
            {
                "error": "Invalid input or database error",
                "details": "string",
                "status": 500
            }
            ```

    #### **Notes**:
    - The `order_id` is required to associate the cart with a specific order.
    - The `product_id` and `quantity` are validated to ensure the product exists and there is sufficient stock.
    - All database operations are handled with proper exception handling to ensure stability.

4. Order Processing & Checkout
    #### **Place an Order**
    - **Path**: `/order/checkout`
    - **Method**: `POST`
    - **Description**: Processes an order for a customer, deducts inventory, and creates a payment entry.
    - **Request Body**:
        ```json
        {
            "customer_id": "int",
            "order_id": "int",
            "payment_method": "string"
        }
        ```
    - **Response**:
        - **Success**:
            ```json
            {
                "message": "Order processed successfully",
                "order_id": "int",
                "status": 200
            }
            ```
        - **Error**:
            ```json
            {
                "error": "Order not found or does not belong to the customer",
                "status": 404
            }
            ```
        - **Invalid Status**:
            ```json
            {
                "error": "Order is not in 'In Cart' status",
                "status": 400
            }
            ```
        - **Empty Cart**:
            ```json
            {
                "error": "No items in the cart to process",
                "status": 400
            }
            ```
        - **Database Error**:
            ```json
            {
                "error": "Database error",
                "details": "string",
                "status": 500
            }
            ```

    #### **Cancel an Order**
    - **Path**: `/order/cancel`
    - **Method**: `POST`
    - **Description**: Cancels an order and restores inventory for all associated items.
    - **Request Body**:
        ```json
        {
            "customer_id": "int",
            "order_id": "int"
        }
        ```
    - **Response**:
        - **Success**:
            ```json
            {
                "message": "Order canceled successfully",
                "order_id": "int",
                "status": 200
            }
            ```
        - **Error**:
            ```json
            {
                "error": "Order not found or does not belong to the customer",
                "status": 404
            }
            ```
        - **Invalid Status**:
            ```json
            {
                "error": "Order cannot be canceled as it is already processed",
                "status": 400
            }
            ```
        - **Database Error**:
            ```json
            {
                "error": "Database error",
                "details": "string",
                "status": 500
            }
            ```

    #### **Fetch Order Details**
    - **Path**: `/order/fetch`
    - **Method**: `GET`
    - **Description**: Retrieves details of a specific order, including items and their quantities.
    - **Query Parameters**:
        - `order_id` (required): The ID of the order to fetch.
        - `customer_id` (required): The ID of the customer who owns the order.
    - **Response**:
        - **Success**:
            ```json
            {
                "order_id": "int",
                "customer_id": "int",
                "status": "string",
                "total_amount": "float",
                "items": [
                    {
                        "product_id": "int",
                        "name": "string",
                        "quantity": "int",
                        "unit_price": "float"
                    },
                    ...
                ]
            }
            ```
        - **Error**:
            ```json
            {
                "error": "Order not found or does not belong to the customer",
                "status": 404
            }
            ```
        - **Database Error**:
            ```json
            {
                "error": "Database error",
                "details": "string",
                "status": 500
            }
            ```

    #### **Notes**:
    - **Order Status**:
        - Orders must have the status "In Cart" to be processed.
        - Orders with statuses other than "In Cart" cannot be modified or canceled.
    - **Inventory Management**:
        - When an order is processed, inventory quantities are deducted.
        - When an order is canceled, inventory quantities are restored.
    - **Payment Integration**:
        - Payment entries are created with the status "Pending" during checkout.
        - Payment status updates (e.g., "Completed") are handled separately.

5. Payment Gateway Integration
    - Description: Customers can pay via multiple payment methods (credit card, PayPal, etc.).

6. Order History & Tracking

    #### **Fetch Order History**
    - **Path**: `/order/history`
    - **Method**: `GET`
    - **Description**: Retrieves a list of all past orders for a specific customer, including order status, total amount, and order date.
    - **Query Parameters**:
        - `customer_id` (required): The ID of the customer whose order history is to be fetched.
    - **Response**:
        - **Success**:
            ```json
            [
                {
                    "order_id": "int",
                    "total": "float",
                    "order_date": "string" // e.g., "2024-06-01"
                },
                ...
            ]
            ```
        - **Error**:
            ```json
            {
                "error": "Missing customer_id",
                "status": 400
            }
            ```
            ```json
            {
                "error": "Database error",
                "details": "string",
                "status": 500
            }
            ```

    #### **Fetch Order Details**
    - **Path**: `/order/fetch`
    - **Method**: `GET`
    - **Description**: Retrieves detailed information for a specific order, including all items, their quantities, and prices.
    - **Query Parameters**:
        - `order_id` (required): The ID of the order to fetch.
        - `customer_id` (required): The ID of the customer who owns the order.
    - **Response**:
        - **Success**:
            ```json
            {
                "order_id": "int",
                "customer_id": "int",
                "status": "string",
                "total_amount": "float",
                "items": [
                    {
                        "product_id": "int",
                        "name": "string",
                        "quantity": "int",
                        "unit_price": "float"
                    },
                    ...
                ]
            }
            ```
        - **Error**:
            ```json
            {
                "error": "Order not found or does not belong to the customer",
                "status": 404
            }
            ```
            ```json
            {
                "error": "Missing order_id or customer_id",
                "status": 400
            }
            ```
            ```json
            {
                "error": "Database error",
                "details": "string",
                "status": 500
            }
            ```

    **Notes**:
    - Customers can view all their past orders and track the status and date of each order.
    - Each order includes a list of purchased items and their details.

7. Reviews & Ratings

    #### **Submit a Product Review and Rating**
    - **Path**: `/products/rating/`
    - **Method**: `POST`
    - **Description**: Allows a customer to submit a rating and optional review comment for a product. The rating must be an integer between 1 and 5. Each review is associated with a customer and a product.
    - **Request Body**:
        ```json
        {
            "product_id": "int",      // Required. The ID of the product being reviewed.
            "customer_id": "int",     // Required. The ID of the customer submitting the review.
            "rating": "int",          // Required. Rating value (1-5).
            "comment": "string"       // Optional. Review comment.
        }
        ```
    - **Response**:
        - **Success**:
            ```json
            {
                "message": "Review submitted successfully"
            }
            ```
        - **Validation Error**:
            ```json
            {
                "error": "Missing required fields"
            }
            ```
            ```json
            {
                "error": "Invalid data type for product_id, customer_id, or rating"
            }
            ```
            ```json
            {
                "error": "Rating must be between 1 and 5."
            }
            ```
        - **Database Error**:
            ```json
            {
                "error": "Database error",
                "details": "string"
            }
            ```

    #### **Product Browsing with Average Rating**
    - **Path**: `/products`
    - **Method**: `GET`
    - **Description**: Allows customers to browse and search for products. Each product includes its average rating, calculated from all submitted reviews.
    - **Query Parameters**:
        - `category_id` (optional): Filter by category.
        - `min_price` (optional): Minimum price.
        - `max_price` (optional): Maximum price.
        - `brand` (optional): Filter by brand name.
        - `rating` (optional): Minimum average rating.
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

    **Notes:**
    - Customers can only submit ratings between 1 and 5.
    - The average rating for each product is automatically calculated and included in product search results.
8. Admin Analytics Dashboard
    Aggregate Functions: Generate sales reports based on revenue, popular products, and trends.7. Reviews & Ratings
    Aggregate Functions: Calculate average product rating.
    - Description: Customers can submit ratings and reviews for products.


9. Promotions & Discounts
    - Description: 
        + Allows admins to create discount codes and special offers.
        + Users can apply promo codes at checkout.

10. Marketing functions

    #### **Fetch Marketing Images**
    - **Path**: `/products/marketing`
    - **Method**: `GET`
    - **Description**: Returns a list of marketing image URLs for products (up to 5).
    - **Response**:
        - **Success**:
            ```json
            {
                "links": [
                    "https://example.com/image1.jpg",
                    "https://example.com/image2.jpg",
                    ...
                ]
            }
            ```
        - **Error**:
            ```json
            {
                "error": "No imgs found"
            }
            ```
            ```json
            {
                "error": "An unexpected error occured",
                "details": "string"
            }
            ```

11. Product page:

    #### **Fetch Product Detail**
    - **Path**: `/product`
    - **Method**: `GET`
    - **Description**: Returns all relevant details of a product, including inventory information, for adding to cart.
    - **Query Parameters**:
        - `product_id` (required): The ID of the product to fetch.
    - **Response**:
        - **Success**:
            ```json
            {
                "product": {
                    "ProductID": "int",
                    "Name": "string",
                    "Description": "string",
                    "Price": "float",
                    "CategoryID": "int",
                    "CategoryName": "string",
                    "SupplierID": "int",
                    "SupplierName": "string",
                    "WarrantyPeriod": "int",
                    "Marketting_Img": "string",
                    "QuantityInStock": "int",
                    "ReorderLevel": "int",
                    "AvgRating": "float",
                    "reviews": [
                        {
                            "Rating": "int",
                            "Comment": "string",
                            "ReviewDate": "string",
                            "CustomerID": "int"
                        },
                        ...
                    ]
                }
            }
            ```
        - **Error**:
            ```json
            {
                "error": "Product not found."
            }
            ```
            ```json
            {
                "error": "Database error",
                "details": "string"
            }
            ```

    **Notes:**
    - The response includes product information, inventory (stock), supplier, category, average rating, and up to 3 recent reviews.
    - Use this endpoint to display product details and check inventory before adding to cart.