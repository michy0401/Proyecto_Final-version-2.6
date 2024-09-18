-- Seleccionar la base de datos
USE `Drogueria_inventario`;

-- insert user
INSERT INTO `user` (`user`, `password`) VALUES 
('darg', '123abc'),
('gehr', '456def'),
('arle', '789fghi');
SELECT * FROM `user`;

-- insert job_title
INSERT INTO job_title (job_title) VALUES 
('Manager'),
('Seller'),
('Seller');
SELECT * FROM job_title;

-- insert employee
INSERT INTO employee (id_user, name_employee, address, email, phone_number, id_job_title) VALUES 
('1', 'Daniela Argueta', 'Campos verdes', '20040104@correo.sv', '72765308', '1'),
('2', 'Gerson Hernandez', 'Nuevo lourdes', '20235753@correo.sv', '72511023', '2'),
('3', 'Ariana Lemus', 'Villa', '19790714@correo.sv', '72031573', '2');
SELECT * FROM employee;

-- insert supplier type
INSERT INTO supplier_type (supplier_type) VALUES 
('Mayorista'),
('Minorista');
SELECT * FROM supplier_type;

-- insert supplier
INSERT INTO supplier (id_supplier_type, name, phone_number, email, address, certification, seller_name, seller_phone_number, seller_email) VALUES 
('1', 'Laboratorio Solaris', '7584-9675', 'sdfghj2@labsolaris.com', 'carretera sonsonate', '258963147', 'Pablo Lopez', '5263-4178', 'julo@labsolaris.com'),
('2', 'Farmacia San Nicolas', '2203-6530', 'zxcvbn@sannico.com', 'centro de lourdes', NULL, NULL, NULL, NULL);
SELECT * FROM supplier;

-- insert presentation_type
INSERT INTO presentation_type (presentation_type) VALUES 
('Pastilla'),
('Capsula'),
('Polvo'),
('Inyeccion'),
('Jarabe'),
('Gota'),
('Ampolleta');
SELECT * FROM presentation_type;

-- insert category_product
INSERT INTO category_product (category_product) VALUES 
('Medicamento'),
('Cuidado de bebé'),
('Dsipositivo médico'),
('Suplemento'),
('Otro');
SELECT * FROM category_product;

-- insert brand_product
INSERT INTO brand_product (brand_product) VALUES 
('Nestle'),
('Pampers'),
('Enfamil'),
('Johnsons');
SELECT * FROM brand_product;

-- insert flavor_product
INSERT INTO flavor_product (flavor_product) VALUES 
('Uva'),
('Fresa'),
('Cereza'),
('Coco');
SELECT * FROM flavor_product;

-- insert product
INSERT INTO product (id_presentation_type, id_category_product, id_supplier, name_product, quantity, unit_cost, product_price, expiration_date, id_brand_product, id_flavor_product, required_prescription, recommended_age, instruction, guarantee) VALUES 
(1, 1, 1, 'Paracetamol 500mg', 50, 0.50, 1.00, '2025-12-31', 1, 1, 'Sí', 'Adultos', 'Tomar cada 8 horas', 12),
(2, 2, 2, 'Crema para bebés Johnsons', 30, 3.00, 4.50, '2026-06-30', 4, NULL, 'No', 'Bebés', 'Aplicar después del baño', 24),
(4, 1, 1, 'Antibiótico Amoxicilina', 100, 2.50, 5.00, '2025-09-15', 3, NULL, 'Sí', 'Adultos y Niños', 'Inyectar cada 12 horas', 6),
(5, 4, 2, 'Jarabe para la tos', 60, 1.75, 3.50, '2026-01-20', NULL, 2, 'No', 'Todos', 'Tomar 10ml cada 4 horas', NULL),
(3, 3, 1, 'Proteína en polvo', 40, 10.00, 15.00, '2025-11-25', 2, 3, 'No', 'Adultos', 'Mezclar con agua o leche', 18);
SELECT * FROM product;


INSERT INTO product (id_presentation_type, id_category_product, id_supplier, name_product, quantity, unit_cost, product_price, expiration_date, id_brand_product, id_flavor_product, required_prescription, recommended_age, instruction, guarantee) VALUES 
(5, 4, 2, 'Jarabe', 60, 1.75, 3.50, '2026-01-20', NULL, 2, 'No', 'Todos', 'Tomar 10ml cada 4 horas', NULL);









