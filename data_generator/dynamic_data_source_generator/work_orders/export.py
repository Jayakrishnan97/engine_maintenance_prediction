"""
Part 2 - Validate & Export Work Orders
"""

from pathlib import Path

from generate import work_order_df

# ==========================================================
# VALIDATION
# ==========================================================

print("\n========================================")
print("FACT WORK ORDER VALIDATION")
print("========================================")

print(f"\nTotal Work Orders : {len(work_order_df):,}")

print(f"Unique Work Orders : {work_order_df['work_order_id'].nunique():,}")

print(f"Unique Faults : {work_order_df['fault_id'].nunique():,}")

print(f"Unique Engines : {work_order_df['engine_serial_number'].nunique():,}")

print(f"Unique Components : {work_order_df['component_serial_number'].nunique():,}")


# ==========================================================
# DUPLICATES
# ==========================================================

duplicates = work_order_df["work_order_id"].duplicated().sum()

print(f"\nDuplicate Work Order IDs : {duplicates}")


# ==========================================================
# MISSING VALUES
# ==========================================================

print("\n========================================")
print("MISSING VALUES")
print("========================================")

print(work_order_df.isnull().sum())


# ==========================================================
# MAINTENANCE TYPE
# ==========================================================

print("\n========================================")
print("MAINTENANCE TYPE")
print("========================================")

print(work_order_df["maintenance_type"].value_counts())


# ==========================================================
# PRIORITY
# ==========================================================

print("\n========================================")
print("PRIORITY")
print("========================================")

print(work_order_df["priority"].value_counts())


# ==========================================================
# STATUS
# ==========================================================

print("\n========================================")
print("WORK ORDER STATUS")
print("========================================")

print(work_order_df["work_order_status"].value_counts())


# ==========================================================
# ASSIGNED TEAM
# ==========================================================

print("\n========================================")
print("ASSIGNED TEAM")
print("========================================")

print(work_order_df["assigned_team"].value_counts())


# ==========================================================
# TOP TECHNICIANS
# ==========================================================

print("\n========================================")
print("TOP TECHNICIANS")
print("========================================")

print(
    work_order_df["technician_id"]
    .value_counts()
    .head(10)
)


# ==========================================================
# LABOR HOURS
# ==========================================================

print("\n========================================")
print("LABOR HOURS")
print("========================================")

print(work_order_df["labor_hours"].describe())


# ==========================================================
# SAMPLE
# ==========================================================

print("\n========================================")
print("SAMPLE RECORDS")
print("========================================")

print(work_order_df.head(10))


# ==========================================================
# EXPORT
# ==========================================================

BASE_PATH = Path(__file__).resolve().parents[3]

OUTPUT_DIR = BASE_PATH / "data_source" / "dynamic_datasource"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

OUTPUT_FILE = OUTPUT_DIR / "fact_work_order.csv"

work_order_df.to_csv(
    OUTPUT_FILE,
    index=False
)


# ==========================================================
# SUMMARY
# ==========================================================

print("\n========================================")
print("FACT WORK ORDER EXPORTED")
print("========================================")

print(f"Output File : {OUTPUT_FILE.name}")

print(f"Location    : {OUTPUT_DIR}")

print(f"Rows        : {len(work_order_df):,}")

print(f"Columns     : {len(work_order_df.columns)}")

print("\nExport Successful")