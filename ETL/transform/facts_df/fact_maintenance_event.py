import pandas as pd

from ETL.extract.extract import fact_maintenance_event_df

from ETL.transform.common.helpers import (
    standardize_columns,
    remove_duplicates,
    strip_strings,
    uppercase_columns
)

from ETL.transform.common.datatype import (
    to_numeric,
    to_datetime
)

from ETL.transform.common.validation import (
    validate_required_columns,
    validate_unique_key,
    validate_positive,
    validate_notnull,
    validate_allowed_values
)

from ETL.transform.common.constant import (
    MAINTENANCE_RESULT,
    MAINTENANCE_TYPE,
    ACTION_TAKEN,
    PARTS_REPLACED,
    RELEASE_TO_SERVICE
)


def transform_fact_maintenance_event(df:pd.DataFrame) -> pd.DataFrame:

    df = df.copy()

    #helpers

    df = standardize_columns(df)
    df = remove_duplicates(df)
    df = strip_strings(df)
    df = uppercase_columns(df,
                           [
                               "engine_serial_number",
                               "aircraft_registration",
                               "maintenance_type",
                               "action_taken",
                               "parts_replaced",
                               "maintenance_result",
                               "release_to_service"
                           ])

    #date and numeric
    df = to_datetime(df, ["maintenance_date"])

    df = to_numeric(df, ["labor_hours"])

    #validation

    validate_unique_key(df, "maintenance_event_id")

    validate_positive(df, ["labor_hours"])

    validate_notnull(df,
                     [
                        "maintenance_event_id",
                        "work_order_id",
                        "fault_id",
                        "engine_serial_number",
                        "aircraft_registration",
                        "maintenance_date"
                     ])

    validate_required_columns(df,
                              [
                                "maintenance_event_id",
                                "work_order_id",
                                "fault_id",
                                "engine_serial_number",
                                "aircraft_registration",
                                "maintenance_date"   
                              ])


    validate_allowed_values (df, "maintenance_type", MAINTENANCE_TYPE)
    validate_allowed_values (df, "action_taken", ACTION_TAKEN)
    validate_allowed_values (df, "parts_replaced", PARTS_REPLACED)
    validate_allowed_values (df, "maintenance_result", MAINTENANCE_RESULT)
    validate_allowed_values (df, "release_to_service", RELEASE_TO_SERVICE)


    return df



if __name__ == "__main__":
    transform_fact_maintenance_event_df = transform_fact_maintenance_event(fact_maintenance_event_df)

    print("="*60)
    print("fact_maintenance_transform_completed")
    print("="*60)

    print(f"rows: {len(transform_fact_maintenance_event_df)}")
    print(f"cols: {len(transform_fact_maintenance_event_df.columns)}")

    print("\nData Types:")
    print(f"{transform_fact_maintenance_event_df.dtypes}")

    print("\nFirst Five Records:")
    print(transform_fact_maintenance_event_df.head())