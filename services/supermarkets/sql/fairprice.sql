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
  (1, 'Star Anise', 100, 3.50),
  (2, 'Cardamom', 150, 0.25),
  (3, 'Coconut Cream', 25, 5.35),
  (4, 'Beef', 75, 10),
  (5, 'Vegetable Oil', 75, 3),
  (6, 'Cinnamon Stick', 75, 2),
  (7, 'Cloves', 100, 0.90),
  (8, 'Water', 75, 0.55),
  (9, 'Tamarind Paste', 75, 1.35),




-- Check data in the fairpriceStock table
-- SELECT * FROM fairpriceStock;