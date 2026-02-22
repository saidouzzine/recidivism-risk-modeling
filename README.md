# recidivism-risk-modeling
Analyse statistique et économétrique de la récidive à partir de données pénitentiaires. Modélisation en Python de la probabilité de récidive et de la durée de liberté (probit, modèles multinomiaux, effets marginaux), avec une approche reproductible orientée data science appliquée.

# 1. Modélisation du risque de récidive par économétrie des variables qualitatives

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Statsmodels](https://img.shields.io/badge/Statsmodels-Econometrics-green)
![SQL](https://img.shields.io/badge/Database-PostgreSQL-lightgrey)
![Status](https://img.shields.io/badge/Project-Active-success)

# 2. Description du projet

Ce projet analyse le risque de récidive d'anciens détenus à partir de données pénitentiaires.  
L'objectif est d'estimer la probabilité de récidive à l'aide de modèles économétriques (Probit, Logit multinomial) et d'étudier l'effet marginal des facteurs individuels et carcéraux.  
Les données proviennent d'une base SQL et sont traitées en Python.

# 3. Structure du dépôt

```
recidive-risk-model/
│
├── src/
│   ├── config.py
│   ├── load_data.py
│   ├── preprocessing.py
│   ├── eda.py
│   ├── models.py
│   ├── marginal_effects.py
│   └── main.py
│
├── requirements.txt
└── install_packages.sh
```

# 4. Fonctionnalités principales

## 4.1 Chargement des données
Extraction automatique depuis une base SQL contenant la table `recidive`.

## 4.2 Préparation des données
Nettoyage, typage, création de la variable latente de récidive.

## 4.3 Analyse descriptive
Matrice de corrélation et statistiques comparatives.

## 4.4 Modélisation économétrique
- Modèle Probit (individuel, prison, complet)
- Modèle Logit multinomial (durée avant récidive)
- Effets marginaux

## 4.5 Reproductibilité
Code modulaire, structuré, facilement intégrable dans un pipeline de data science.

# 5. Exécution

```
bash install_packages.sh
python src/main.py
```

# 6. Auteur

Projet réalisé par Said Ouzzine, Data Scientist|Econométrie|modélisation statistique

Profil LinkedIn :https://www.linkedin.com/in/said-ouzzine/


