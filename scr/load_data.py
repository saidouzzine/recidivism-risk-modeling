# Connexion SQL + extraction
# Chargement des données depuis une base SQL

import pandas as pd
import psycopg2
from config import DB_CONFIG

def load_recidive_table():
    """
    Charge la table 'recidive' depuis la base SQL.
    Retourne un DataFrame pandas.
    """
    conn = psycopg2.connect(**DB_CONFIG)
    query = "SELECT * FROM recidive;"
    df = pd.read_sql(query, conn)
    conn.close()
    return df
