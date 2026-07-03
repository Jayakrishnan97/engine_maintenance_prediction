"""
part3_validate.py

Validates generated component life records.
"""

import pandas as pd

from generate_life import component_life


print("\n==========================================")
print(" FACT COMPONENT LIFE VALIDATION")
print("==========================================")

# ==========================================================
# BASIC INFO
# ==========================================================

print(f"\nTotal Rows              : {len(component_life):,}")

print(f"Unique Components       : {component_life['component_serial_number'].nunique():,}")

print(f"Unique Engines          : {component_life['engine_serial_number'].nunique():,}")

print(f"Unique Utilization IDs  : {component_life['utilization_id'].nunique():,}")


# ==========================================================
# DUPLICATES
# ==========================================================

duplicate_ids = component_life["utilization_id"].duplicated().sum()

print(f"\nDuplicate Utilization IDs : {duplicate_ids}")


# ==========================================================
# NULL VALUES
# ==========================================================

print("\nMissing Values")

print("------------------------------------------")

print(component_life.isnull().sum())


# ==========================================================
# LIFE UNIT DISTRIBUTION
# ==========================================================

print("\nLife Unit Distribution")

print("------------------------------------------")

print(component_life["life_unit"].value_counts(dropna=False))


# ==========================================================
# STATUS DISTRIBUTION
# ==========================================================

print("\nComponent Status")

print("------------------------------------------")

print(component_life["status"].value_counts(dropna=False))


# ==========================================================
# CHECK TSN NEVER DECREASES
# ==========================================================

print("\nChecking TSN Progression...")

errors = 0

for serial, group in component_life.groupby("component_serial_number"):

    values = group["tsn"].tolist()

    if values != sorted(values):

        errors += 1

print(f"Components with TSN Errors : {errors}")


# ==========================================================
# CHECK TSO NEVER DECREASES
# ==========================================================

print("\nChecking TSO Progression...")

errors = 0

for serial, group in component_life.groupby("component_serial_number"):

    values = group["tso"].fillna(0).tolist()

    if values != sorted(values):

        errors += 1

print(f"Components with TSO Errors : {errors}")


# ==========================================================
# CHECK TSR NEVER DECREASES
# ==========================================================

print("\nChecking TSR Progression...")

errors = 0

for serial, group in component_life.groupby("component_serial_number"):

    values = group["tsr"].fillna(0).tolist()

    if values != sorted(values):

        errors += 1

print(f"Components with TSR Errors : {errors}")


# ==========================================================
# LIFE LIMIT CHECK
# ==========================================================

print("\nChecking Life Limit Exceedance...")

exceeded = component_life[
    component_life["tsn"] > component_life["life_limit"]
]

print(f"Components exceeding life limit : {len(exceeded):,}")


# ==========================================================
# SAMPLE
# ==========================================================

print("\nSample Records")

print("------------------------------------------")

print(component_life.head(10))


print("\n==========================================")
print(" VALIDATION COMPLETE")
print("==========================================")