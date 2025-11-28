-- schema.sql

CREATE DATABASE IF NOT EXISTS b1pqkad90ffurwescyys
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;

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
  github VARCHAR(255),
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

-- tabla education 
CREATE TABLE IF NOT EXISTS education (
  id INT AUTO_INCREMENT PRIMARY KEY,
  institution VARCHAR(200),
  degree VARCHAR(200),
  start_year VARCHAR(10),
  end_year VARCHAR(10),
  description TEXT
);

-- tabla skills
CREATE TABLE IF NOT EXISTS skills (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100),
  level INT DEFAULT 0
);

-- tabla projects 
CREATE TABLE IF NOT EXISTS projects (
  id INT AUTO_INCREMENT PRIMARY KEY,
  title VARCHAR(255),
  description TEXT,
  link VARCHAR(255),
  image VARCHAR(255)
);

-- seed de datos personales
INSERT INTO personal (id, name, title, phone, email, about, linkedin, github)
VALUES (
  1,
  'Mateo Ulla',
  'Estudiante - Programación, AI y Finanzas',
  '(351) 810-4498',
  'mateoullaa@gmail.com',
  'Estudiante de Programación con
orientación en Inteligencia Artificial y
Finanzas, apasionado por los negocios y
los emprendimientos.
Experiencia como fundador de un servicio
de detailing automotriz.
Orientado al crecimiento en el ambito
tecnológico y financiero, aplicando
habilidades en programación, análisis y
liderazgo.
',
  'https://www.linkedin.com/in/mateoulla/',
  'https://github.com/mateo-ulla'
);

-- seed experience 
INSERT INTO experience (company, role, start_date, end_date, description) VALUES
('Título', 'Subtítulo', '0000', '0000', 'Descripción'),
('Título', 'Subtítulo', '0000', '0000', 'Descripción');

-- seed de educacion
INSERT INTO education (institution, degree, start_year, end_year, description) VALUES
('Instituto Técnico Renault', 'Técnico en Programación', '2019', '2025', 'Formacion técnica con orientación en programación, bases de datos y sistemas.'),
('IICANA', 'Certificación de Inglés ECCE - Nivel B2', '2016', '2025', 'Certificación internacional de inglés intermedio alto (nivel B2).');

-- seed skills
INSERT INTO skills (name, level) VALUES
('Python', 90),
('Flask', 85),
('MySQL', 85),
('HTML/CSS', 80),
('JavaScript', 80),
('Español (Nativo)', 100),
('Inglés (Nivel B2 - ECCE)', 90),
('Trabajo en equipo', 90),
('Liderazgo', 95),
('Resolución de problemas', 100),
('Pensamiento crítico', 90),
('Comunicación', 90);

-- seed projects
INSERT INTO projects (title, description, github, image) VALUES
('Portfolio Web (Proyecto Integrador)',
  'Aplicación web full stack con Flask, MySQL y Bootstrap. Incluye login, panel de edición y diseño adaptable.',
  'https://github.com/mateo-ulla/Proyecto-Integrador-Portfolio',
  'portfolio_web.jpg'
),

('Detailhaus - Fundador',
  'Emprendimiento personal de detailing automotriz. Gestión de clientes y marketing digital (SEO y SEM). Uso de WhatsApp Business, Facebook Ads y redes sociales.',
  'https://www.instagram.com/detailhaus.cba/',
  'detailhaus.jpg'
),

('Taller Mecánico (con Django)',
  'Proyecto desarrollado para un taller mecánico. Basado en el sistema previo hecho con Flet, este proyecto traslada la lógica a un sitio web con HTML, CSS, Bootstrap y templates de Django.',
  'https://github.com/mateo-ulla/Taller-Mecanico-Django-V2',
  'taller_mecanico.jpg'
),

('Aula Virtual (con Flask)',
  'Aplicación web para gestión educativa: cursos, materiales, evaluaciones y usuarios. Desarrollada con Flask, MySQL y Bootstrap.',
  'https://github.com/mateo-ulla/Aula-Virtual',
  'aula_virtual.jpg'
),

('Simulador de Cobro (API de Mercado Pago)',
  'App en Flask para simular compras y cobros con tarjeta simulada y Mercado Pago (Checkout Pro).',
  'https://github.com/mateo-ulla/App-de-cobro',
  'app_cobro.jpg'
),

('Copa Renault App',
  'Aplicación web para gestión de la Copa Renault: equipos, partidos, reservas de cantina y sponsors. Hecha con Flask y Bootstrap.',
  'https://github.com/mateo-ulla/App-Copa-Renault',
  'copa_renault.jpg'
);
