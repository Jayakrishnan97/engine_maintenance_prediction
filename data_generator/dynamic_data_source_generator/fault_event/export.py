"""
Part 4 - Export Fact Fault Event
"""

from pathlib import Path

from generate import fault_df


# ==========================================================
# OUTPUT PATH
# ==========================================================

BASE_PATH = Path(__file__).resolve().parents[3]

OUTPUT_DIR = BASE_PATH / "data_source" / "dynamic_datasource"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

OUTPUT_FILE = OUTPUT_DIR / "fact_fault_event.csv"


# ==========================================================
# EXPORT CSV
# ==========================================================

fault_df.to_csv(
    OUTPUT_FILE,
    index=False
)


# ==========================================================
# SUMMARY
# ==========================================================

print("\n======================================")
print(" FACT FAULT EVENT EXPORTED")
print("======================================")

print(f"Output File : {OUTPUT_FILE.name}")
print(f"Location    : {OUTPUT_DIR}")
print(f"Rows        : {len(fault_df):,}")
print(f"Columns     : {len(fault_df.columns)}")

print("\nColumns")

for column in fault_df.columns:
    print(f" - {column}")

print("\nExport Successful")