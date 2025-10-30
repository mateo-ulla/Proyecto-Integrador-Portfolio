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

-- tabla personal (solo un registro con id=1)
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

-- seed inicial: personal con id=1
INSERT INTO personal (id, name, title, phone, email, about, linkedin, github)
VALUES (1, 'mateo ulla', 'estudiante - programacion y ai', '(351) 810-4498', 'mateoullaa@gmail.com',
' estudiante de programacion con orientacion en inteligencia artificial y finanzas. fundador de emprendimiento de detailing. en busca de oportunidades.', 
'https://ar.linkedin.com/in/mateo-ulla-08857636b', 'https://github.com/mateo-ulla');

-- algunos datos de ejemplo
INSERT INTO experience (company, role, start_date, end_date, description) VALUES
('prodetailing', 'fundador', '2021', '2023', 'creacion y gestion de emprendimiento de detailing automotriz. marketing digital y atención a clientes.'),
('instituto tecnico renault', 'practicas', '2024', NULL, 'practicas y proyectos en programacion y datos.');

INSERT INTO skills (name, level) VALUES
('python', 5),
('sql', 4),
('flask', 4),
('javascript', 3);
