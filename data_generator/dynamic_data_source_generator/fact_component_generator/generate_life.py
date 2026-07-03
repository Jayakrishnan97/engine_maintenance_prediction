"""
part2_generate_life.py

Generates component utilization records.

Requires:
    from load_data import *
"""

import pandas as pd
from load_data import inventory, engine_utilization, component_state


# ==========================================================
# OUTPUT
# ==========================================================

component_life_records = []

utilization_counter = 1


# ==========================================================
# GROUP COMPONENTS BY ENGINE
# ==========================================================

engine_components = (
    inventory
    .groupby("engine_serial_number")
    ["component_serial_number"]
    .apply(list)
    .to_dict()
)


# ==========================================================
# GENERATE LIFE
# ==========================================================

for _, util in engine_utilization.iterrows():

    engine = util["engine_serial_number"]

    if engine not in engine_components:
        continue

    flight_hours = float(util["flight_hours"])
    flight_cycles = int(util["flight_cycles"])

    event_date = util["utilization_date"]

    for serial in engine_components[engine]:

        state = component_state[serial]

        unit = state["life_unit"]

        # ------------------------------------
        # CALCULATE INCREMENT
        # ------------------------------------

        if unit == "FH":

            increment = flight_hours

        elif unit == "FC":

            increment = flight_cycles

        elif unit == "MO":

            previous = state["last_event_date"]

            months = (
                (event_date.year - previous.year) * 12
                + (event_date.month - previous.month)
            )

            increment = max(months, 0)

            state["last_event_date"] = event_date

        else:
            # On-condition components (no life limit)
            increment = flight_hours

        # ------------------------------------
        # UPDATE COUNTERS
        # ------------------------------------

        state["tsn"] += increment

        install_type = state["installation_type"]

        if install_type in ["NEW", "OVERHAULED"]:
            state["tso"] += increment

        elif install_type == "REPAIRED":
            state["tsr"] += increment

    # ------------------------------------
    # RECORD
    # ------------------------------------

        component_life_records.append({

            "utilization_id":
                f"UTL{utilization_counter:09d}",

            "component_serial_number":
                serial,

            "component_id":
                state["component_id"],

            "engine_serial_number":
                engine,

            "utilization_date":
                event_date,

            "tsn":
                round(state["tsn"], 2),

            "tso":
                round(state["tso"], 2),

            "tsr":
                round(state["tsr"], 2),

            "life_unit":
                state["life_unit"],

            "life_limit":
                state["life_limit"],

            "status":
                state["status"]

        })

        utilization_counter += 1


# ==========================================================
# DATAFRAME
# ==========================================================

component_life = pd.DataFrame(component_life_records)


print()
print("Generation Complete")
print("----------------------------")
print(f"Rows Generated : {len(component_life):,}")
print(f"Unique Engines : {component_life['engine_serial_number'].nunique():,}")
print(f"Unique Components : {component_life['component_serial_number'].nunique():,}")