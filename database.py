import psycopg2

conn = psycopg2.connect(
        database="SAE_jv",
        host="localhost",
        user="postgres",
        password="Paulbrp5",
        port="5433"
    )
cur = conn.cursor()

def nbCases():
    cur.execute("SELECT cases_decouvertes FROM statistiques WHERE joueur_id = 1")
    nombre_cases_decouvertes = cur.fetchone()[0]
    return nombre_cases_decouvertes

def close_connection():
    cur.close()
    conn.close()