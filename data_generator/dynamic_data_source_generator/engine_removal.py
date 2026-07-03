"""
Generate Fact Engine Removal
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


MAINTENANCE_PATH = "/home/jay/Python_DSA/python/projects/engine_maintenance_prediction/data_source/dynamic_datasource/fact_maintenance_event.csv"

UTILIZATION_PATH = "/home/jay/Python_DSA/python/projects/engine_maintenance_prediction/data_source/dynamic_datasource/fact_engine_utilization.csv"

OUTPUT_PATH = "/home/jay/Python_DSA/python/projects/engine_maintenance_prediction/data_source/dynamic_datasource/fact_engine_removal.csv"

# ==========================================================
# LOAD DATA
# ==========================================================

maintenance_df = pd.read_csv(MAINTENANCE_PATH)

utilization_df = pd.read_csv(UTILIZATION_PATH)

maintenance_df.columns = maintenance_df.columns.str.strip().str.lower()

utilization_df.columns = utilization_df.columns.str.strip().str.lower()

maintenance_df["maintenance_date"] = pd.to_datetime(
    maintenance_df["maintenance_date"]
)

utilization_df["utilization_date"] = pd.to_datetime(
    utilization_df["utilization_date"]
)

# ==========================================================
# LATEST ENGINE UTILIZATION
# ==========================================================

latest_utilization = (

    utilization_df

    .sort_values("utilization_date")

    .groupby("engine_serial_number")

    .last()

)

# ==========================================================
# MASTER DATA
# ==========================================================

REMOVAL_REASONS = [

    "PERFORMANCE_DEGRADATION",

    "LLP_LIMIT",

    "FOD",

    "HIGH_VIBRATION",

    "SCHEDULED_OVERHAUL"

]

TECHNICIANS = [

    f"TECH{i:03d}"

    for i in range(1,21)

]

# ==========================================================
# OUTPUT
# ==========================================================

removals = []

counter = 1

# ==========================================================
# GENERATE
# ==========================================================

for _, row in maintenance_df.iterrows():

    maintenance_type = row["maintenance_type"]

    maintenance_result = row["maintenance_result"]

    generate = False

    if maintenance_type == "OVERHAUL":

        generate = True

    elif maintenance_result == "SCRAPPED":

        generate = True

    elif maintenance_type == "REPAIR":

        generate = random.random() < 0.05

    if not generate:

        continue

    engine = row["engine_serial_number"]

    if engine in latest_utilization.index:

        util = latest_utilization.loc[engine]

        engine_hours = util["cumulative_engine_hours"]

        engine_cycles = util["cumulative_engine_cycles"]

    else:

        engine_hours = 0

        engine_cycles = 0

    if maintenance_type == "OVERHAUL":

        reason = "SCHEDULED_OVERHAUL"

        removal_type = "PLANNED"

    elif maintenance_result == "SCRAPPED":

        reason = "FOD"

        removal_type = "UNSCHEDULED"

    else:

        reason = random.choice(REMOVAL_REASONS[:-1])

        removal_type = "UNSCHEDULED"

    replacement_engine = f"ESN{random.randint(700001,700050):06d}"

    record = {

        "removal_id": f"RM{counter:09d}",

        "maintenance_event_id": row["maintenance_event_id"],

        "work_order_id": row["work_order_id"],

        "engine_serial_number": engine,

        "aircraft_registration": row["aircraft_registration"],

        "removal_date": row["maintenance_date"],

        "removal_reason": reason,

        "removal_type": removal_type,

        "engine_hours_at_removal": engine_hours,

        "engine_cycles_at_removal": engine_cycles,

        "removed_by": random.choice(TECHNICIANS),

        "replacement_engine_serial": replacement_engine,

        "removal_status": "COMPLETED"

    }

    removals.append(record)

    counter += 1

# ==========================================================
# DATAFRAME
# ==========================================================

removal_df = pd.DataFrame(removals)

# ==========================================================
# VALIDATION
# ==========================================================

print("\n===================================")
print("FACT ENGINE REMOVAL")
print("===================================")

print(f"Rows : {len(removal_df):,}")

print(f"Duplicate IDs : {removal_df['removal_id'].duplicated().sum()}")

print("\nRemoval Types")

print(removal_df["removal_type"].value_counts())

print("\nRemoval Reasons")

print(removal_df["removal_reason"].value_counts())

print("\nMissing Values")

print(removal_df.isnull().sum())

print("\nSample")

print(removal_df.head())

# ==========================================================
# EXPORT
# ==========================================================

removal_df.to_csv(

    OUTPUT_PATH,

    index=False

)

print("\n===================================")

print("ENGINE REMOVAL EXPORTED")

print("===================================")

print(f"Rows : {len(removal_df):,}")

print(f"File : {OUTPUT_PATH}")


