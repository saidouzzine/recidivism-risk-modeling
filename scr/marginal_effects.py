# Calcul des effets marginaux

def compute_marginal_effects(model):
    """
    Calcule les effets marginaux moyens du modèle Probit.
    """
    return model.get_margeff(at="mean").summary()
