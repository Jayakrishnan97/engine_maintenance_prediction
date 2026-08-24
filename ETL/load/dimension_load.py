import pandas as pd

from ETL.load.connection import get_connection_sql

#=====================================================

from ETL.transform.dimension_df.dimension_df import dim_aircraft, dim_airport, dim_route, dim_component, dim_engine


def load_dimension(df:pd.DataFrame, table_Name: str) -> None:

    connection = get_connection_sql()

    try:

        df.to_sql(
            table_Name,
            connection,
            if_exists="replace",
            index=False
        )

        print(f"{table_Name} loaded successfully")

    finally:
        connection.dispose()


def load_all_dimensions(
    dim_aircraft,
    dim_engine,
    dim_airport,
    dim_route,
    dim_component
):
    
    df = dim_aircraft
    load_dimension(df, "dim_aircraft")

    df = dim_airport
    load_dimension(df, "dim_airport")

    df = dim_route
    load_dimension(df, "dim_route")

    df = dim_component
    load_dimension(df, "dim_component")

    df = dim_engine
    load_dimension(df, "dim_engine")


if __name__ == "__main__":

    load_all_dimensions(
        dim_aircraft,
        dim_engine,
        dim_airport,
        dim_route,
        dim_component
    )




