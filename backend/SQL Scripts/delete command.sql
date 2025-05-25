-- Delete order items related to orders with status 'In cart'
DELETE FROM OrderItem
WHERE OrderID IN (
    SELECT OrderID FROM Orders WHERE Status = 'In cart'
);

-- Delete orders with status 'In cart'
DELETE FROM Orders
WHERE Status = 'In cart';

----------------------

-- Replace @TargetOrderID with the actual OrderID you want to delete
DECLARE @TargetOrderID INT = 2006; -- Example value

-- Step 1: Delete from child tables first (due to foreign key constraints)
DELETE FROM Payment WHERE OrderID = @TargetOrderID;
DELETE FROM Shipping WHERE OrderID = @TargetOrderID;
DELETE FROM OrderItem WHERE OrderID = @TargetOrderID;

-- Step 2: Delete the order
DELETE FROM Orders WHERE OrderID = @TargetOrderID;


-------------------------