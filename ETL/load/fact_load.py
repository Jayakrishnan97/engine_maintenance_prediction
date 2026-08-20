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


def main():
    load_fact_df(transform_engine_component_inventory_df, "engine_component_inventory")

    load_fact_df(transform_engine_installation_df, "engine_installation")

    load_fact_df(transform_fact_component_life_df, "fact_component_life")

    load_fact_df(transform_fact_engine_removal_df, "fact_engine_removal")

    load_fact_df(transform_fact_engine_utilization_df, "fact_engine_utilization")

    load_fact_df(transform_fact_fault_event_df, "fact_fault_event")

    load_fact_df(transform_fact_flight_df, "fact_flight")

    load_fact_df(transform_fact_maintenance_event_df, "fact_maintenance_event")

    load_fact_df(transform_fact_shop_df, "fact_shop_visit")

    load_fact_df(transform_fact_workorder_df, "fact_workorder")


if __name__ == "__main__":
    main()


