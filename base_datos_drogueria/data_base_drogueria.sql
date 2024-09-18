-- Seleccionar la base de datos
USE `Drogueria_inventario`;

-- User
CREATE TABLE IF NOT EXISTS `user` (
    id_user INT AUTO_INCREMENT NOT NULL,
    `user` VARCHAR(100) NOT NULL,
    password VARCHAR(8) NOT NULL,
    CONSTRAINT user_pk PRIMARY KEY (id_user)
);

-- Job Title
CREATE TABLE IF NOT EXISTS `job_title` (
    id_job_title INT AUTO_INCREMENT NOT NULL,
    job_title VARCHAR(100) NOT NULL,
    CONSTRAINT job_title_pk PRIMARY KEY (id_job_title)
);

-- Employee
CREATE TABLE IF NOT EXISTS `employee` (
    id_employee INT AUTO_INCREMENT NOT NULL,
    id_user INT NOT NULL,
    name_employee VARCHAR(100) NOT NULL,
    address VARCHAR(100) NOT NULL,
    email VARCHAR(50) NOT NULL,
    phone_number VARCHAR(20) NOT NULL,
    id_job_title INT NOT NULL,
    CONSTRAINT employee_pk PRIMARY KEY (id_employee),
    CONSTRAINT fk_employee_user FOREIGN KEY (id_user) REFERENCES `user`(id_user),
    CONSTRAINT fk_employee_job_title FOREIGN KEY (id_job_title) REFERENCES `job_title`(id_job_title)
);

-- Supplier Type
CREATE TABLE IF NOT EXISTS `supplier_type` (
    id_supplier_type INT AUTO_INCREMENT NOT NULL,
    supplier_type VARCHAR(100) NOT NULL,
    CONSTRAINT supplier_type_pk PRIMARY KEY (id_supplier_type)
);

-- Supplier
CREATE TABLE IF NOT EXISTS `supplier` (
    id_supplier INT AUTO_INCREMENT NOT NULL,
    id_supplier_type INT NOT NULL,
    name VARCHAR(100) NOT NULL,
    phone_number VARCHAR(20) NOT NULL,
    email VARCHAR(50) NOT NULL,
    address VARCHAR(100) NOT NULL,
    certification VARCHAR(100) NULL,
    seller_name VARCHAR(100) NULL,
    seller_phone_number VARCHAR(20) NULL,
    seller_email VARCHAR(50) NULL,
    CONSTRAINT supplier_pk PRIMARY KEY (id_supplier),
    CONSTRAINT fk_supplier_supplier_type FOREIGN KEY (id_supplier_type) REFERENCES `supplier_type`(id_supplier_type)
);

-- Presentation Type
CREATE TABLE IF NOT EXISTS `presentation_type` (
    id_presentation_type INT AUTO_INCREMENT NOT NULL,
    presentation_type VARCHAR(100) NOT NULL,
    CONSTRAINT presentation_type_pk PRIMARY KEY (id_presentation_type)
);

-- Category Product
CREATE TABLE IF NOT EXISTS `category_product` (
    id_category_product INT AUTO_INCREMENT NOT NULL,
    category_product VARCHAR(100) NOT NULL,
    CONSTRAINT category_product_pk PRIMARY KEY (id_category_product)
);

-- Brand Product
CREATE TABLE IF NOT EXISTS `brand_product` (
    id_brand_product INT AUTO_INCREMENT NOT NULL,
    brand_product VARCHAR(100) NOT NULL,
    CONSTRAINT brand_product_pk PRIMARY KEY (id_brand_product)
);

-- Flavor Product
CREATE TABLE IF NOT EXISTS `flavor_product` (
    id_flavor_product INT AUTO_INCREMENT NOT NULL,
    flavor_product VARCHAR(100) NOT NULL,
    CONSTRAINT flavor_product_pk PRIMARY KEY (id_flavor_product)
);

-- Product
CREATE TABLE IF NOT EXISTS `product` (
    id_product INT AUTO_INCREMENT NOT NULL,
    id_presentation_type INT NOT NULL,
    id_category_product INT NOT NULL,
    id_supplier INT NOT NULL,
    name_product VARCHAR(100) NOT NULL,
    quantity INT NOT NULL,
    unit_cost FLOAT(10,2) NOT NULL,
    product_price FLOAT(10,2) NOT NULL,
    expiration_date DATE NOT NULL,
    id_brand_product INT NULL,
    id_flavor_product INT NULL,
    required_prescription VARCHAR(100) NULL,
    recommended_age VARCHAR(100) NULL,
    instruction VARCHAR(100) NULL,
    guarantee INT NULL,
    CONSTRAINT product_pk PRIMARY KEY (id_product),
    CONSTRAINT fk_product_presentation_type FOREIGN KEY (id_presentation_type) REFERENCES `presentation_type`(id_presentation_type),
    CONSTRAINT fk_product_category_product FOREIGN KEY (id_category_product) REFERENCES `category_product`(id_category_product),
    CONSTRAINT fk_product_supplier FOREIGN KEY (id_supplier) REFERENCES `supplier`(id_supplier),
    CONSTRAINT fk_product_brand_product FOREIGN KEY (id_brand_product) REFERENCES `brand_product`(id_brand_product),
    CONSTRAINT fk_product_flavor_product FOREIGN KEY (id_flavor_product) REFERENCES `flavor_product`(id_flavor_product)
);
