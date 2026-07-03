"""
Part 1 - Load Data

Loads all datasets required for fact_fault_event generation.
"""

import pandas as pd
from pathlib import Path


# ==========================================================
# PATHS
# ==========================================================

BASE_PATH = Path(__file__).resolve().parents[3]

DATA_SOURCE = BASE_PATH / "data_source" / "dynamic_datasource"

FLIGHT_PATH = DATA_SOURCE / "fact_flight.csv"
ENGINE_UTIL_PATH = DATA_SOURCE / "fact_engine_utilization.csv"
INVENTORY_PATH = DATA_SOURCE / "engine_component_inventory.csv"
COMPONENT_PATH = "/home/jay/Python_DSA/python/projects/engine_maintenance_prediction/data_source/static_datasource/dim_engine_component.csv"


# ==========================================================
# LOAD CSVs
# ==========================================================

flight_df = pd.read_csv(FLIGHT_PATH)

engine_util_df = pd.read_csv(ENGINE_UTIL_PATH)

inventory_df = pd.read_csv(INVENTORY_PATH)

component_df = pd.read_csv(COMPONENT_PATH)


# ==========================================================
# STANDARDIZE COLUMN NAMES
# ==========================================================

for df in [flight_df, engine_util_df, inventory_df, component_df]:
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
    )


# ==========================================================
# DATE CONVERSION
# ==========================================================

flight_df["actual_departure"] = pd.to_datetime(
    flight_df["actual_departure"]
)

flight_df["actual_arrival"] = pd.to_datetime(
    flight_df["actual_arrival"]
)

engine_util_df["utilization_date"] = pd.to_datetime(
    engine_util_df["utilization_date"]
)

inventory_df["installation_date"] = pd.to_datetime(
    inventory_df["installation_date"]
)

inventory_df["manufacture_date"] = pd.to_datetime(
    inventory_df["manufacture_date"]
)


# ==========================================================
# SORT
# ==========================================================

flight_df = flight_df.sort_values(
    "actual_departure"
).reset_index(drop=True)

engine_util_df = engine_util_df.sort_values(
    ["engine_serial_number", "utilization_date"]
).reset_index(drop=True)


# ==========================================================
# COMPONENT LOOKUP
# ==========================================================

engine_components = (
    inventory_df
    .groupby("engine_serial_number")["component_serial_number"]
    .apply(list)
    .to_dict()
)


# ==========================================================
# COMPONENT MASTER LOOKUP
# ==========================================================

component_lookup = (
    component_df
    .set_index("component_id")
    .to_dict("index")
)


# ==========================================================
# INVENTORY LOOKUP
# ==========================================================

inventory_lookup = (
    inventory_df
    .set_index("component_serial_number")
    .to_dict("index")
)


# ==========================================================
# SUMMARY
# ==========================================================

print("\n===================================")
print("FAULT EVENT LOAD COMPLETE")
print("===================================")

print(f"Flights               : {len(flight_df):,}")
print(f"Engine Utilization    : {len(engine_util_df):,}")
print(f"Inventory Components  : {len(inventory_df):,}")
print(f"Component Master      : {len(component_df):,}")
print(f"Engines               : {len(engine_components):,}")

print("\nLoad Successful")