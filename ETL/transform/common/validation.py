import pandas as pd


#validate_required_columns,
#validate_unique_key,
#validate_positive,
#validate_notnull,
#validate_allowed_values,
#validate_date_order

def validate_required_columns(df:pd.DataFrame, required_columns: list) -> None:

    missing = [col for col in required_columns if col not in df.columns]

    if missing:
        raise ValueError (f"missing columns: {missing}")
    

def validate_unique_key(df:pd.DataFrame, key: str) -> None:

    if key not in df.columns:
        return
    
    duplicates = df[df[key].duplicated()]

    if not duplicates.empty:
        raise ValueError (f"{key} found duplicate")
    

def validate_positive(df:pd.DataFrame, columns: list) -> None:

    for col in columns:
        if col not in df.columns:
            continue
        
        if (df[col] < 0).any():
            raise ValueError(f"negative values found in {col}")
        
def validate_notnull(df: pd.DataFrame, columns: list) -> None:

    for col in columns:
        if col not in df.columns:
            continue

        if df[col].isnull().any():
            raise ValueError(f"found null in {col}")

def validate_allowed_values(df:pd.DataFrame, column: str, allowed_values: list) -> None:

    if column not in df.columns:
        return
    
    invalid = df[~df[column].isin(allowed_values)]

    if not invalid.empty:
        raise ValueError(f"invalid values found in {column}")


def validate_date_order(df:pd.DataFrame, start_date:str, end_date: str) -> None:

    if start_date not in df.columns:
        return
    
    if end_date not in df.columns:
        return
    
    invalid = df[df[end_date] < df[start_date]]

    if not invalid.empty:
        raise ValueError(f"{end_date} cannot be earlier than {start_date}")
