import pandas as pd

from finalize import inventory_df

# ==========================================================
# OUTPUT FILE
# ==========================================================

OUTPUT_FILE = "/home/jay/Python_DSA/python/projects/engine_maintenance_prediction/data_source/dynamic_datasource/engine_component_inventory.csv"

# ==========================================================
# EXPORT CSV
# ==========================================================

inventory_df.to_csv(
    OUTPUT_FILE,
    index=False
)

