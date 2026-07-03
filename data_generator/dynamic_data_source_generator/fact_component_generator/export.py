"""
part4_export.py

Exports fact_component_life.csv
"""

from pathlib import Path

from generate_life import component_life


# ==========================================================
# OUTPUT PATH
# ==========================================================

BASE_PATH = Path(__file__).resolve().parents[3]

OUTPUT_DIR = BASE_PATH / "data_source" /"dynamic_datasource"

OUTPUT_DIR.mkdir(exist_ok=True)

OUTPUT_FILE = OUTPUT_DIR / "fact_component_life.csv"


# ==========================================================
# EXPORT
# ==========================================================

component_life.to_csv(
    OUTPUT_FILE,
    index=False
)


# ==========================================================
# SUMMARY
# ==========================================================

print("\n====================================")
print("FACT COMPONENT LIFE EXPORTED")
print("====================================")

print(f"Output File : {OUTPUT_FILE.name}")
print(f"Location    : {OUTPUT_DIR}")
print(f"Rows        : {len(component_life):,}")
print(f"Columns     : {len(component_life.columns)}")

print("\nColumns")

for col in component_life.columns:
    print(f" - {col}")

print("\nExport Complete")