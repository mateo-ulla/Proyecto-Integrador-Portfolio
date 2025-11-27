# seed_admin_production.py
# crea o actualiza el usuario admin en la base de datos (Clever Cloud)
# SIN variables de entorno, todo hardcodeado

import sys
import pymysql
from werkzeug.security import generate_password_hash

# -----------------------------
# DATOS DE CONEXIÓN CLEVER CLOUD (HARDCODEADOS)
# -----------------------------
DB_HOST = "b1pqkad90ffurwescyys-mysql.services.clever-cloud.com"
DB_USER = "ulrdoatjddazulgr"
DB_PASSWORD = "U9eN3UvTZ6vOXraLE02h"
DB_NAME = "b1pqkad90ffurwescyys"
DB_PORT = 3306
# -----------------------------


def get_connection():
    return pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        db=DB_NAME,
        port=DB_PORT,
        cursorclass=pymysql.cursors.DictCursor
    )


def upsert_admin(username, password_plain):
    password_hash = generate_password_hash(password_plain)
    conn = None

    try:
        conn = get_connection()
        with conn.cursor() as cursor:

            # verificar si el usuario existe
            cursor.execute("SELECT id FROM admin WHERE username=%s", (username,))
            existing = cursor.fetchone()

            if existing:
                print(f"usuario '{username}' existe -> actualizando contraseña…")
                cursor.execute(
                    "UPDATE admin SET password=%s WHERE username=%s",
                    (password_hash, username)
                )
            else:
                print(f"usuario '{username}' no existe -> creando usuario…")
                cursor.execute(
                    "INSERT INTO admin (username, password) VALUES (%s, %s)",
                    (username, password_hash)
                )

        conn.commit()
        print("✔ admin creado/actualizado correctamente.")
    
    except Exception as e:
        print("error: no se pudo crear/actualizar admin.")
        print("detalles:", e)
        sys.exit(1)

    finally:
        if conn:
            try:
                conn.close()
            except:
                pass


def main():
    print("script: crear/actualizar admin en Clever Cloud")

    username = input("usuario (default: admin): ").strip() or "admin"
    password = input("ingresa la contraseña del admin: ").strip()

    if not password:
        print("error: la contraseña no puede ser vacía.")
        sys.exit(1)

    upsert_admin(username, password)


if __name__ == "__main__":
    
    main()
