import pandas as pd


# ==========================================================
# COMMON HELPERS

#standardize_columns
#remove_duplicates
#strip_strings
#uppercase_columns

# ==========================================================

def standardize_columns(df:pd.DataFrame) -> pd.DataFrame:
    """
    Standardize column names.
    """
    df.columns = (df.columns
                .str.strip()
                .str.lower()
                .str.replace(" ", "_"))
    
    return df

def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    
    return df.drop_duplicates()

def strip_strings(df: pd.DataFrame) -> pd.DataFrame:

    string_cols = df.select_dtypes(include=object).columns

    for col in string_cols:
        df[col] = df[col].str.strip()

    return df

def uppercase_columns(df: pd.DataFrame, columns: list) -> pd.DataFrame:

    for col in columns:
        if col in df.columns:
            df[col] = df[col].str.upper()

    return df

