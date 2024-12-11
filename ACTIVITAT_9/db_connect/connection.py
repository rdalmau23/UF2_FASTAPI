import psycopg2
from psycopg2.extras import RealDictCursor

def get_db_connection():
    return psycopg2.connect(
        host="localhost",  # O l'adreça del teu servidor
        database="nom_de_la_teva_base_de_dades",
        user="nom_usuari",
        password="la_teva_contrasenya",
        cursor_factory=RealDictCursor
    )
