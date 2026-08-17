import pandas as pd

from ETL.extract.extract import initial_engine_installation_df


from ETL.transform.common.helpers import(
    standardize_columns,
    remove_duplicates,
    strip_strings,
    uppercase_columns
)

from ETL.transform.common.datatype import (
    to_numeric
)

from ETL.transform.common.validation import(
    validate_required_columns,
    validate_unique_key,
    validate_notnull,
    validate_allowed_values
)

from ETL.transform.common.constant import (
    ENGINE_POSITION
)

def transform_engine_installation(df:pd.DataFrame) -> pd.DataFrame:

    df = df.copy()

    #helpers

    df = standardize_columns(df)
    df = remove_duplicates(df)
    df = strip_strings(df)
    df = uppercase_columns(df,
                           [
                               "aircraft_registration",
                               "engine_serial_number",
                               "engine_position"
                           ])

    df = to_numeric(df, ["installation_id"])

    validate_unique_key(df, "installation_id")

    validate_notnull(df,
                     [
                        "installation_id",
                        "aircraft_registration",
                        "engine_serial_number",
                        "engine_position"
                     ])

    validate_required_columns(df,
                              [
                                "installation_id",
                                "aircraft_registration",
                                "engine_serial_number",
                                "engine_position"
                              ])

    validate_allowed_values(df, "engine_position", ENGINE_POSITION)

    return df


transform_engine_installation_df = transform_engine_installation(initial_engine_installation_df)

if __name__ == "__main__":

    print("="*60)
    print("transform_engine_installation_completed")
    print("="*60)


    print(f"rows: {len(transform_engine_installation_df)}")
    print(f"cols: {len(transform_engine_installation_df.columns)}")

    print("\ndataypes")
    print(f"{transform_engine_installation_df.dtypes}")

    print("5 rows")
    print(f'{transform_engine_installation_df.head()}')