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

-- tabla experience (por ahora vacia, lista para futuras experiencias)
CREATE TABLE IF NOT EXISTS experience (
  id INT AUTO_INCREMENT PRIMARY KEY,
  company VARCHAR(200),
  role VARCHAR(200),
  start_date VARCHAR(50),
  end_date VARCHAR(50),
  description TEXT
);

-- tabla education 
CREATE TABLE IF NOT EXISTS education (
  id INT AUTO_INCREMENT PRIMARY KEY,
  institution VARCHAR(200),
  degree VARCHAR(200),
  start_year VARCHAR(10),
  end_year VARCHAR(10),
  description TEXT
);

-- tabla skills (niveles expresados en porcentajes)
CREATE TABLE IF NOT EXISTS skills (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100),
  level INT DEFAULT 0
);

-- seed inicial: datos personales
INSERT INTO personal (id, name, title, phone, email, about, linkedin, github)
VALUES (
  1,
  'Mateo Ulla',
  'Estudiante - Programacion y AI',
  '(351) 810-4498',
  'mateoullaa@gmail.com',
  'Estudiante de programacion con orientacion en inteligencia artificial y finanzas. Fundador de emprendimiento de detailing. En busca de oportunidades y crecimiento profesional.',
  'https://ar.linkedin.com/in/mateo-ulla-08857636b',
  'https://github.com/mateo-ulla'
);

-- seed de educacion
INSERT INTO education (institution, degree, start_year, end_year, description) VALUES
('Instituto Tecnico Renault', 'Tecnico en Programacion', '2019', '2025', 'Formacion tecnica con orientacion en programacion, bases de datos y sistemas.'),
('IICANA', 'Certificacion de Ingles ECCE - Nivel B2', '2016', '2025', 'Certificacion internacional de ingles intermedio alto (nivel B2).');

-- no insertamos experiencia (queda vacia para completar en el futuro)

-- seed de habilidades (hard & soft skills + idiomas)
INSERT INTO skills (name, level) VALUES
('Python', 90),
('Flask', 80),
('MySQL', 80),
('HTML/CSS', 75),
('JavaScript', 70),
('Ingles (Nivel B2 - ECCE)', 90),
('Espanol (Nativo)', 100),
('Trabajo en equipo', 90),
('Comunicacion', 95);
