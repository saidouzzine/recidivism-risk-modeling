# Script principal du projet

from load_data import load_recidive_table
from preprocessing import preprocess
from eda import plot_correlation
from models import (
    probit_individuel,
    probit_prison,
    probit_complet,
    multinomial_recidive
)
from marginal_effects import compute_marginal_effects

def main():
    df = load_recidive_table()
    df = preprocess(df)

    plot_correlation(df)

    model_ind = probit_individuel(df)
    print(model_ind.summary())

    model_prison = probit_prison(df)
    print(model_prison.summary())

    model_full = probit_complet(df)
    print(model_full.summary())

    print(compute_marginal_effects(model_full))

    model_multi = multinomial_recidive(df)
    print(model_multi.summary())

if __name__ == "__main__":
    main()
