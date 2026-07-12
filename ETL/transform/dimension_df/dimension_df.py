import pandas as pd

from ETL.extract.extract import (
    dim_aircraft_df,
    dim_engine_df,
    dim_airport_df,
    dim_routes_df,
    dim_engine_component_df,
)


def clean_columns(df):
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )
    return df


def transform_aircraft(df):

    df = clean_columns(df.copy())

    df.drop_duplicates(inplace=True)

    df["aircraft_registration"] = (
        df["aircraft_registration"]
        .str.upper()
        .str.strip()
    )

    return df


def transform_engine(df):

    df = clean_columns(df.copy())

    df.drop_duplicates(inplace=True)

    df["engine_serial_number"] = (
        df["engine_serial_number"]
        .str.upper()
        .str.strip()
    )

    df["engine_manufacture_date"] = pd.to_datetime(
        df["engine_manufacture_date"],
        errors="coerce"
    )

    return df


def transform_airport(df):

    df = clean_columns(df.copy())

    df.drop_duplicates(inplace=True)

    df["airport_code"] = df["airport_code"].str.upper()

    return df


def transform_route(df):

    df = clean_columns(df.copy())

    df.drop_duplicates(inplace=True)

    return df


def transform_component(df):

    df = clean_columns(df.copy())

    df.drop_duplicates(inplace=True)

    df["life_unit"] = (
        df["life_unit"]
        .fillna("")
        .str.upper()
    )

    df["life_limit"] = pd.to_numeric(
        df["life_limit"],
        errors="coerce"
    )

    return df


# =====================================================

if __name__ == "__main__":

    dim_aircraft = transform_aircraft(dim_aircraft_df)

    dim_engine = transform_engine(dim_engine_df)

    dim_airport = transform_airport(dim_airport_df)

    dim_route = transform_route(dim_routes_df)

    dim_component = transform_component(dim_engine_component_df)

    print("Dimension Transformation Completed")