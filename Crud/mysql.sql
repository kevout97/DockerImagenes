CREATE DATABASE crud_certificates;
CREATE TABLE crud_certificates.domains (id INT PRIMARY KEY AUTO_INCREMENT,fulldomain VARCHAR(500), expiration_date DATE, description VARCHAR(1500));