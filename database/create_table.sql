CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    product_name VARCHAR(255),
    description TEXT,
    price DECIMAL(10, 2),
    image VARCHAR(255),
    category VARCHAR(255)
);

CREATE TABLE promotions (
    id SERIAL PRIMARY KEY,
    product_id INTEGER,
    start_date DATE,
    end_date DATE,
    discount_percentage DECIMAL(5, 2)
);
