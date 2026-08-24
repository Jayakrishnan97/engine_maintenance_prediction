import pandas as pd

from ETL.load.connection import get_connection_sql

#==============loading df====================================================================================

from ETL.transform.facts_df.engine_component_inventory import transform_engine_component_inventory_df

from ETL.transform.facts_df.engine_installation import transform_engine_installation_df

from ETL.transform.facts_df.fact_component_life import transform_fact_component_life_df

from ETL.transform.facts_df.fact_engine_removal import transform_fact_engine_removal_df

from ETL.transform.facts_df.fact_engine_utilization import transform_fact_engine_utilization_df

from ETL.transform.facts_df.fact_fault_event import transform_fact_fault_event_df

from ETL.transform.facts_df.fact_flight import transform_fact_flight_df

from ETL.transform.facts_df.fact_maintenance_event import transform_fact_maintenance_event_df

from ETL.transform.facts_df.fact_shop_visit import transform_fact_shop_df

from ETL.transform.facts_df.fact_work_order import transform_fact_workorder_df

#========================================================================================================


def load_fact_df(df:pd.DataFrame, table_name: str) -> None:

    connection = get_connection_sql()

    try:

        df.to_sql(
            table_name,
            connection,
            if_exists="replace",
            index=False
        )

        print(f"{table_name} loaded successfully")

    finally:
        connection.dispose()


def load_all_facts():
    
    df = transform_engine_component_inventory_df
    load_fact_df(df, "engine_component_inventory")


    df = transform_engine_installation_df
    load_fact_df(df, "engine_installation")

    df = transform_fact_component_life_df
    load_fact_df(df, "fact_component_life")

    df = transform_fact_engine_removal_df
    load_fact_df(df, "fact_engine_removal")

    df = transform_fact_engine_utilization_df
    load_fact_df(df, "fact_engine_utilization")

    df = transform_fact_fault_event_df
    load_fact_df(df, "fact_fault_event")

    df = transform_fact_flight_df
    load_fact_df(df, "fact_flight")

    df = transform_fact_maintenance_event_df
    load_fact_df(df, "fact_maintenance_event")

    df = transform_fact_shop_df
    load_fact_df(df, "fact_shop_visit")

    df = transform_fact_workorder_df
    load_fact_df(df, "fact_workorder")


if __name__ == "__main__":
    load_all_facts()


