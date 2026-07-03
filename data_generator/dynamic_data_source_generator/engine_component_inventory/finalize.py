import pandas as pd

from generate_inventory import inventory_records

# ==========================================================
# CREATE DATAFRAME
# ==========================================================

inventory_df = pd.DataFrame(inventory_records)

# ==========================================================
# DATE CONVERSION
# ==========================================================

inventory_df["manufacture_date"] = pd.to_datetime(
    inventory_df["manufacture_date"]
)

inventory_df["installation_date"] = pd.to_datetime(
    inventory_df["installation_date"]
)

# ==========================================================
# VALIDATION
# ==========================================================

# Installation date should never be before manufacture date

invalid_dates = inventory_df[
    inventory_df["installation_date"] < inventory_df["manufacture_date"]
]

if len(invalid_dates) > 0:
    raise ValueError(
        f"{len(invalid_dates)} records have installation date before manufacture date."
    )

# Duplicate Component Serial Numbers

duplicates = inventory_df[
    inventory_df.duplicated(
        subset=["component_serial_number"],
        keep=False
    )
]

if len(duplicates) > 0:
    raise ValueError(
        "Duplicate component serial numbers found."
    )

# ==========================================================
# SORT DATA
# ==========================================================

inventory_df = inventory_df.sort_values(
    by=[
        "engine_serial_number",
        "component_id"
    ]
).reset_index(drop=True)

# ==========================================================
# FORMAT DATES
# ==========================================================

inventory_df["manufacture_date"] = (
    inventory_df["manufacture_date"]
    .dt.strftime("%Y-%m-%d")
)

inventory_df["installation_date"] = (
    inventory_df["installation_date"]
    .dt.strftime("%Y-%m-%d")
)