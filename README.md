# Portfolio Web - Mateo Ulla

**Proyecto Final - Laboratorio de Programación (Instituto Técnico Renault)**  
Aplicación web Full Stack desarrollada con **Flask**, **MySQL**, **PyMySQL**, **Flask-WTF** y **Bootstrap**.  
El proyecto tiene como objetivo crear un **Portfolio Profesional**, editable por un usuario administrador y desplegado en línea.

---

## Descripción General

Este proyecto es un **Portfolio Web Personal** que muestra información sobre:
- Datos personales  
- Estudios cursados  
- Experiencia laboral  
- Habilidades técnicas  
- Enlaces a GitHub, LinkedIn y descarga de CV  

Cuenta con un **panel de administración protegido por login**, donde el usuario (rol: *admin*) puede modificar los datos en tiempo real.

---

## Tecnologías utilizadas

| Categoría | Tecnologías |
|------------|-------------|
| **Frontend** | HTML5, CSS, Jinja2, Bootstrap |
| **Backend** | Python 3, Flask, Flask-WTF, Werkzeug |
| **Base de datos** | MySQL (conector: PyMySQL) |
| **Seguridad** | Flask-WTF (CSRF Protection), Hash de contraseña |
| **Diseño** | Paleta oscura y minimalista, animaciones CSS sutiles |
| **Deploy** | Base de datos en Clever Cloud, app Flask en Render |
| **POO** | Implementada en `models.py` con los 4 pilares comentados en el código |

---

## Estructura del proyecto

```
portfolio_flask/
├── app.py
├── config.py
├── db.py
├── models.py
├── forms.py
├── seed_admin.py
├── schema.sql
├── requirements.txt
├── run.sh
├── static/
│   ├── css/
│   │   ├── bootstrap.min.css
│   │   └── custom.css
│   ├── js/
│   │   └── main.js
│   └── uploads/
│       ├── profile.jpg
│       └── CV MATEO ULLA.pdf
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── about.html
│   ├── proyect.html
│   ├── login.html
│   ├── admin_edit.html
│   └── partials/
│       ├── nav.html
│       └── footer.html
└── README.md
```

---

## Instalación y ejecución en entorno local

### Crear entorno virtual
```bash
python -m venv venv
source venv/bin/activate    # Linux / macOS
venv\Scripts\activate       # Windows
```

### Instalar dependencias
```bash
pip install -r requirements.txt
```

### Crear base de datos MySQL local
Ejecutar el script `schema.sql`:
```bash
mysql -u root -p < schema.sql
```

### Crear usuario administrador
Ejecutar:
```bash
python seed_admin.py
```
🔹 Por defecto se crea un usuario:
```
usuario: admin
contraseña: 123456
```
Podés modificarlo en el archivo `seed_admin.py`.

### Ejecutar la aplicación
```bash
python app.py
```

Abrir en el navegador:  
👉 http://127.0.0.1:5000  

---

## Acceso al panel de administración
- Ingresar a `/login`
- Autenticarse con las credenciales del usuario admin
- Acceder a `/admin` para editar la información del portfolio

---

## Programación Orientada a Objetos (POO)

La aplicación utiliza los **4 pilares de la POO**, claramente comentados en el código dentro de `models.py`:
1. **Encapsulación:** atributos privados (`_table`)
2. **Abstracción:** métodos genéricos como `BaseModel.all()`
3. **Herencia:** `PersonalModel`, `ExperienceModel` heredan de `BaseModel`
4. **Polimorfismo:** sobrescritura del método `all()` en `SkillsModel`

---

## Diseño y Responsividad

- Implementación con **Bootstrap 5**, adaptable a **mobile, tablet y escritorio**.
- Paleta de colores: negro, gris oscuro, beige.
- Animaciones suaves:
  - Hover en foto de perfil (`.profile-img`)
  - Transición en badges de habilidades (`.skill-badge`)

---

## Secciones principales

| Página | Descripción |
|---------|--------------|
| `/` | Página principal (perfil, experiencias, habilidades) |
| `/about` | Detalles personales y estudios |
| `/proyect` | Proyectos y trabajos |
| `/login` | Acceso de administrador |
| `/admin` | Panel de edición del portfolio |
| `/download/cv` | Descarga directa del CV en PDF |

---

## Despliegue en Clever Cloud + Render

### A) Base de datos en Clever Cloud
1. Crear cuenta en [Clever Cloud](https://www.clever-cloud.com/).
2. Crear un nuevo *Add-on* de tipo **MySQL**.
3. Copiar las credenciales (host, user, password, db, port).
4. Importar el archivo `schema.sql`:
   ```bash
   mysql -h <host> -P <port> -u <user> -p <database> < schema.sql
   ```
5. Ejecutar `seed_admin.py` con las variables configuradas para crear el admin.

---

### B) Desplegar la app Flask en Render
1. Crear cuenta en [Render.com](https://render.com/).
2. Conectar el repositorio de GitHub con el proyecto.
3. Configurar variables de entorno:
   ```
   SECRET_KEY=mi_clave_secreta
   DB_HOST=xxxx
   DB_USER=xxxx
   DB_PASSWORD=xxxx
   DB_NAME=xxxx
   DB_PORT=3306
   ```
4. Configurar comandos:
   - **Build Command:** `pip install -r requirements.txt`
5. Deploy y listo 

---

## Resetear la base de datos (opcional)

Si modificaste los datos del seed y querés recargarlos:
```bash
mysql -u root -p -e "DROP DATABASE IF EXISTS portfolio_db; CREATE DATABASE portfolio_db;"
mysql -u root -p portfolio_db < schema.sql
python seed_admin.py
```

---

## Enlaces

- **LinkedIn:** [Mateo Ulla](https://ar.linkedin.com/in/mateo-ulla-08857636b)
- **GitHub:** [mateo-ulla](https://github.com/mateo-ulla)
