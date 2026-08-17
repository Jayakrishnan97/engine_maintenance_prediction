import pandas as pd

from ETL.extract.extract import fact_work_order_df

from ETL.transform.common.helpers import(
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
    MAINTENANCE_TYPE,
    PRIORITY,
    ASSIGNED_TEAM,
    WORK_ORDER_STATUS
)



def transform_fact_workorder(df:pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    #common 
    df = standardize_columns(df)
    df = remove_duplicates(df)
    df = strip_strings(df)
    df = uppercase_columns(df,
                           [
                               "engine_serial_number",
                               "aircraft_registration",
                               "component_serial_number",
                               "maintenance_type",
                               "priority",
                               "assigned_team",
                               "technician_id",
                               "work_order_status"
                           ])

    #datetime
    df = to_datetime(df,
                     [
                         "work_order_date",
                         "planned_start",
                         "planned_end",
                         "actual_start",
                         "actual_end"
                     ])

    df = to_numeric(df,
                    ["labour_hours"])


    #validation

    validate_unique_key(df, "work_order_id")

    validate_notnull(
        df,
        [
            "work_order_id",
            "fault_id",
            "engine_serial_number",
            "work_order_date"
        ]
    )

    validate_required_columns(
        df,
        [
            "work_order_id",
            "fault_id",
            "work_order_date",
            "engine_serial_number",
            "aircraft_registration",
            "work_order_status",
            "maintenance_type",
            "priority",

        ]
    )
    #validate constant

    validate_allowed_values(
        df,
        "maintenance_type",
        MAINTENANCE_TYPE
    )

    validate_allowed_values(
        df,
        "priority",
        PRIORITY
    )

    validate_allowed_values(
        df,
        "assigned_team",
        ASSIGNED_TEAM
    )

    validate_allowed_values(
        df,
        "work_order_status",
        WORK_ORDER_STATUS
    )

    validate_positive(
        df,
        ["labor_hours"]
    )

    #1. planned_end >= planned_start

    invalid_plan_dates = df[df['planned_start'] > df['planned_end']]

    if not invalid_plan_dates.empty:
        raise ValueError('planned start cannot be later than planned end')
    
    #2. actual_end >= actual_start

    invalid_actual_dates = df[df['actual_start'] > df['actual_end']]

    if not invalid_actual_dates.empty:
        raise ValueError('actual start date cannot be later than actual end date')
    
    #3. actual_end >= work_order_date

    invalid_completion_date = df[df['actual_end'] < df['work_order_date']]

    if not invalid_completion_date.empty:
        raise ValueError('actual end cannot be earlier than work order date')


    #4. COMPLETED → actual_start and actual_end must exist

    completed_missing_date = df[(df['work_order_status'] == 'COMPLETED') & (
        df['actual_start'].isna() | df['actual_end'].isna())]

    if not completed_missing_date.empty:
        raise ValueError('work_order_status cannot be completed if actual start or end is empty')
    
    return df


transform_fact_workorder_df = transform_fact_workorder(fact_work_order_df)

if __name__ == "__main__":
    

    print("="*60)
    print("work_order_transform_completed")
    print("="*60)

    print(f"rows: {len(transform_fact_workorder_df)}")
    print(f"cols: {len(transform_fact_workorder_df.columns)}")

    print("\nData Types:")
    print(f"{transform_fact_workorder_df.dtypes}")

    print("\nFirst Five Records:")
    print(transform_fact_workorder_df.head())

