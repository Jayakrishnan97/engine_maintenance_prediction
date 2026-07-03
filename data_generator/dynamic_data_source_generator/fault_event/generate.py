"""
Part 2 - Generate Fault Events
"""

import random
import pandas as pd

from load_data import (
    engine_util_df,
    inventory_lookup,
    engine_components,
)

# ==========================================================
# RANDOM SEED
# ==========================================================

random.seed(42)

# ==========================================================
# MASTER DATA
# ==========================================================

FAULT_CODES = [

    ("OIL001", "Low Oil Pressure", "OIL"),
    ("OIL002", "High Oil Temperature", "OIL"),

    ("FUEL001", "Fuel Pressure Low", "FUEL"),
    ("FUEL002", "Fuel Flow Imbalance", "FUEL"),

    ("IGN001", "Igniter Failure", "IGNITION"),

    ("VIB001", "High Engine Vibration", "VIBRATION"),

    ("TMP001", "High EGT", "TEMPERATURE"),

    ("CMP001", "Compressor Stall", "COMPRESSOR"),

    ("TRB001", "Turbine Blade Damage", "TURBINE"),

    ("SNS001", "Sensor Failure", "SENSOR")

]

SEVERITY = [

    ("LOW",0.70),

    ("MEDIUM",0.20),

    ("HIGH",0.08),

    ("CRITICAL",0.02)

]

DETECTION_SOURCE = [

    "BITE",

    "Pilot Report",

    "EICAS",

    "Maintenance Inspection",

    "Oil Analysis"

]

STATUS = [

    "OPEN",

    "CLOSED",

    "DEFERRED"

]

FAULT_PROBABILITY = 0.03      # 3% of utilization events


# ==========================================================
# OUTPUT
# ==========================================================

fault_records = []

fault_counter = 1


# ==========================================================
# GENERATE
# ==========================================================

for _, util in engine_util_df.iterrows():

    if random.random() > FAULT_PROBABILITY:
        continue

    engine = util["engine_serial_number"]

    if engine not in engine_components:
        continue

    serial = random.choice(engine_components[engine])

    component = inventory_lookup[serial]

    code, description, category = random.choice(FAULT_CODES)

    severity = random.choices(

        population=[x[0] for x in SEVERITY],

        weights=[x[1] for x in SEVERITY],

        k=1

    )[0]

    record = {

        "fault_id":
            f"FLT{fault_counter:09d}",

        "flight_id":
            util["flight_id"],

        "engine_serial_number":
            engine,

        "aircraft_registration":
            util["aircraft_registration"],

        "component_serial_number":
            serial,

        "component_id":
            component["component_id"],

        "fault_date":
            util["utilization_date"],

        "fault_code":
            code,

        "fault_description":
            description,

        "fault_category":
            category,

        "severity":
            severity,

        "detection_source":
            random.choice(DETECTION_SOURCE),

        "status":
            random.choice(STATUS)

    }

    fault_records.append(record)

    fault_counter += 1


# ==========================================================
# DATAFRAME
# ==========================================================

fault_df = pd.DataFrame(fault_records)


print("\n================================")
print("FAULT GENERATION COMPLETE")
print("================================")

print(f"Fault Events : {len(fault_df):,}")

print(f"Unique Engines : {fault_df['engine_serial_number'].nunique() if len(fault_df) else 0}")

print(f"Unique Components : {fault_df['component_serial_number'].nunique() if len(fault_df) else 0}")