-- schema.sql

CREATE DATABASE IF NOT EXISTS portfolio_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE portfolio_db;

-- tabla admin
CREATE TABLE IF NOT EXISTS admin (
  id INT AUTO_INCREMENT PRIMARY KEY,
  username VARCHAR(100) NOT NULL UNIQUE,
  password VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- tabla personal 
CREATE TABLE IF NOT EXISTS personal (
  id INT PRIMARY KEY,
  name VARCHAR(200),
  title VARCHAR(200),
  phone VARCHAR(100),
  email VARCHAR(200),
  about TEXT,
  linkedin VARCHAR(255),
  github VARCHAR(255)
);

-- tabla experience
CREATE TABLE IF NOT EXISTS experience (
  id INT AUTO_INCREMENT PRIMARY KEY,
  company VARCHAR(200),
  role VARCHAR(200),
  start_date VARCHAR(50),
  end_date VARCHAR(50),
  description TEXT
);

-- tabla skills
CREATE TABLE IF NOT EXISTS skills (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100),
  level INT DEFAULT 1
);

-- seed inicial
INSERT INTO personal (id, name, title, phone, email, about, linkedin, github)
VALUES (1, 'Mateo ulla', 'Estudiante - Programacion y AI', '(351) 810-4498', 'mateoullaa@gmail.com',
' Estudiante de Programacion con orientacion en Inteligencia Artificial y Finanzas. Fundador de emprendimiento de detailing. En busca de oportunidades.', 
'https://ar.linkedin.com/in/mateo-ulla-08857636b', 'https://github.com/mateo-ulla');

-- datos de ejemplo
INSERT INTO experience (company, role, start_date, end_date, description) VALUES
('Prodetailing', 'Fundador', '2020', '2023', 'Creacion y gestion de emprendimiento de detailing automotriz. Marketing digital y Atencion al cliente.'),
('Instituto Tecnico Renault', 'Estudios', '2023', "Actualidad", 'Estudios y proyectos en programacion.');

INSERT INTO skills (name, level) VALUES
('Python', 5),
('SQL', 4),
('Flask', 4),
('Javascript', 3);
