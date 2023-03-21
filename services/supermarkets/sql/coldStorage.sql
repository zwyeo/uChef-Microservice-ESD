-- Create a new schema
CREATE SCHEMA coldStorage;
USE coldStorage;

-- Create a table for coldStorage
CREATE TABLE coldStorageStock (
  id INT PRIMARY KEY,
  itemName VARCHAR(50) NOT NULL,
  quantity INT NOT NULL,
  price DECIMAL(10,2) NOT NULL
);

-- Insert sample data into the coldStorageStock table
INSERT INTO coldStorageStock (id, itemName, quantity, price) VALUES
  (1, 'Lime', 20, 1.50),
  (2, 'Sugar', 35, 0.80),
  (3, 'Challots', 75, 0.40);


-- Check data in the coldStorageStock table
-- SELECT * FROM coldStorageStock;