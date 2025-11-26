-- schema.sql

USE b1pqkad90ffurwescyys;

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

-- tabla experience (por ahora vacia)
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

-- seed de datos personales
INSERT INTO personal (id, name, title, phone, email, about, linkedin, github)
VALUES (
  1,
  'Mateo Ulla',
  'Estudiante - Programacion y AI',
  '(351) 810-4498',
  'mateoullaa@gmail.com',
  'Estudiante de Programacion con
orientacion en Inteligencia Artificial y
Finanzas, apasionado por los negocios y
los emprendimientos.
Experiencia como fundador de un servicio
de detailing automotriz.
Orientado al crecimiento en el ámbito
tecnológico y financiero, aplicando
habilidades en programación, análisis y
liderazgo.
',
  'https://www.linkedin.com/in/mateoulla/',
  'https://github.com/mateo-ulla'
);

-- seed de experience (vacío por ahora)
INSERT INTO experience (company, role, start_date, end_date, description) VALUES
('Titulo', 'Subtitulo', '0000', '0000', 'Descripcion'),
('Titulo', 'Subtitulo', '0000', '0000', 'Descripcion');

-- seed de educacion
INSERT INTO education (institution, degree, start_year, end_year, description) VALUES
('Instituto Tecnico Renault', 'Tecnico en Programacion', '2019', '2025', 'Formacion tecnica con orientacion en programacion, bases de datos y sistemas.'),
('IICANA', 'Certificacion de Ingles ECCE - Nivel B2', '2016', '2025', 'Certificacion internacional de ingles intermedio alto (nivel B2).');

-- seed de habilidades (hard & soft skills + idiomas)
INSERT INTO skills (name, level) VALUES
('Python', 90),
('Flask', 85),
('MySQL', 85),
('HTML/CSS', 80),
('JavaScript', 80),
('Ingles (Nivel B2 - ECCE)', 90),
('Espanol (Nativo)', 100),
('Trabajo en equipo', 90),
('Liderazgo', 95),
('Resolucion de problemas', 100),
('Pensamiento critico', 90),
('Comunicacion', 90);
