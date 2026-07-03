import pandas as pd

# ==========================================================
# CONFIGURATION
# ==========================================================

ENGINE_FILE = "/home/jay/Python_DSA/python/projects/engine_maintenance_prediction/data_source/static_datasource/dim_engine.csv"
COMPONENT_FILE = "/home/jay/Python_DSA/python/projects/engine_maintenance_prediction/data_source/static_datasource/dim_engine_component.csv"

# ==========================================================
# LOAD DATA
# ==========================================================

engines = pd.read_csv(ENGINE_FILE)
components = pd.read_csv(COMPONENT_FILE)

# ==========================================================
# VALIDATION
# ==========================================================

required_engine_columns = [
    "engine_serial_number",
    "engine_model",
    "engine_manufacture_date",
    "engine_status"
]

required_component_columns = [
    "component_id",
    "component_name",
    "maintenance_type",
    "life_unit",
    "life_limit",
    "repairable",
    "serialized"
]

for col in required_engine_columns:
    if col not in engines.columns:
        raise ValueError(f"Missing column in dim_engine.csv : {col}")

for col in required_component_columns:
    if col not in components.columns:
        raise ValueError(f"Missing column in dim_component.csv : {col}")

# ==========================================================
# CLEAN DATA
# ==========================================================

engines["engine_manufacture_date"] = pd.to_datetime(
    engines["engine_manufacture_date"]
)

components["serialized"] = (
    components["serialized"]
    .astype(str)
    .str.upper()
)

components["maintenance_type"] = (
    components["maintenance_type"]
    .astype(str)
    .str.upper()
)

# ==========================================================
# KEEP ONLY SERIALIZED COMPONENTS
# ==========================================================

serialized_components = components[
    components["serialized"] == "YES"
].copy()

# ==========================================================
# POSITION MAPPING
# ==========================================================

POSITION_MAP = {

    "Fan Disk": "CENTER",
    "Fan Shaft": "CENTER",

    "LPC Stage 1 Disk": "STAGE1",
    "LPC Stage 2 Disk": "STAGE2",
    "LPC Stage 3 Disk": "STAGE3",

    "HPC Stage 1 Disk": "STAGE1",
    "HPC Stage 2 Disk": "STAGE2",
    "HPC Stage 3 Disk": "STAGE3",
    "HPC Stage 4 Disk": "STAGE4",
    "HPC Stage 5 Disk": "STAGE5",

    "HPT Stage 1 Disk": "STAGE1",
    "HPT Stage 2 Disk": "STAGE2",

    "LPT Stage 1 Disk": "STAGE1",
    "LPT Stage 2 Disk": "STAGE2",
    "LPT Stage 3 Disk": "STAGE3",
    "LPT Stage 4 Disk": "STAGE4",

    "Fuel Pump": "CENTER",
    "Oil Pump": "CENTER",
    "Starter": "CENTER",

    "Igniter Plug A": "A",
    "Igniter Plug B": "B"
}

# ==========================================================
# DEFAULT POSITION
# ==========================================================

def get_position(component_name):

    return POSITION_MAP.get(
        component_name,
        "CENTER"
    )

# ==========================================================
# INSTALLATION TYPE
# ==========================================================

def get_installation_type(maintenance_type):

    if maintenance_type == "LIFE_LIMITED":
        return "NEW"

    elif maintenance_type == "HARD_TIME":
        return "NEW"

    elif maintenance_type == "ON_CONDITION":
        return "NEW"

    return "NEW"

# ==========================================================
# COMPONENT STATUS
# ==========================================================

DEFAULT_STATUS = "ACTIVE"

# ==========================================================
# SERIAL NUMBER GENERATOR
# ==========================================================

component_serial_counter = 900001

def generate_component_serial():

    global component_serial_counter

    serial = f"CSN{component_serial_counter}"

    component_serial_counter += 1

    return serial

# ==========================================================
# DATA LOADED SUCCESSFULLY
# ==========================================================

print(f"Engines Loaded              : {len(engines)}")
print(f"Components Loaded           : {len(components)}")
print(f"Serialized Components Only  : {len(serialized_components)}")