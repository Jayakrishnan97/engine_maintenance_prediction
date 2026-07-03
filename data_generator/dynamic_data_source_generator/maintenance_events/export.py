"""
Part 2 - Validate & Export Maintenance Events
"""

from pathlib import Path

from generate import maintenance_df

# ==========================================================
# VALIDATION
# ==========================================================

print("\n========================================")
print("FACT MAINTENANCE EVENT VALIDATION")
print("========================================")

print(f"\nTotal Maintenance Events : {len(maintenance_df):,}")

print(f"Unique Maintenance Events : {maintenance_df['maintenance_event_id'].nunique():,}")

print(f"Unique Work Orders : {maintenance_df['work_order_id'].nunique():,}")

print(f"Unique Engines : {maintenance_df['engine_serial_number'].nunique():,}")

print(f"Unique Components : {maintenance_df['component_serial_number'].nunique():,}")


# ==========================================================
# DUPLICATES
# ==========================================================

duplicates = maintenance_df["maintenance_event_id"].duplicated().sum()

print(f"\nDuplicate Maintenance Event IDs : {duplicates}")


# ==========================================================
# MISSING VALUES
# ==========================================================

print("\n========================================")
print("MISSING VALUES")
print("========================================")

print(maintenance_df.isnull().sum())


# ==========================================================
# MAINTENANCE TYPE
# ==========================================================

print("\n========================================")
print("MAINTENANCE TYPE DISTRIBUTION")
print("========================================")

print(maintenance_df["maintenance_type"].value_counts())


# ==========================================================
# MAINTENANCE RESULT
# ==========================================================

print("\n========================================")
print("MAINTENANCE RESULT")
print("========================================")

print(maintenance_df["maintenance_result"].value_counts())


# ==========================================================
# ACTION TAKEN
# ==========================================================

print("\n========================================")
print("ACTION TAKEN")
print("========================================")

print(maintenance_df["action_taken"].value_counts())


# ==========================================================
# PARTS REPLACED
# ==========================================================

print("\n========================================")
print("PARTS REPLACED")
print("========================================")

print(maintenance_df["parts_replaced"].value_counts())


# ==========================================================
# RELEASE TO SERVICE
# ==========================================================

print("\n========================================")
print("RELEASE TO SERVICE")
print("========================================")

print(maintenance_df["release_to_service"].value_counts())


# ==========================================================
# TECHNICIAN DISTRIBUTION
# ==========================================================

print("\n========================================")
print("TOP TECHNICIANS")
print("========================================")

print(
    maintenance_df["technician_id"]
    .value_counts()
    .head(10)
)


# ==========================================================
# LABOR HOURS
# ==========================================================

print("\n========================================")
print("LABOR HOURS")
print("========================================")

print(maintenance_df["labor_hours"].describe())


# ==========================================================
# SAMPLE RECORDS
# ==========================================================

print("\n========================================")
print("SAMPLE RECORDS")
print("========================================")

print(maintenance_df.head(10))


# ==========================================================
# EXPORT
# ==========================================================

BASE_PATH = Path(__file__).resolve().parents[3]

OUTPUT_DIR = BASE_PATH / "data_source" / "dynamic_datasource"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

OUTPUT_FILE = OUTPUT_DIR / "fact_maintenance_event.csv"

maintenance_df.to_csv(
    OUTPUT_FILE,
    index=False
)


# ==========================================================
# SUMMARY
# ==========================================================

print("\n========================================")
print("FACT MAINTENANCE EVENT EXPORTED")
print("========================================")

print(f"Output File : {OUTPUT_FILE.name}")

print(f"Location    : {OUTPUT_DIR}")

print(f"Rows        : {len(maintenance_df):,}")

print(f"Columns     : {len(maintenance_df.columns)}")

print("\nExport Successful")