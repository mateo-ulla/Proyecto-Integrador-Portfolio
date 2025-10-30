# seed_admin.py

from werkzeug.security import generate_password_hash
import pymysql
from config import Config

def create_admin(username, password):
    hashed = generate_password_hash(password)
    conn = pymysql.connect(host=Config.DB_HOST, user=Config.DB_USER, password=Config.DB_PASSWORD, database=Config.DB_NAME, port=Config.DB_PORT)
    try:
        with conn.cursor() as cur:
            cur.execute("insert into admin (username, password) values (%s, %s)", (username, hashed))
        conn.commit()
        print("admin creado")
    except Exception as e:
        print("error:", e)
    finally:
        conn.close()

if __name__ == '__main__':
    create_admin('admin', '123456')
