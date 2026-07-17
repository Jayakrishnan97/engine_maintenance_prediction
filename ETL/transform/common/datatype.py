import pandas as pd


#to_datetime
#to_numeric


def to_datetime(df: pd.DataFrame, columns: list) -> pd.DataFrame:

    for col in columns:
        if col in df.columns:
            df[col] = pd.to_datetime(
                df[col],
                errors= "coerce"
            )
    return df

def to_numeric(df:pd.DataFrame, columns: list) -> pd.DataFrame:

    for col in columns:
        if col in df.columns:
            df[col] = pd.to_numeric(
                df[col],
                errors="coerce"
            )
    
    return df

def to_string(df:pd.DataFrame, columns: list) -> pd.DataFrame:

    for col in columns:
        if col in df.columns:
            df[col] = df[col].astype("string")

    return df