import pandas as pd

from ETL.extract.extract import fact_shop_visit_df

from ETL.transform.common.helpers import (
    standardize_columns,
    remove_duplicates,
    strip_strings,
    uppercase_columns
)

from ETL.transform.common.datatype import (
    to_datetime,
    to_numeric
)

from ETL.transform.common.validation import (
    validate_required_columns,
    validate_unique_key,
    validate_positive,
    validate_notnull,
    validate_allowed_values,
    validate_date_order
)

from ETL.transform.common.constant import (
    VISIT_REASON,
    LLP_REPLACED,
    TEST_CELL_RESULT,
    RETURN_TO_SERVICE,
    SHOP_NAME
)

def transform_fact_shop_visit(df:pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    #common
    df = standardize_columns(df)
    df = remove_duplicates(df)
    df = strip_strings(df)
    df = uppercase_columns(df,
                           [    
                                "maintenance_event_id",
                                "work_order_id"
                                "engine_serial_number",
                                "aircraft_registration",
                                "visit_reason",
                                "shop_name",
                                "llp_replaced",
                                "test_cell_result",
                                "return_to_service"
                           ])

    #datetime & numeric

    df = to_datetime(df,
                     [
                         "arrival_date",
                         "teardown_date",
                         "assembly_date",
                         "completion_date"
                     ])
    df = to_numeric(df,
                    [
                        "modules_removed",
                        "days_in_shop"
                    ])



    #validation
    
    validate_unique_key(df, "shop_visit_id")

    validate_notnull(df,
                     [
                        "shop_visit_id",
                        "maintenance_event_id",
                        "work_order_id"
                        "engine_serial_number",
                        "arrival_date",
                    ])

    validate_required_columns(df,
                              [
                                "shop_visit_id",
                                "maintenance_event_id",
                                "work_order_id",
                                "engine_serial_number",
                                "aircraft_registration",
                                "arrival_date",
                                "completion_date"
                              ])

    validate_allowed_values (df, "visit_reason", VISIT_REASON)

    validate_allowed_values(df, "llp_replaced", LLP_REPLACED)

    validate_allowed_values(df, "test_cell_result", TEST_CELL_RESULT)

    validate_allowed_values(df, "return_to_service", RETURN_TO_SERVICE)

    validate_allowed_values(df, "shop_name", SHOP_NAME)

    validate_positive(df,
                      [
                          "modules_removed",
                          "days_in_shop"
                      ])

    #business rules
    # Teardown cannot happen before arrival

    invalid_teardown_date = df[df['teardown_date'] < df['arrival_date']]

    if not invalid_teardown_date.empty:
        raise ValueError('# Teardown cannot happen before arrival')

    # Assembly cannot happen before teardown

    invalid_assembly_date = df[df['assembly_date'] < df['teardown_date']]

    if not invalid_assembly_date.empty:
        raise ValueError('Assembly cannot happen before teardown')

    # Completion cannot happen before assembly

    invalid_completion_date = df[df['completion_date'] < df['assembly_date']]

    if not invalid_completion_date.empty:
        raise ValueError('Completion cannot happen before assembly')


    # Completion cannot happen before arrival

    invalid_completion_date2 = df[df['completion_date'] < df['arrival_date']]

    if not invalid_completion_date2.empty:
        raise ValueError('Completion cannot happen before arrival')
    

    # Validate days in shop against actual dates

    calculated_days = ((
        df['completion_date'] - df['arrival_date']
    ).dt.total_seconds())/ (24*60*60)

    invalid_total_days = ((df['days_in_shop'] - calculated_days).abs()) > 1

    if invalid_total_days.any():
        raise ValueError("days_in_shop does not match arrival and completion date")


    return df

transform_fact_shop_df = transform_fact_shop_visit(fact_shop_visit_df)

if __name__ == "__main__":

    


    print("="*60)
    print("fact_shop_visit_transform_completed")
    print("="*60)


    print(f"rows: {len(transform_fact_shop_df)}")
    print(f"cols: {len(transform_fact_shop_df.columns)}")


    print("\nDatatypes")
    print(f"{transform_fact_shop_df.dtypes}")


    print("\nFirst Five Records:")
    print(transform_fact_shop_df.head())
