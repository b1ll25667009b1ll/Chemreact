import pandas as pd
import os

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")

def load_uspto():
    path = os.path.join(DATA_DIR, "uspto.parquet")
    try:
        df = pd.read_parquet(path)
        return df
    except Exception as e:
        return None

def load_buchwald():
    path = os.path.join(DATA_DIR, "buchwald.parquet")
    try:
        df = pd.read_parquet(path)
        return df
    except Exception as e:
        return None


def simple_lookup(reactants: list):
    """
    Very simple matching engine (we upgrade later to ML)
    """
    uspto = load_uspto()

    if uspto is None:
        return None

    # Expect dataset columns like:
    # reactants, products
    for _, row in uspto.iterrows():
        if all(r.lower() in str(row["reactants"]).lower() for r in reactants):
            return {
                "match": True,
                "reactants": row["reactants"],
                "products": row["products"]
            }

    return None
