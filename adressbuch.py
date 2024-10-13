import psycopg2

def create_connection():
    connection = psycopg2.connect(
        host='10.107.164.120',
        user='safi',
        password='safi',
        database='project3'  # ggf. anpassen
    )
    return connection

try:
    conn = create_connection()
    print("Verbindung zur PostgreSQL-Datenbank erfolgreich")
    conn.close()
except psycopg2.Error as err:
    print(f"Fehler: {err}")