# Modèles économétriques : Probit + Multinomial Logit
# Estimation des modèles économétriques

import statsmodels.api as sm
import statsmodels.formula.api as smf

def probit_individuel(df):
    """
    Modèle Probit basé uniquement sur les caractéristiques individuelles.
    """
    formula = "statut ~ C(alcool) + C(drogue) + nivetud + age_an + C(origine)"
    model = smf.probit(formula, data=df).fit()
    return model

def probit_prison(df):
    """
    Modèle Probit basé uniquement sur les caractéristiques liées au séjour.
    """
    formula = "statut ~ preuve + regle + durprison + C(raison) + C(job)"
    model = smf.probit(formula, data=df).fit()
    return model

def probit_complet(df):
    """
    Modèle Probit complet : caractéristiques individuelles + prison.
    """
    formula = ("statut ~ C(alcool) + C(drogue) + nivetud + age_an + C(origine) "
               "+ preuve + regle + durprison + C(raison) + C(job)")
    model = smf.probit(formula, data=df).fit()
    return model

def multinomial_recidive(df):
    """
    Modèle Logit multinomial :
    - 0 = pas de récidive
    - 1 = récidive <= 12 mois
    - 2 = récidive > 12 mois
    """
    df = df.copy()
    df["classe"] = df["durliberte"].apply(
        lambda x: 0 if x == 0 else (1 if x <= 12 else 2)
    )

    formula = "C(classe) ~ C(alcool) + C(drogue) + nivetud + age_an + C(origine) + preuve + regle + durprison + C(raison) + C(job)"
    model = smf.mnlogit(formula, data=df).fit()
    return model
