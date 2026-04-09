import pandas as pd

def clean_data(df):
    df = df.copy()

    # Drop irrelevant
    df = df.drop(columns=['Patient ID', 'Income', 'Hemisphere', 'Continent', 'Country' ], errors='ignore')

    # Target encoding
    df["Sex"] = df["Sex"].map({"Male": 0, "Female": 1})

    return df