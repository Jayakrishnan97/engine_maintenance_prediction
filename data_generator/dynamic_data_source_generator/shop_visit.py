"""
Generate Fact Shop Visit
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

OUTPUT_PATH = "/home/jay/Python_DSA/python/projects/engine_maintenance_prediction/data_source/dynamic_datasource/fact_shop_visit.csv"

MAINTENANCE_PATH = "/home/jay/Python_DSA/python/projects/engine_maintenance_prediction/data_source/dynamic_datasource/fact_maintenance_event.csv"


# ==========================================================
# LOAD DATA
# ==========================================================

maintenance_df = pd.read_csv(MAINTENANCE_PATH)

maintenance_df.columns = (
    maintenance_df.columns
    .str.strip()
    .str.lower()
)

maintenance_df["maintenance_date"] = pd.to_datetime(
    maintenance_df["maintenance_date"]
)

# ==========================================================
# MASTER DATA
# ==========================================================

SHOPS = [

    "GE Engine Shop",

    "Lufthansa Technik",

    "Rolls-Royce MRO",

    "Pratt & Whitney MRO",

    "Air India Engineering"

]

VISIT_REASONS = [

    "PERFORMANCE_RESTORATION",

    "LLP_REPLACEMENT",

    "VIBRATION",

    "FOD",

    "SCHEDULED_OVERHAUL"

]

# ==========================================================
# OUTPUT
# ==========================================================

shop_visits = []

counter = 1

# ==========================================================
# GENERATE
# ==========================================================

for _, row in maintenance_df.iterrows():

    maintenance_type = row["maintenance_type"]

    # ------------------------------------------
    # Only major maintenance enters shop
    # ------------------------------------------

    if maintenance_type == "OVERHAUL":

        generate = True

    else:

        generate = random.random() < 0.05

    if not generate:
        continue

    # ------------------------------------------
    # Visit Reason
    # ------------------------------------------

    if maintenance_type == "OVERHAUL":

        visit_reason = "SCHEDULED_OVERHAUL"

    else:

        visit_reason = random.choice(VISIT_REASONS[:-1])

    # ------------------------------------------
    # Dates
    # ------------------------------------------

    arrival_date = row["maintenance_date"]

    teardown_date = arrival_date + pd.Timedelta(days=1)

    assembly_date = teardown_date + pd.Timedelta(
        days=random.randint(10, 40)
    )

    completion_date = assembly_date + pd.Timedelta(days=2)

    days_in_shop = (
        completion_date - arrival_date
    ).days

    # ------------------------------------------
    # LLP Replacement
    # ------------------------------------------

    llp_replaced = "YES" if (
        visit_reason == "LLP_REPLACEMENT"
    ) else "NO"

    # ------------------------------------------
    # Test Cell
    # ------------------------------------------

    test_cell_result = random.choices(

        ["PASS", "FAIL"],

        weights=[98, 2],

        k=1

    )[0]

    return_to_service = (
        "YES"
        if test_cell_result == "PASS"
        else "NO"
    )

    # ------------------------------------------
    # Record
    # ------------------------------------------

    record = {

        "shop_visit_id":
            f"SV{counter:09d}",

        "maintenance_event_id":
            row["maintenance_event_id"],

        "work_order_id":
            row["work_order_id"],

        "engine_serial_number":
            row["engine_serial_number"],

        "aircraft_registration":
            row["aircraft_registration"],

        "visit_reason":
            visit_reason,

        "shop_name":
            random.choice(SHOPS),

        "arrival_date":
            arrival_date,

        "teardown_date":
            teardown_date,

        "assembly_date":
            assembly_date,

        "completion_date":
            completion_date,

        "days_in_shop":
            days_in_shop,

        "modules_removed":
            random.randint(1,6),

        "llp_replaced":
            llp_replaced,

        "test_cell_result":
            test_cell_result,

        "return_to_service":
            return_to_service

    }

    shop_visits.append(record)

    counter += 1

# ==========================================================
# DATAFRAME
# ==========================================================

shop_visit_df = pd.DataFrame(shop_visits)

# ==========================================================
# VALIDATION
# ==========================================================

print("\n====================================")
print("FACT SHOP VISIT VALIDATION")
print("====================================")

print(f"Total Shop Visits : {len(shop_visit_df):,}")

print(f"Duplicate IDs : {shop_visit_df['shop_visit_id'].duplicated().sum()}")

print("\nMissing Values")

print(shop_visit_df.isnull().sum())

print("\nVisit Reasons")

print(shop_visit_df["visit_reason"].value_counts())

print("\nShop Distribution")

print(shop_visit_df["shop_name"].value_counts())

print("\nTest Cell")

print(shop_visit_df["test_cell_result"].value_counts())

print("\nReturn To Service")

print(shop_visit_df["return_to_service"].value_counts())

print("\nSample")

print(shop_visit_df.head())

# ==========================================================
# EXPORT
# ==========================================================

shop_visit_df.to_csv(

    OUTPUT_PATH,

    index=False

)

print("\n====================================")
print("SHOP VISITS EXPORTED")
print("====================================")

print(f"Rows : {len(shop_visit_df):,}")

print(f"File : {OUTPUT_PATH}")