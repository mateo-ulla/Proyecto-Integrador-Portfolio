# models.py

# se muestran los 4 pilares de la poo con comentarios:
# - encapsulacion
# - abstraccion
# - herencia
# - polimorfismo

from db import get_connection

# encapsulacion: la tabla es un atributo privado para uso interno
class BaseModel:
    def __init__(self, table):
        self._table = table  # atributo encapsulado

    # abstraccion: metodos genericos que ocultan la complejidad sql
    def all(self):
        conn = get_connection()
        with conn.cursor() as cur:
            cur.execute(f"select * from {self._table} order by id desc")
            return cur.fetchall()

    def find(self, id):
        conn = get_connection()
        with conn.cursor() as cur:
            cur.execute(f"select * from {self._table} where id=%s", (id,))
            return cur.fetchone()

    def delete(self, id):
        conn = get_connection()
        with conn.cursor() as cur:
            cur.execute(f"delete from {self._table} where id=%s", (id,))
            conn.commit()

# herencia: todos los modelos heredan la logica base
class PersonalModel(BaseModel):
    def __init__(self):
        super().__init__('personal')

    def update(self, data):
        conn = get_connection()
        with conn.cursor() as cur:
            cur.execute("""
                update personal 
                set name=%s, title=%s, phone=%s, email=%s, about=%s, linkedin=%s, github=%s
                where id=1
            """, (
                data['name'],
                data['title'],
                data['phone'],
                data['email'],
                data['about'],
                data['linkedin'],
                data['github']
            ))
            conn.commit()

class ExperienceModel(BaseModel):
    def __init__(self):
        super().__init__('experience')

    def create(self, data):
        conn = get_connection()
        with conn.cursor() as cur:
            cur.execute("""
                insert into experience (company, role, start_date, end_date, description) 
                values (%s,%s,%s,%s,%s)
            """, (
                data['company'],
                data['role'],
                data['start_date'],
                data.get('end_date'),
                data['description']
            ))
            conn.commit()
            return cur.lastrowid

class SkillsModel(BaseModel):
    def __init__(self):
        super().__init__('skills')

    # polimorfismo: se redefine all() para mostrar segun nivel
    def all(self):
        conn = get_connection()
        with conn.cursor() as cur:
            cur.execute("select * from skills order by level desc")
            return cur.fetchall()

class EducationModel(BaseModel):
    def __init__(self):
        super().__init__('education')

# herencia + polimorfismo aplicados en ProjectsModel
class ProjectsModel(BaseModel):
    def __init__(self):
        super().__init__('projects')

    def create(self, data):
        conn = get_connection()
        with conn.cursor() as cur:
            cur.execute("""
                insert into projects (title, description, github, image)
                values (%s, %s, %s, %s)
            """, (
                data['title'],
                data['description'],
                data['github'],
                data['image']
            ))
            conn.commit()

    def update(self, id, data):
        conn = get_connection()
        with conn.cursor() as cur:
            cur.execute("""
                update projects 
                set title=%s, description=%s, github=%s, image=%s
                where id=%s
            """, (
                data['title'],
                data['description'],
                data['github'],
                data['image'],
                id
            ))
            conn.commit()
