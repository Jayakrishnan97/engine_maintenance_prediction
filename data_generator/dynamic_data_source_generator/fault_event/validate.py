"""
Part 3 - Validate Fault Events
"""

from generate import fault_df

print("\n====================================")
print("FACT FAULT EVENT VALIDATION")
print("====================================")


# ==========================================================
# BASIC INFO
# ==========================================================

print(f"\nTotal Fault Events : {len(fault_df):,}")

print(f"Unique Fault IDs : {fault_df['fault_id'].nunique():,}")

print(f"Unique Flights : {fault_df['flight_id'].nunique():,}")

print(f"Unique Engines : {fault_df['engine_serial_number'].nunique():,}")

print(f"Unique Components : {fault_df['component_serial_number'].nunique():,}")


# ==========================================================
# DUPLICATES
# ==========================================================

duplicate_faults = fault_df["fault_id"].duplicated().sum()

print(f"\nDuplicate Fault IDs : {duplicate_faults}")


# ==========================================================
# NULL VALUES
# ==========================================================

print("\n====================================")
print("MISSING VALUES")
print("====================================")

print(fault_df.isnull().sum())


# ==========================================================
# SEVERITY
# ==========================================================

print("\n====================================")
print("SEVERITY DISTRIBUTION")
print("====================================")

print(fault_df["severity"].value_counts())


# ==========================================================
# STATUS
# ==========================================================

print("\n====================================")
print("STATUS DISTRIBUTION")
print("====================================")

print(fault_df["status"].value_counts())


# ==========================================================
# CATEGORY
# ==========================================================

print("\n====================================")
print("FAULT CATEGORY DISTRIBUTION")
print("====================================")

print(fault_df["fault_category"].value_counts())


# ==========================================================
# DETECTION SOURCE
# ==========================================================

print("\n====================================")
print("DETECTION SOURCE")
print("====================================")

print(fault_df["detection_source"].value_counts())


# ==========================================================
# COMPONENTS
# ==========================================================

print("\n====================================")
print("MOST FAILED COMPONENTS")
print("====================================")

print(
    fault_df["component_id"]
    .value_counts()
    .head(10)
)


# ==========================================================
# ENGINES
# ==========================================================

print("\n====================================")
print("ENGINES WITH MOST FAULTS")
print("====================================")

print(
    fault_df["engine_serial_number"]
    .value_counts()
    .head(10)
)


# ==========================================================
# SAMPLE
# ==========================================================

print("\n====================================")
print("SAMPLE RECORDS")
print("====================================")

print(fault_df.head(10))


print("\n====================================")
print("VALIDATION COMPLETE")
print("====================================")