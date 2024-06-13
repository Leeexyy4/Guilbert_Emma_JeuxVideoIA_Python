import psycopg2

conn = psycopg2.connect(
        database="SAE_jv",
        host="localhost",
        user="postgres",
        password="Paulbrp5",
        port="5433"
    )

def nbCases():
    cur = conn.cursor()
    cur.execute("SELECT cases_decouvertes FROM statistiques WHERE joueur_id = 1")
    nombre_cases_decouvertes = cur.fetchone()[0]
    cur.close()
    return nombre_cases_decouvertes

def envoyer_donnees_bdd(partie_id, joueur_id, cases_decouvertes, manches_effectuees, morts, cles_recuperees, points_vie, boss_vaincus, pv_moyen):
        cur = conn.cursor()
        cur.execute("INSERT INTO statistiques (partie_id, joueur_id, cases_decouvertes, manches_effectuees, morts, cles_recuperees, points_vie, boss_vaincus, pv_moyen) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (partie_id, joueur_id, cases_decouvertes, manches_effectuees, morts, cles_recuperees, points_vie, boss_vaincus, pv_moyen))
        conn.commit()
        cur.close()
        print("Données envoyées à la base de données avec succès")

def creer_partie(gagnant):
        cur = conn.cursor()
        cur.execute("INSERT INTO parties (gagnant) VALUES (%s) RETURNING id", (gagnant,))
        partie_id = cur.fetchone()[0]
        conn.commit()
        cur.close()
        return partie_id

def recuperer_donnees_bdd(partie_id):
        cur = conn.cursor()
        cur.execute("SELECT * FROM statistiques WHERE partie_id = %s", (partie_id,))
        donnees = cur.fetchall()
        cur.close()
        return donnees

