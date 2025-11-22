# seed_admin_production.py
# este script crea o actualiza el usuario admin en la base de datos de clever cloud
# usa el hash de werkzeug, igual que el login de la app

import pymysql
from werkzeug.security import generate_password_hash
from config import Config

def main():
    print("generando hash de contraseña...")
    password = input("ingresa la contraseña del admin: ")
    password_hash = generate_password_hash(password)
    print("\nhash generado correctamente.\n")

    print("conectando a la base de datos de clever cloud...")

    try:
        conn = pymysql.connect(
            host=Config.DB_HOST,
            user=Config.DB_USER,
            password=Config.DB_PASSWORD,
            db=Config.DB_NAME,
            port=Config.DB_PORT,
            cursorclass=pymysql.cursors.DictCursor
        )

        with conn.cursor() as cursor:
            # si existe -> actualizar
            cursor.execute("SELECT * FROM admin WHERE username='admin'")
            existing = cursor.fetchone()

            if existing:
                print("usuario admin ya existe. actualizando contraseña...")
                cursor.execute(
                    "UPDATE admin SET password=%s WHERE username='admin'",
                    (password_hash,)
                )
            else:
                print("creando usuario admin...")
                cursor.execute(
                    "INSERT INTO admin (username, password) VALUES (%s, %s)",
                    ('admin', password_hash)
                )

            conn.commit()
            print("\n✔ admin creado/actualizado exitosamente")
    
    except Exception as e:
        print("\n error al conectar o modificar la base de datos:")
        print(e)
    
    finally:
        try:
            conn.close()
        except:
            pass


if __name__ == "__main__":
    main()
