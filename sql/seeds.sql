------------------------------------------------------
-- PRODUCTOS
------------------------------------------------------

INSERT INTO products
(
    code,
    name
)
VALUES
(
    'PC001',
    'Gaming PC'
);

------------------------------------------------------
-- MATERIALES
------------------------------------------------------

INSERT INTO materials
(
    code,
    name
)
VALUES
('CPU001','CPU Ryzen 7'),
('MB001','Motherboard B650'),
('RAM001','RAM 16GB DDR5'),
('SSD001','SSD 1TB NVMe'),
('PSU001','Power Supply 750W'),
('GPU001','Graphics Card RTX');

------------------------------------------------------
-- INVENTARIO
------------------------------------------------------

INSERT INTO inventory
(
    material_id,
    stock
)
VALUES
(1,50),
(2,45),
(3,200),
(4,75),
(5,40),
(6,20);

------------------------------------------------------
-- BILL OF MATERIALS
------------------------------------------------------

INSERT INTO bill_of_materials
(
    product_id,
    material_id,
    quantity_required
)
VALUES
(1,1,1), -- CPU
(1,2,1), -- Motherboard
(1,3,2), -- RAM
(1,4,1), -- SSD
(1,5,1), -- PSU
(1,6,1); -- GPU

------------------------------------------------------
-- NOTA
------------------------------------------------------
-- Las órdenes de venta NO se insertan aquí.
-- Serán creadas dinámicamente por seed_data.py
-- utilizando ORDER_QUANTITY.
------------------------------------------------------
