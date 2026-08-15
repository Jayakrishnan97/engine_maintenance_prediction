import pandas as pd


from ETL.extract.extract import fact_engine_removal_df

from ETL.transform.common.helpers import (
    standardize_columns,
    remove_duplicates,
    strip_strings,
    uppercase_columns
)

from ETL.transform.common.datatype import(
    to_datetime,
    to_numeric
)

from ETL.transform.common.validation import (
    validate_required_columns,
    validate_unique_key,
    validate_positive,
    validate_notnull,
    validate_allowed_values
)

from ETL.transform.common.constant import (
    REMOVAL_REASON,
    REMOVAL_STATUS,
    REMOVAL_TYPE
)


def transform_fact_engine_removal(df:pd.DataFrame) -> pd.DataFrame:
    df = df.copy()


    #helpers

    df = standardize_columns(df)
    df = remove_duplicates(df)
    df = strip_strings(df)
    df = uppercase_columns(df,
                           [
                               "engine_serial_number",
                               "aircraft_registration",
                               "replacement_engine_serial",
                               "removal_reason",
                               "removal_type",
                               "removal_status"
                           ])


    
    
    #datetime & numeric

    df = to_datetime(df,
                     ["removal_date"])

    df = to_numeric(df,
                    ["engine_hours_at_removal","engine_cycles_at_removal"])


    #validation

    validate_positive (df,
                       [
                            "engine_hours_at_removal","engine_cycles_at_removal"
                       ])

    validate_unique_key(df,"removal_id")

    validate_notnull(df,
                     [
                         "removal_id",
                         "maintenance_event_id",
                         "work_order_id",
                         "engine_serial_number",
                         "removal_date"
                     ])

    validate_required_columns(df,
                              [
                                  "removal_id",
                                  "maintenance_event_id",
                                  "work_order_id",
                                  "engine_serial_number",
                                  "aircraft_registration",
                                  "removal_date"

                              ])


    validate_allowed_values(df, "removal_reason", REMOVAL_REASON)

    validate_allowed_values(df, "removal_type", REMOVAL_TYPE)

    validate_allowed_values(df, "removal_status", REMOVAL_STATUS)


    return df

if __name__ == "__main__":
    transform_fact_engine_removal_df = transform_fact_engine_removal(fact_engine_removal_df)

    print("="*60)
    print("engine removal_transform_completed")
    print("="*60)

    print(f"rows: {len(transform_fact_engine_removal_df)}")
    print(f"cols: {len(transform_fact_engine_removal_df.columns)}")

    print("\nData Types:")
    print(f"{transform_fact_engine_removal_df.dtypes}")

    print("\nFirst Five Records:")
    print(transform_fact_engine_removal_df.head())





