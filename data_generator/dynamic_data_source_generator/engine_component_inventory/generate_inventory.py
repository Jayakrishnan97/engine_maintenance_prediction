import pandas as pd
import random
from datetime import timedelta

from load_data import (
    engines,
    serialized_components,
    generate_component_serial,
    get_position,
    get_installation_type,
    DEFAULT_STATUS
)

# Load data
engines = pd.read_csv("/home/jay/Python_DSA/python/projects/engine_maintenance_prediction/data_source/static_datasource/dim_engine.csv")
components = pd.read_csv("/home/jay/Python_DSA/python/projects/engine_maintenance_prediction/data_source/static_datasource/dim_engine_component.csv")

engines["engine_manufacture_date"] = pd.to_datetime(
    engines["engine_manufacture_date"]
)

serialized_components = components[
    components["serialized"].str.upper() == "YES"
].copy()

# ==========================================================
# INVENTORY RECORDS
# ==========================================================

inventory_records = []

inventory_id = 1

# ==========================================================
# LOOP THROUGH EVERY ENGINE
# ==========================================================

for _, engine in engines.iterrows():

    engine_serial = engine["engine_serial_number"]

    engine_mfg = engine["engine_manufacture_date"]

    # Loop through every serialized component
    for _, component in serialized_components.iterrows():

        component_serial = generate_component_serial()

        # -----------------------------------------
        # Component Manufacture Date
        # Must be before or on engine manufacture
        # -----------------------------------------

        manufacture_date = engine_mfg - timedelta(
            days=random.randint(0, 365 * 2)
        )

        # -----------------------------------------
        # Installation Date
        # Between engine manufacture and +180 days
        # -----------------------------------------

        installation_date = engine_mfg + timedelta(
            days=random.randint(0, 180)
        )

        # -----------------------------------------
        # Installation Type
        # -----------------------------------------

        installation_type = get_installation_type(
            component["maintenance_type"]
        )

        # -----------------------------------------
        # Position
        # -----------------------------------------

        position = get_position(
            component["component_name"]
        )

        # -----------------------------------------
        # Build Record
        # -----------------------------------------

        inventory_records.append({

            "inventory_id":
                f"INV{inventory_id:07d}",

            "component_serial_number":
                component_serial,

            "component_id":
                component["component_id"],

            "component_name":
                component["component_name"],

            "engine_serial_number":
                engine_serial,

            "manufacture_date":
                manufacture_date.date(),

            "installation_date":
                installation_date.date(),

            "position":
                position,

            "installation_type":
                installation_type,

            "status":
                DEFAULT_STATUS

        })

        inventory_id += 1