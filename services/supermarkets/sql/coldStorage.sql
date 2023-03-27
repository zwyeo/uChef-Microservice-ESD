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
  (1, 'Chicken Breast', 20, 11.50),
  (2, 'Pickle Juice', 35, 2.80),
  (3, 'Egg', 75, 5.40),
  (4, 'Milk', 75, 2.40),
  (5, ' Flour', 75, 1.40),
  (6, 'Icing Sugar', 75, 3),
  (7, 'Paprika', 75, 4.50),
  (8, 'Salt', 75, 1.40),
  (9, 'Black Pepper', 75, 3.20),
  (10, 'Garlic Powder', 75, 4.20),
  (11, 'Celery Salt', 75, 1.20),
  (12, 'Cayenne Pepper', 75, 4.20),
  (13, 'Olive Oil', 75, 2.20),
  (14, 'Sesame Seed Burger Buns', 75, 3.20);
  


-- Check data in the coldStorageStock table
-- SELECT * FROM coldStorageStock;