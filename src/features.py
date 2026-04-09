import pandas as pd

def add_features(df):
    df = df.copy()

    # Safe split (handle missing / bad format)
    bp_split = df['Blood Pressure'].str.split('/', expand=True)

    df['BP_Systolic'] = pd.to_numeric(bp_split[0], errors='coerce')
    df['BP_Diastolic'] = pd.to_numeric(bp_split[1], errors='coerce')

    df.drop(columns=['Blood Pressure'], inplace=True, errors='ignore')

    return df