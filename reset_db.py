import os
import pymysql

# Variables de entorno de Clever Cloud
DB_HOST = os.environ.get("MYSQL_ADDON_HOST", "b1pqkad90ffurwescyys-mysql.services.clever-cloud.com")
DB_USER = os.environ.get("MYSQL_ADDON_USER", "ulrdoatjddazulgr")
DB_PASSWORD = os.environ.get("MYSQL_ADDON_PASSWORD", "U9eN3UvTZ6vOXraLE02h")
DB_NAME = os.environ.get("MYSQL_ADDON_DB", "b1pqkad90ffurwescyys")
DB_PORT = int(os.environ.get("MYSQL_ADDON_PORT", 3306))

SCHEMA_FILE = "schema.sql"


def drop_all_tables(cursor):
    """Dropear TODAS las tablas de la base de datos."""
    cursor.execute("SET FOREIGN_KEY_CHECKS = 0;")
    cursor.execute("SHOW TABLES;")
    tables = cursor.fetchall()

    for t in tables:
        table_name = list(t.values())[0]
        print(f"Dropping table: {table_name}")
        cursor.execute(f"DROP TABLE IF EXISTS `{table_name}`;")

    cursor.execute("SET FOREIGN_KEY_CHECKS = 1;")


def execute_sql_script(cursor, sql):
    """Ejecuta múltiples sentencias SQL desde schema.sql"""
    commands = sql.split(";")

    for command in commands:
        command = command.strip()
        if command:
            cursor.execute(command)


def main():
    print("Conectando a MySQL en Clever Cloud...")
    conn = pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        db=DB_NAME,
        port=DB_PORT,
        autocommit=True,
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor
    )

    cursor = conn.cursor()

    print("Dropping all tables...")
    drop_all_tables(cursor)

    print("Loading schema.sql...")
    with open(SCHEMA_FILE, "r", encoding="utf-8") as f:
        schema_sql = f.read()

    print("Executing schema.sql...")
    execute_sql_script(cursor, schema_sql)

    print("\n✅ Base de datos reseteada correctamente.")
    print("✔ Todas las tablas fueron eliminadas")
    print("✔ Todas las tablas fueron recreadas desde schema.sql")
    print("✔ Seed de datos insertado")
    print("\nListo.")


if __name__ == "__main__":
    main()
