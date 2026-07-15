import pandas as pd

from ETL.extract.extract import fact_flight_df

from ETL.transform.common.helpers import(
    standardize_columns,
    remove_duplicates,
    strip_strings,
    uppercase_columns
)

from ETL.transform.common.datatype import(
    to_datetime,
    to_numeric,
)

from ETL.transform.common.validation import (
    validate_required_columns,
    validate_unique_key,
    validate_positive,
    validate_notnull,
    validate_allowed_values,
    validate_date_order,
)

from ETL.transform.common.constant import (
    FLIGHT_STATUS,
)

def transform_fact_flight(df:pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    print(type(df))

    df = standardize_columns(df)
    df = remove_duplicates(df)
    df = strip_strings(df)
    df = uppercase_columns(df,
                           [
                               "aircraft_registration", 
                               "origin",
                               "destination",
                               "left_engine_serial_number",
                               "right_engine_serial_number",
                               "weather",
                               "flight_status"
                           ])

    df = to_datetime(df,
                     [
                         "flight_date",
                         "scheduled_departure",
                         "actual_departure",
                         "scheduled_arrival",
                         "actual_arrival"
                     ])
    
    df = to_numeric(df,
                    [
                        "block_hours",
                        "air_hours",
                        "flight_cycles",
                        "flight_duration_min",
                        "delay_minutes"
                    ])
    
    validate_required_columns(df,
                                   [
                                       "flight_id",
                                       "flight_date",
                                       "aircraft_registration",
                                       "route_id",
                                       "left_engine_serial_number",
                                       "right_engine_serial_number"
                                   ])
    
    validate_unique_key(df,
                                "flight_id"
                             )
    
    validate_notnull(df,
                           [
                            "flight_id",
                            "aircraft_registration",
                            "flight_date"
                           ])
    
    validate_positive(df,
                           [
                               "block_hours",
                               "air_hours",
                               "flight_cycles",
                               "flight_duration_min",
                               "delay_minutes"
                           ])
    
    validate_allowed_values(df,
                                 
                                     "flight_status", FLIGHT_STATUS
                                 )
    
    validate_date_order(df, 
                             
                                "scheduled_departure",
                                "scheduled_arrival"
                             )
    
    validate_date_order(df,
                                "actual_departure",
                                "actual_arrival"
                            )
    
    return df

fact_flight_etl_df = transform_fact_flight(fact_flight_df)


print(fact_flight_etl_df.dtypes)

print(fact_flight_etl_df.head())

