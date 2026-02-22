# Nettoyage + création de la variable latente "statut"
# Préparation des données pour l'analyse économétrique

import pandas as pd

def preprocess(df):
    """
    Prépare les données :
    - Convertit les variables catégorielles en catégories
    - Crée la variable binaire 'statut' (1 = récidive, 0 = non récidive)
    """
    df = df.copy()

    categorical_cols = ["alcool", "drogue", "origine", "raison", "job"]
    for col in categorical_cols:
        df[col] = df[col].astype("category")

    df["statut"] = (df["durliberte"] != 0).astype(int)

    return df
