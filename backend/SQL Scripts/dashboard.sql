-- All dbs
SELECT name FROM sys. databases

-- All custom tables
SELECT TABLE_NAME 
FROM INFORMATION_SCHEMA.TABLES 
WHERE TABLE_TYPE = 'BASE TABLE' AND TABLE_SCHEMA = 'dbo';

-- Number of custom tables
SELECT COUNT(*) AS TotalTables
FROM INFORMATION_SCHEMA.TABLES
WHERE TABLE_TYPE = 'BASE TABLE' AND TABLE_SCHEMA = 'dbo';

-- Show all tuples from Category
SELECT * FROM Category;

-- Show all tuples from Supplier
SELECT * FROM Supplier;

-- Show all tuples from Customer
SELECT * FROM Customer;

SELECT * FROM Users

SELECT * FROM Admin;

-- Show all tuples from Product
SELECT * FROM Product;

-- Show all tuples from Inventory
SELECT * FROM Inventory;    
SELECT * FROM Inventory JOIN Product ON Inventory.ProductID = Product.ProductID;
-- Show all tuples from Orders
SELECT * FROM Orders;

-- Show all tuples from OrderItem
SELECT * FROM OrderItem;

-- Corrected join query
SELECT *
FROM Product
JOIN OrderItem ON Product.ProductID = OrderItem.ProductID
JOIN Orders ON OrderItem.OrderID = Orders.OrderID;

-- Another valid join query
SELECT *
FROM Product
JOIN OrderItem ON Product.ProductID = OrderItem.ProductID;


        

-- Show all tuples from Payment
SELECT * FROM Payment;

-- Show all tuples from Shipping
SELECT * FROM Shipping;

-- Show all tuples from Review
SELECT * FROM Review;

-- Test user: lethaihung142@gmail.com 111111111