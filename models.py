# models.py

# se muestran los 4 pilares de la poo con comentarios:
# - encapsulacion
# - abstraccion
# - herencia
# - polimorfismo

from db import get_connection

# encapsulacion: atributos privados y metodos get/set simples
class BaseModel:
    def __init__(self, table):
        self._table = table  # encapsulado: uso interno para nombre de tabla

    # abstraccion: metodo generico para obtener todos los registros
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

# herencia: modelos de datos heredan de BaseModel
class PersonalModel(BaseModel):
    def __init__(self):
        super().__init__('personal')

    def update(self, data):
        conn = get_connection()
        with conn.cursor() as cur:
            cur.execute("""
                update personal set name=%s, title=%s, phone=%s, email=%s, about=%s, linkedin=%s, github=%s
                where id=1
            """, (data['name'], data['title'], data['phone'], data['email'], data['about'], data['linkedin'], data['github']))
            return True

class ExperienceModel(BaseModel):
    def __init__(self):
        super().__init__('experience')

    def create(self, data):
        conn = get_connection()
        with conn.cursor() as cur:
            cur.execute("insert into experience (company, role, start_date, end_date, description) values (%s,%s,%s,%s,%s)",
                        (data['company'], data['role'], data['start_date'], data.get('end_date'), data['description']))
            return cur.lastrowid

class SkillsModel(BaseModel):
    def __init__(self):
        super().__init__('skills')

    # polimorfismo: sobrescribimos all() si queremos orden distinto
    def all(self):
        conn = get_connection()
        with conn.cursor() as cur:
            cur.execute("select * from skills order by level desc")
            return cur.fetchall()
        
class EducationModel(BaseModel):
    def __init__(self):
        super().__init__('education')
