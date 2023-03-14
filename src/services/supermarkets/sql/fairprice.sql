-- Create a new schema
CREATE SCHEMA fairprice;
USE fairprice;

-- Create a table for fairprice
CREATE TABLE fairpriceStock (
  id INT PRIMARY KEY,
  itemName VARCHAR(50) NOT NULL,
  quantity INT NOT NULL,
  price DECIMAL(10,2) NOT NULL
);

-- Insert sample data into the fairpriceStock table
INSERT INTO fairpriceStock (id, itemName, quantity, price) VALUES
  (1, 'Apple', 100, 0.50),
  (2, 'Banana', 150, 0.25),
  (3, 'Orange', 75, 0.35);

-- Check data in the fairpriceStock table
-- SELECT * FROM fairpriceStock;