import pandas as pd

from ETL.extract.extract import fact_component_life_df


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
)

from ETL.transform.common.constant import(
    LIFE_UNITS
)


def transform_fact_component_life(df:pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    #helpers
    df = standardize_columns(df)
    df = remove_duplicates(df)
    df = strip_strings(df)
    df = uppercase_columns(df,
                           [
                               "utilization_id",
                               "component_id",
                               "engine_serial_number",
                               "status"
                           ])

    #datetime

    df = to_numeric(df, ["tsn","tso","tsr", "life_limit"])

    df = to_datetime(df, ["utilization_date"])

    #validation

    validate_unique_key(df, "utilization_id")

    validate_positive(df, ["tsn","tso","tsr", "life_limit"])

    validate_notnull(df,
                     [
                        "utilization_id",
                        "component_serial_number",
                        "component_id",
                        "engine_serial_number"
                     ])


    validate_required_columns(df,
                              [
                                "utilization_id",
                                "component_serial_number",
                                "component_id",
                                "engine_serial_number",
                                "life_unit",
                                "status",
                                "tsn",
                                "tso",
                                "tsr",
                                "life_limit"
                              ])


    #business rule

    invalid_values = df[
                        df['life_limit'].notna() &
                        df["life_unit"].isna()]

    if not invalid_values.empty:
        raise ValueError('life units cannot be empty to life limit component')

    return df


transform_fact_component_life_df = transform_fact_component_life(fact_component_life_df)

if __name__ == "__main__":


    print("="*60)
    print("transform_fact_component_life_completed")
    print("="*60)


    print(f"rows: {len(transform_fact_component_life_df)}")
    print(f"cols: {len(transform_fact_component_life_df.columns)}")

    print("\ndataypes")
    print(f"{transform_fact_component_life_df.dtypes}")

    print("5 rows")
    print(f'{transform_fact_component_life_df.head()}')