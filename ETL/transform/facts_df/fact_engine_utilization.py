import pandas as pd

from ETL.extract.extract import fact_engine_utilization_df

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

from ETL.transform.common.validation import(
    validate_required_columns,
    validate_unique_key,
    validate_positive,
    validate_notnull,
    validate_allowed_values,
    validate_date_order
)

from ETL.transform.common.constant import(
    ENGINE_STATUS
)


def transform_engine_utilization(df:pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df = standardize_columns(df)
    df = remove_duplicates(df)
    df = strip_strings(df)
    df = uppercase_columns(
        df,
        [
            "engine_serial_number",
            "aircraft_registration",
            "engine_status"
        ]
    )

    df = to_datetime(df,
                     [
                        "utilization_date"   
                     ]
    )

    df = to_numeric(df,
                    [
                        "flight_hours",
                        "flight_cycles",
                        "cumulative_engine_hours",
                        "cumulative_engine_cycles"
                    ]
                    )
    
    validate_required_columns(df,
                              [
                                  "utilization_id",
                                  "utilization_date",
                                  "flight_id",
                                  "engine_serial_number",
                                  "aircraft_registration"
                              ])


    validate_unique_key(df,
                        
                            "utilization_id"
                        )
    
    validate_positive(df,[
        "flight_hours",
        "flight_cycles",
        "cumulative_engine_hours",
        "cumulative_engine_cycles"
    ])


    validate_notnull(df,
                     [
                         "utilization_id",
                         "engine_serial_number",
                         "utilization_date"
                     ])
    

    validate_allowed_values(df,
                            "engine_status",
                            ENGINE_STATUS)
    

    return df


transform_fact_engine_utilization_df = transform_engine_utilization(fact_engine_utilization_df)

if __name__ == "__main__":
    

    print(transform_fact_engine_utilization_df.dtypes)

    print(transform_fact_engine_utilization_df.head())

