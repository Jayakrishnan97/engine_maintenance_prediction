"""
Part 1 - Generate Maintenance Events
"""

import random
import pandas as pd
from pathlib import Path

# ==========================================================
# RANDOM SEED
# ==========================================================

random.seed(42)

# ==========================================================
# PATHS
# ==========================================================

BASE_PATH = Path(__file__).resolve().parents[3]

DATA_SOURCE = BASE_PATH / "data_source" / "dynamic_datasource"

WORK_ORDER_PATH = DATA_SOURCE / "fact_work_order.csv"

# ==========================================================
# LOAD DATA
# ==========================================================

wo_df = pd.read_csv(WORK_ORDER_PATH)

wo_df.columns = (
    wo_df.columns
    .str.strip()
    .str.lower()
)

wo_df["planned_start"] = pd.to_datetime(wo_df["planned_start"])

wo_df["planned_end"] = pd.to_datetime(wo_df["planned_end"])

wo_df["actual_start"] = pd.to_datetime(wo_df["actual_start"])

wo_df["actual_end"] = pd.to_datetime(wo_df["actual_end"])

# ==========================================================
# MASTER DATA
# ==========================================================

ACTION_MAP = {

    "INSPECTION": [
        "Visual Inspection",
        "Borescope Inspection",
        "Operational Check"
    ],

    "REPAIR": [
        "Repaired",
        "Adjusted",
        "Cleaned"
    ],

    "REPLACEMENT": [
        "Component Replaced"
    ],

    "OVERHAUL": [
        "Overhauled"
    ]

}

RESULTS = [

    ("SERVICEABLE",90),

    ("DEFERRED",8),

    ("SCRAPPED",2)

]

# ==========================================================
# OUTPUT
# ==========================================================

maintenance_records = []

counter = 1

# ==========================================================
# GENERATE
# ==========================================================

for _, wo in wo_df.iterrows():

    # Only completed work orders generate maintenance events
    if wo["work_order_status"] != "COMPLETED":
        continue

    maintenance_type = wo["maintenance_type"]

    action_taken = random.choice(
        ACTION_MAP[maintenance_type]
    )

    maintenance_result = random.choices(

        [x[0] for x in RESULTS],

        weights=[x[1] for x in RESULTS],

        k=1

    )[0]

    release_to_service = (
        "YES"
        if maintenance_result == "SERVICEABLE"
        else "NO"
    )

    parts_replaced = (
        "YES"
        if maintenance_type == "REPLACEMENT"
        else "NO"
    )

    record = {

        "maintenance_event_id":
            f"ME{counter:09d}",

        "work_order_id":
            wo["work_order_id"],

        "fault_id":
            wo["fault_id"],

        "engine_serial_number":
            wo["engine_serial_number"],

        "aircraft_registration":
            wo["aircraft_registration"],

        "component_serial_number":
            wo["component_serial_number"],

        "component_id":
            wo["component_id"],

        "maintenance_date":
            wo["actual_end"],

        "maintenance_type":
            maintenance_type,

        "action_taken":
            action_taken,

        "technician_id":
            wo["technician_id"],

        "labor_hours":
            wo["labor_hours"],

        "parts_replaced":
            parts_replaced,

        "maintenance_result":
            maintenance_result,

        "release_to_service":
            release_to_service

    }

    maintenance_records.append(record)

    counter += 1

# ==========================================================
# DATAFRAME
# ==========================================================

maintenance_df = pd.DataFrame(maintenance_records)

print("\n===================================")
print("MAINTENANCE EVENTS GENERATED")
print("===================================")

print(f"Maintenance Events : {len(maintenance_df):,}")

print(f"Unique Work Orders : {maintenance_df['work_order_id'].nunique():,}")

print(f"Unique Engines     : {maintenance_df['engine_serial_number'].nunique():,}")