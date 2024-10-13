import psycopg2


# Stablish DB connection
def create_connection():
    connection = psycopg2.connect(
        host='10.107.164.120',
        user='safi',
        password='safi',
        database='project3'  # ggf. anpassen
    )
    return connection

# Add record to DB
def add_contact(name, phone, email, adresse):
    conn = ""
    try:
       conn = create_connection()
    except psycopg2.Error as err:
       print(f"Fehler: {err}") 
    cursor = conn.cursor() 
    sql = "INSERT INTO contacts (name, phone, email, adresse) VALUES (%s, %s, %s, %s)" 
    values = (name, phone, email, adresse) 
    cursor.execute(sql, values) 
    conn.commit() 
    cursor.close() 
    conn.close() 

# Test add
add_contact("Rahimdad Faisal Safi", "+491633456734", "h.h@gmail.com", "Berlin")

# try:
#     conn = create_connection()
#     print("Verbindung zur PostgreSQL-Datenbank erfolgreich")
#     conn.close()
# except psycopg2.Error as err:
#     print(f"Fehler: {err}")