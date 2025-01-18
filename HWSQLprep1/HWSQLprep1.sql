CREATE TABLE category (
    category_id INT PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE products (
    product_id INT PRIMARY KEY,
    name TEXT NOT NULL,
    price INT NOT NULL,
    category_id INT,
    FOREIGN KEY (category_id) REFERENCES category(category_id)
);

CREATE TABLE nutritions (
    nutrition_id INT PRIMARY KEY,
    product_id INT,
    name TEXT,
    calories INT,
    fats INT,
    sugar INT,
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    date_time DATETIME NOT NULL,
    address TEXT NOT NULL,
    customer_name TEXT NOT NULL,
    customer_ph TEXT NOT NULL,
    total_price INT NOT NULL
);

CREATE TABLE products_orders (
    order_id INT,
    product_id INT,
    amount INT NOT NULL,
    PRIMARY KEY (order_id, product_id),
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);
