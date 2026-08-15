import pandas as pd

from ETL.extract.extract import initial_engine_component_inventory_df

from ETL.transform.common.helpers import (
    standardize_columns,
    remove_duplicates,
    strip_strings,
    uppercase_columns
)

from ETL.transform.common.datatype import (
    to_datetime
)

from ETL.transform.common.validation import (
    validate_required_columns,
    validate_unique_key,
    validate_notnull,
    validate_allowed_values
)

from ETL.transform.common.constant import (
    POSITION
)



def transform_engine_component_inventory(df:pd.DataFrame) -> pd.DataFrame:

    df = df.copy()

    #helpers

    df = standardize_columns(df)
    df = remove_duplicates(df)
    df = strip_strings(df)
    df = uppercase_columns(df,
                           [
                               "component_name",
                               "position",
                               "installation_type",
                               "status"
                           ])

    
    # datetime

    df = to_datetime(df,
                     [
                        "manufacture_date",
                        "installation_date"
                     ])



    #validate

    validate_unique_key(df, "inventory_id")

    validate_notnull(df,
                     [
                        "inventory_id",
                        "component_id",
                        "engine_serial_number",
                        "installation_date"
                     ])

    validate_required_columns(df,
                              [
                                "inventory_id",
                                "component_id",
                                "engine_serial_number",
                                "installation_date",
                                "component_name"
                              ])

    validate_allowed_values(df, "position", POSITION)

    #business rule

    invalid_date = df[df["installation_date"] < df["manufacture_date"]]

    if not invalid_date.empty:
        raise ValueError("installation date cannot be earlier than manufacture date")

    
    return df

if __name__ == "__main__":

    transform_engine_component_inventory_df = transform_engine_component_inventory(initial_engine_component_inventory_df)

    print("="*60)
    print("transform_engine_component_inventory_completed")
    print("="*60)


    print(f"rows: {len(transform_engine_component_inventory_df)}")
    print(f"cols: {len(transform_engine_component_inventory_df.columns)}")

    print("\ndataypes")
    print(f"{transform_engine_component_inventory_df.dtypes}")

    print("5 rows")
    print(f'{transform_engine_component_inventory_df.head()}')