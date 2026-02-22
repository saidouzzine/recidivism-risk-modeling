# Analyse descriptive et visualisation

import seaborn as sns
import matplotlib.pyplot as plt

def plot_correlation(df):
    """
    Affiche la matrice de corrélation des variables numériques.
    """
    num_cols = ["alcool", "drogue", "preuve", "regle", "durprison",
                "nivetud", "age_an", "durliberte"]

    corr = df[num_cols].corr()

    plt.figure(figsize=(10, 8))
    sns.heatmap(corr, annot=True, cmap="coolwarm")
    plt.title("Matrice de corrélation des caractéristiques")
    plt.show()
