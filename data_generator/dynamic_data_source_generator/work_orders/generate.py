"""
Part 1 - Generate Work Orders
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

FAULT_PATH = DATA_SOURCE / "fact_fault_event.csv"

# ==========================================================
# LOAD DATA
# ==========================================================

fault_df = pd.read_csv(FAULT_PATH)

fault_df.columns = (
    fault_df.columns
    .str.strip()
    .str.lower()
)

fault_df["fault_date"] = pd.to_datetime(fault_df["fault_date"])

# ==========================================================
# MASTER DATA
# ==========================================================

MAINTENANCE_TYPES = [
    ("INSPECTION", 40),
    ("REPAIR", 35),
    ("REPLACEMENT", 20),
    ("OVERHAUL", 5)
]

TECHNICIANS = [
    f"TECH{i:03d}"
    for i in range(1, 21)
]

TEAMS = [
    "Powerplant",
    "Line Maintenance",
    "Component Shop"
]

STATUS = [
    ("COMPLETED", 80),
    ("OPEN", 10),
    ("IN_PROGRESS", 8),
    ("CANCELLED", 2)
]

# ==========================================================
# OUTPUT
# ==========================================================

work_orders = []

wo_counter = 1

# ==========================================================
# GENERATE
# ==========================================================

for _, fault in fault_df.iterrows():

    maintenance_type = random.choices(
        [x[0] for x in MAINTENANCE_TYPES],
        weights=[x[1] for x in MAINTENANCE_TYPES],
        k=1
    )[0]

    severity = fault["severity"]

    if severity == "LOW":
        priority = "LOW"

    elif severity == "MEDIUM":
        priority = "MEDIUM"

    elif severity == "HIGH":
        priority = "HIGH"

    else:
        priority = "AOG"

    if maintenance_type == "INSPECTION":
        duration = random.randint(2, 4)

    elif maintenance_type == "REPAIR":
        duration = random.randint(6, 16)

    elif maintenance_type == "REPLACEMENT":
        duration = random.randint(4, 8)

    else:
        duration = random.randint(40, 100)

    planned_start = fault["fault_date"]

    planned_end = planned_start + pd.Timedelta(hours=duration)

    status = random.choices(
        [x[0] for x in STATUS],
        weights=[x[1] for x in STATUS],
        k=1
    )[0]

    if status == "COMPLETED":

        actual_start = planned_start

        actual_end = planned_end

    elif status == "IN_PROGRESS":

        actual_start = planned_start

        actual_end = pd.NaT

    else:

        actual_start = pd.NaT

        actual_end = pd.NaT

    record = {

        "work_order_id": f"WO{wo_counter:09d}",

        "fault_id": fault["fault_id"],

        "engine_serial_number": fault["engine_serial_number"],

        "aircraft_registration": fault["aircraft_registration"],

        "component_serial_number": fault["component_serial_number"],

        "component_id": fault["component_id"],

        "work_order_date": planned_start,

        "maintenance_type": maintenance_type,

        "priority": priority,

        "assigned_team": random.choice(TEAMS),

        "technician_id": random.choice(TECHNICIANS),

        "planned_start": planned_start,

        "planned_end": planned_end,

        "actual_start": actual_start,

        "actual_end": actual_end,

        "labor_hours": duration,

        "work_order_status": status

    }

    work_orders.append(record)

    wo_counter += 1

# ==========================================================
# DATAFRAME
# ==========================================================

work_order_df = pd.DataFrame(work_orders)

print("\n===================================")
print("WORK ORDER GENERATION COMPLETE")
print("===================================")

print(f"Work Orders : {len(work_order_df):,}")

print(f"Unique Faults : {work_order_df['fault_id'].nunique():,}")

print(f"Unique Technicians : {work_order_df['technician_id'].nunique():,}")

print(f"Completed : {(work_order_df['work_order_status']=='COMPLETED').sum():,}")