"""
part1_load_data.py

Loads all source datasets and initializes component state.
"""

import pandas as pd
from pathlib import Path


# ==========================================================
# PATHS
# ==========================================================

components_path = "/home/jay/Python_DSA/python/projects/engine_maintenance_prediction/data_source/static_datasource/dim_engine_component.csv"
inventory_path = "/home/jay/Python_DSA/python/projects/engine_maintenance_prediction/data_source/dynamic_datasource/engine_component_inventory.csv"
engine_util_path = "/home/jay/Python_DSA/python/projects/engine_maintenance_prediction/data_source/dynamic_datasource/fact_engine_utilization.csv"


# ==========================================================
# LOAD CSVs
# ==========================================================

components = pd.read_csv(components_path)
inventory = pd.read_csv(inventory_path)
engine_utilization = pd.read_csv(engine_util_path)


# ==========================================================
# CLEAN DATA
# ==========================================================

components.columns = components.columns.str.strip().str.lower()
inventory.columns = inventory.columns.str.strip().str.lower()
engine_utilization.columns = engine_utilization.columns.str.strip().str.lower()


# ==========================================================
# KEEP ONLY REQUIRED COLUMNS
# ==========================================================

component_master = components[
    [
        "component_id",
        "life_unit",
        "life_limit",
    ]
]

inventory = inventory[
    [
        "component_serial_number",
        "component_id",
        "engine_serial_number",
        "installation_type",
        "installation_date",
        "manufacture_date",
        "status",
    ]
]


# ==========================================================
# MERGE
# ==========================================================

inventory = inventory.merge(
    component_master,
    on="component_id",
    how="left",
)


# ==========================================================
# NORMALIZE LIFE UNIT
# ==========================================================

def normalize_life_unit(unit):

    if pd.isna(unit):
        return None

    unit = str(unit).strip().upper()

    mapping = {
        "FH": "FH",
        "HOUR": "FH",
        "HOURS": "FH",

        "FC": "FC",
        "CYCLE": "FC",
        "CYCLES": "FC",

        "MO": "MO",
        "MONTH": "MO",
        "MONTHS": "MO"
    }

    return mapping.get(unit)


inventory["life_unit"] = inventory["life_unit"].apply(normalize_life_unit)


# ==========================================================
# DATE CONVERSION
# ==========================================================

inventory["installation_date"] = pd.to_datetime(
    inventory["installation_date"]
)

inventory["manufacture_date"] = pd.to_datetime(
    inventory["manufacture_date"]
)

engine_utilization["utilization_date"] = pd.to_datetime(
    engine_utilization["utilization_date"]
)


# ==========================================================
# SORT UTILIZATION
# ==========================================================
engine_utilization = (
    engine_utilization
    .sort_values(
        ["engine_serial_number", "utilization_date"]
    )
    .reset_index(drop=True)
)

# ==========================================================
# INITIAL COMPONENT STATE
# ==========================================================

component_state = {}

for _, row in inventory.iterrows():

    component_state[row["component_serial_number"]] = {

        "component_id": row["component_id"],

        "engine_serial_number": row["engine_serial_number"],

        "installation_type": str(row["installation_type"]).upper(),

        "life_unit": row["life_unit"],

        "life_limit": row["life_limit"],

        "installation_date": row["installation_date"],

        "manufacture_date": row["manufacture_date"],

        "status": str(row["status"]).upper(),

        # Running counters
        "tsn": 0.0,
        "tso": 0.0,
        "tsr": 0.0,

        # Used later for month calculations
        "last_event_date": row["installation_date"],
    }


print(f"Components Loaded      : {len(components):,}")
print(f"Inventory Loaded      : {len(inventory):,}")
print(f"Engine Util Records   : {len(engine_utilization):,}")
print(f"Component States      : {len(component_state):,}")