CREATE TABLE products
(
    id SERIAL PRIMARY KEY,
    code VARCHAR(20) UNIQUE NOT NULL,
    name VARCHAR(100) NOT NULL
);

CREATE TABLE materials
(
    id SERIAL PRIMARY KEY,
    code VARCHAR(20) UNIQUE NOT NULL,
    name VARCHAR(100) NOT NULL
);

CREATE TABLE inventory
(
    material_id INTEGER PRIMARY KEY,
    stock INTEGER NOT NULL,

    FOREIGN KEY(material_id)
        REFERENCES materials(id)
);

CREATE TABLE bill_of_materials
(
    product_id INTEGER,
    material_id INTEGER,
    quantity_required INTEGER NOT NULL,

    PRIMARY KEY(product_id, material_id),

    FOREIGN KEY(product_id)
        REFERENCES products(id),

    FOREIGN KEY(material_id)
        REFERENCES materials(id)
);

CREATE TABLE sales_orders
(
    id SERIAL PRIMARY KEY,

    product_id INTEGER NOT NULL,

    quantity INTEGER NOT NULL,

    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY(product_id)
        REFERENCES products(id)
);
