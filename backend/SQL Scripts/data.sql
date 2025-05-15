INSERT INTO Category (CategoryName, ParentCategoryID) VALUES 
('Electronics', NULL),
('Mobile Phones', 1),
('Laptops', 1),
('Accessories', 1),
('Furniture', NULL);

INSERT INTO Supplier (Name, ContactName, Phone, Email, Address) VALUES 
('TechWorld', 'Alice Johnson', '1234567890', 'alice@techworld.com', '123 Tech Street'),
('GadgetHub', 'Bob Smith', '0987654321', 'bob@gadgethub.com', '456 Gadget Avenue'),
('HomeStyle', 'Charlie Brown', '1122334455', 'charlie@homestyle.com', '789 Home Lane'),
('SmartTech', 'Diana Green', '2233445566', 'diana@smarttech.com', '321 Smart Road'),
('TrendMaker', 'Ethan White', '3344556677', 'ethan@trendmaker.com', '654 Trend Plaza');

INSERT INTO Users (FirstName, LastName, Email, Phone, Address, City, State, ZipCode, RegistrationDate, UserType) VALUES 
('John', 'Doe', 'johndoe@email.com', '9876543210', '123 Main St', 'New York', 'NY', '10001', '2023-01-15', 'Customer'),
('Jane', 'Smith', 'janesmith@email.com', '8765432109', '456 Broadway', 'Los Angeles', 'CA', '90001', '2023-02-20', 'Customer'),
('Bob', 'Johnson', 'bobjohnson@email.com', '7654321098', '789 Elm St', 'Chicago', 'IL', '60601', '2023-03-25', 'Customer'),
('Alice', 'Williams', 'alicewilliams@email.com', '6543210987', '321 Oak St', 'Houston', 'TX', '77001', '2023-04-10', 'Customer'),
('Charlie', 'Brown', 'charliebrown@email.com', '5432109876', '654 Pine St', 'Miami', 'FL', '33101', '2023-05-05', 'Customer'),
('Eve', 'Adams', 'eveadams@email.com', '4321098765', '101 Maple St', 'San Francisco', 'CA', '94101', '2023-06-10', 'Admin'),
('Frank', 'Taylor', 'franktaylor@email.com', '3210987654', '202 Willow St', 'Seattle', 'WA', '98101', '2023-07-20', 'Admin');

INSERT INTO Customer (UserID, LoyaltyPoints) VALUES 
((SELECT UserID FROM Users WHERE Email='johndoe@email.com'), 150),
((SELECT UserID FROM Users WHERE Email='janesmith@email.com'), 200),
((SELECT UserID FROM Users WHERE Email='bobjohnson@email.com'), 120),
((SELECT UserID FROM Users WHERE Email='alicewilliams@email.com'), 250),
((SELECT UserID FROM Users WHERE Email='charliebrown@email.com'), 180);

INSERT INTO Admin (UserID, Role) VALUES 
((SELECT UserID FROM Users WHERE Email='eveadams@email.com'), 'Manager'),
((SELECT UserID FROM Users WHERE Email='franktaylor@email.com'), 'Supervisor');

INSERT INTO Product (Name, Description, Price, CategoryID, SupplierID, WarrantyPeriod) VALUES 
('iPhone 14', 'Latest Apple iPhone with A15 Bionic', 999.99, 2, 1, 24),
('MacBook Air', 'Lightweight Apple laptop with M1 chip', 1199.99, 3, 1, 36),
('Wireless Earbuds', 'High-quality audio with noise cancellation', 199.99, 4, 2, 12),
('Office Chair', 'Ergonomic chair for comfortable working', 299.99, 5, 3, 24),
('Smartwatch', 'Advanced features for fitness tracking', 249.99, 4, 4, 18);

INSERT INTO Inventory (ProductID, QuantityInStock, ReorderLevel) VALUES 
(1, 50, 10),
(2, 30, 5),
(3, 100, 20),
(4, 25, 5),
(5, 40, 10);

INSERT INTO Orders (CustomerID, OrderDate, Status, TotalAmount) VALUES 
(1, '2025-05-01', 'Completed', 999.99),
(2, '2025-05-02', 'Pending', 1199.99),
(3, '2025-05-03', 'Shipped', 199.99),
(4, '2025-05-04', 'Completed', 299.99),
(5, '2025-05-05', 'Processing', 249.99);

INSERT INTO OrderItem (OrderID, ProductID, Quantity, UnitPrice) VALUES 
(1, 1, 1, 999.99),
(2, 2, 1, 1199.99),
(3, 3, 2, 199.99),
(4, 4, 1, 299.99),
(5, 5, 1, 249.99);

INSERT INTO Payment (OrderID, PaymentDate, PaymentMethod, Amount, PaymentStatus) VALUES 
(1, '2025-05-01', 'Credit Card', 999.99, 'Completed'),
(2, '2025-05-02', 'PayPal', 1199.99, 'Pending'),
(3, '2025-05-03', 'Debit Card', 199.99, 'Completed'),
(4, '2025-05-04', 'Bank Transfer', 299.99, 'Completed'),
(5, '2025-05-05', 'Cash on Delivery', 249.99, 'Processing');

INSERT INTO Shipping (OrderID, ShippingMethod, TrackingNumber, ShippingDate, EstimatedArrival, ShippingStatus) VALUES 
(1, 'FedEx', 'FX123456', '2025-05-02', '2025-05-05', 'Delivered'),
(2, 'UPS', 'UP987654', '2025-05-03', '2025-05-06', 'In Transit'),
(3, 'DHL', 'DH456789', '2025-05-04', '2025-05-07', 'Shipped'),
(4, 'USPS', 'US789123', '2025-05-05', '2025-05-08', 'Delivered'),
(5, 'Local Carrier', 'LC321456', '2025-05-06', '2025-05-09', 'Processing');

INSERT INTO Review (CustomerID, ProductID, Rating, Comment, ReviewDate) VALUES 
(1, 1, 5, 'Amazing phone with great performance!', '2025-05-10'),
(2, 2, 4, 'Very efficient laptop, but a bit pricey.', '2025-05-11'),
(3, 3, 5, 'Fantastic audio quality, highly recommend!', '2025-05-12'),
(4, 4, 3, 'Comfortable chair but took time to assemble.', '2025-05-13'),
(5, 5, 5, 'Perfect smartwatch for fitness tracking!', '2025-05-14');
