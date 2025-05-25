--DROP DATABASE IF EXISTS E_retail;
CREATE DATABASE E_Retail;
USE E_Retail;

CREATE TABLE Category (
    CategoryID INT PRIMARY KEY IDENTITY(1,1),
    CategoryName VARCHAR(100),

);

CREATE TABLE Supplier (
    SupplierID INT PRIMARY KEY IDENTITY(1,1),
    Name VARCHAR(100),
    ContactName VARCHAR(100),
    Phone VARCHAR(20),
    Email VARCHAR(100),
    Address VARCHAR(255)
);

CREATE TABLE Users (
    UserID INT PRIMARY KEY IDENTITY(1,1),
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Email VARCHAR(100) UNIQUE,
    Phone VARCHAR(20),
    Address VARCHAR(255),
    City VARCHAR(50),
    State VARCHAR(50),
    ZipCode VARCHAR(10),
    RegistrationDate DATE,
    password VARCHAR(255),
    UserType VARCHAR(20) CHECK (UserType IN ('Admin', 'Customer'))
);

CREATE TABLE Admin (
    AdminID INT PRIMARY KEY IDENTITY(1,1),
    UserID INT UNIQUE,
    Role VARCHAR(50),
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE
);

CREATE TABLE Customer (
    CustomerID INT PRIMARY KEY IDENTITY(1,1),
    UserID INT UNIQUE,
    LoyaltyPoints INT DEFAULT 0,
    FOREIGN KEY (UserID) REFERENCES Users(UserID) ON DELETE CASCADE
);


CREATE TABLE Product (
    ProductID INT PRIMARY KEY IDENTITY(1,1),
    Name VARCHAR(100),
    Description VARCHAR(MAX),
    Price DECIMAL(10,2),
    CategoryID INT,
    SupplierID INT,
    WarrantyPeriod INT,
    Marketting_Img VARCHAR(255),
    FOREIGN KEY (CategoryID) REFERENCES Category(CategoryID),
    FOREIGN KEY (SupplierID) REFERENCES Supplier(SupplierID)
);

CREATE TABLE Inventory (
    ProductID INT PRIMARY KEY,
    QuantityInStock INT,
    ReorderLevel INT,
    FOREIGN KEY (ProductID) REFERENCES Product(ProductID)
);

CREATE TABLE Orders (
    OrderID INT PRIMARY KEY IDENTITY(1,1),
    CustomerID INT,
    OrderDate DATE,
    Status VARCHAR(50), -- In cart, Pending, Completed, Canceled
    TotalAmount DECIMAL(10,2),
    FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID)
);

CREATE TABLE OrderItem (
    OrderItemID INT PRIMARY KEY IDENTITY(1,1),
    OrderID INT,
    ProductID INT,
    Quantity INT,
    UnitPrice DECIMAL(10,2),
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID),
    FOREIGN KEY (ProductID) REFERENCES Product(ProductID)
);

CREATE TABLE Payment (
    PaymentID INT PRIMARY KEY IDENTITY(1,1),
    OrderID INT,
    PaymentDate DATE,
    PaymentMethod VARCHAR(50),
    Amount DECIMAL(10,2),
    PaymentStatus VARCHAR(50),
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID)
);

CREATE TABLE Shipping (
    ShippingID INT PRIMARY KEY IDENTITY(1,1),
    OrderID INT,
    ShippingMethod VARCHAR(50),
    TrackingNumber VARCHAR(100),
    ShippingDate DATE,
    EstimatedArrival DATE,
    ShippingStatus VARCHAR(50),
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID)
);

CREATE TABLE Review (
    ReviewID INT PRIMARY KEY IDENTITY(1,1),
    CustomerID INT,
    ProductID INT,
    Rating INT CHECK (Rating BETWEEN 1 AND 5),
    Comment VARCHAR(MAX), 
    ReviewDate DATE,
    FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID),
    FOREIGN KEY (ProductID) REFERENCES Product(ProductID)
);
