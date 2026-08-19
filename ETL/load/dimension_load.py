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


load_dimension(dim_aircraft, "dim_aircraft")

load_dimension(dim_airport, "dim_airport")

load_dimension(dim_route, "dim_route")

load_dimension(dim_component, "dim_component")

load_dimension(dim_engine, "dim_engine")




