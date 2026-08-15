import pandas as pd

from ETL.extract.extract import fact_fault_event_df

from ETL.transform.common.helpers import (
    standardize_columns,
    remove_duplicates,
    strip_strings,
    uppercase_columns,
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
    FAULT_CATEGORY,
    SEVERITY,
    DETECTION_SOURCE,
    FAULT_STATUS
)


def transform_fact_fault_event(df:pd.DataFrame)->pd.DataFrame:
    df = df.copy()
    
    #cleaning
    df = standardize_columns(df)
    df = strip_strings(df)
    df = remove_duplicates(df)
    df = uppercase_columns(
        df,
        [
        "engine_serial_number",
        "aircraft_registration",
        "component_serial_number",
        "fault_code",
        "fault_description",
        "fault_category",
        "severity",
        "detection_source",
        "status"
        ]
    )
    

    #datatype conversion
    df = to_datetime(
        df,
        [
        "fault_date"
        ]
    )


    #validation

    validate_required_columns(
        df,
        [
            "fault_id",
            "fault_date",
            "flight_id",
            "engine_serial_number",
            "fault_category",
            "severity",
            "status"
        ]
    )

    validate_unique_key(
        df,
        "fault_id"
    )

    validate_notnull(
        df,
        [
        "fault_id",
        "fault_date",
        "flight_id",
        "engine_serial_number"
        ]
    )

    
    validate_allowed_values(
        df,
        "fault_category",
        FAULT_CATEGORY
    )

    validate_allowed_values(
        df,
        "severity",
        SEVERITY
    )

    validate_allowed_values(
        df,
        "detection_source",
        DETECTION_SOURCE
    )

    validate_allowed_values(
        df,
        "status",
        FAULT_STATUS
    )
    
    #business rules

    if df['fault_description'].str.strip().eq('').any():
        raise ValueError(
            "fault description cannot be empty"
        )

    if df["fault_code"].str.strip().eq('').any():
        raise ValueError(
            "fault code cannot be empty"
        )

    return df

if __name__ == "__main__":
    fact_fault_event_etl_df = transform_fact_fault_event(fact_fault_event_df)

    print(f'rows: {len(fact_fault_event_etl_df)}')

    print(f'columns: {len(fact_fault_event_etl_df.columns)}')