import pandas as pd

from load_data import (
    utilization,
    component_state,
    engine_components,
    months_between
)

# ==========================================================
# OUTPUT RECORDS
# ==========================================================

life_records = []

# ==========================================================
# HELPER FUNCTION
# ==========================================================

def update_component_state(
    state,
    flight_hours,
    flight_cycles,
    utilization_date
):
    """
    Updates TSN / TSO / TSR for one utilization event.
    """

    life_unit = state["life_unit"]



    # --------------------------------------------------
    # HOURS
    # --------------------------------------------------

    if life_unit == "HOURS":

        state["tsn"] += flight_hours

        if state["tso"] is not None:
            state["tso"] += flight_hours

        if state["tsr"] is not None:
            state["tsr"] += flight_hours

    # --------------------------------------------------
    # CYCLES
    # --------------------------------------------------

    elif life_unit == "CYCLES":

        state["tsn"] += flight_cycles

        if state["tso"] is not None:
            state["tso"] += flight_cycles

        if state["tsr"] is not None:
            state["tsr"] += flight_cycles

    # --------------------------------------------------
    # MOS
    # --------------------------------------------------

    elif life_unit == "MOS":

        mos = months_between(
            state["manufacture_date"],
            utilization_date
        )

        state["tsn"] = mos

        if state["tso"] is not None:

            overhaul_months = months_between(
                state["installation_date"],
                utilization_date
            )

            state["tso"] = overhaul_months

        if state["tsr"] is not None:

            repair_months = months_between(
                state["installation_date"],
                utilization_date
            )

            state["tsr"] = repair_months

# ==========================================================
# HELPER FUNCTION
# ==========================================================

def build_fact_row(
    utilization_id,
    engine_serial,
    state
):
    
    tsn_hours = None
    tsn_cycles = None
    tsn_mos = None

    tso_hours = None
    tso_cycles = None
    tso_mos = None

    tsr_hours = None
    tsr_cycles = None
    tsr_mos = None
    
    # --------------------------------------------

    if state["life_unit"] == "HOURS":

        tsn_hours = round(state["tsn"], 2)

        if state["tso"] is not None:
            tso_hours = round(state["tso"], 2)

        if state["tsr"] is not None:
            tsr_hours = round(state["tsr"], 2)

    # --------------------------------------------

    elif state["life_unit"] == "CYCLES":

        tsn_cycles = int(state["tsn"])

        if state["tso"] is not None:
            tso_cycles = int(state["tso"])

        if state["tsr"] is not None:
            tsr_cycles = int(state["tsr"])

    # --------------------------------------------

    elif state["life_unit"] == "MOS":

        tsn_mos = int(state["tsn"])

        if state["tso"] is not None:
            tso_mos = int(state["tso"])

        if state["tsr"] is not None:
            tsr_mos = int(state["tsr"])

    # --------------------------------------------

    return {

        "utilization_id": utilization_id,

        "component_id": state["part_number"],

        "component_serial_number": state["serial_number"],

        "engine_serial_number": engine_serial,

        "tsn_hours": tsn_hours,
        "tsn_cycles": tsn_cycles,
        "tsn_mos": tsn_mos,

        "tso_hours": tso_hours,
        "tso_cycles": tso_cycles,
        "tso_mos": tso_mos,

        "tsr_hours": tsr_hours,
        "tsr_cycles": tsr_cycles,
        "tsr_mos": tsr_mos,
    }

# ==========================================================
# GENERATE COMPONENT LIFE
# ==========================================================

for _, util in utilization.iterrows():

    utilization_id = util["utilization_id"]
    utilization_date = util["utilization_date"]

    engine_serial = util["engine_serial_number"]

    flight_hours = float(util["flight_hours"])
    flight_cycles = int(util["flight_cycles"])

    # ------------------------------------------------------
    # Skip engines with no installed components
    # ------------------------------------------------------

    if engine_serial not in engine_components:
        continue

    # ------------------------------------------------------
    # Process every installed component
    # ------------------------------------------------------

    for key in engine_components[engine_serial]:

        state = component_state[key]

        # ----------------------------------------------
        # Skip until component is installed
        # ----------------------------------------------

        if utilization_date < state["installation_date"]:
            continue

        # ----------------------------------------------
        # Skip removed components (future enhancement)
        # ----------------------------------------------

        if state.get("status") == "REMOVED":
            continue

        # ----------------------------------------------
        # Update TSN / TSO / TSR
        # ----------------------------------------------

        update_component_state(
            state,
            flight_hours,
            flight_cycles,
            utilization_date
        )

        # ----------------------------------------------
        # Create one fact row
        # ----------------------------------------------

        record = build_fact_row(
            utilization_id,
            engine_serial,
            state
        )

        life_records.append(record)

# ==========================================================
# GENERATION SUMMARY
# ==========================================================

print("=" * 60)
print("Component Life Generation Complete")
print(f"Rows Generated : {len(life_records):,}")
print("=" * 60)

# ==========================================================
# CREATE DATAFRAME
# ==========================================================

component_life_df = pd.DataFrame(life_records)

# ==========================================================
# REMOVE DUPLICATES
# ==========================================================

component_life_df.drop_duplicates(inplace=True)

# ==========================================================
# SORT DATA
# ==========================================================

component_life_df.sort_values(
    by=[
        "engine_serial_number",
        "component_id",
        "component_serial_number",
        "utilization_id"
    ],
    inplace=True
)

component_life_df.reset_index(
    drop=True,
    inplace=True
)

# ==========================================================
# VALIDATIONS
# ==========================================================

# Primary Keys
required_columns = [
    "utilization_id",
    "component_id",
    "component_serial_number",
    "engine_serial_number"
]

for col in required_columns:

    if component_life_df[col].isnull().any():

        raise ValueError(
            f"NULL values found in {col}"
        )

# ----------------------------------------------------------
# TSO cannot exceed TSN
# ----------------------------------------------------------

hours = component_life_df[
    (component_life_df["tso_hours"].notna()) &
    (component_life_df["tso_hours"] > component_life_df["tsn_hours"])
]

cycles = component_life_df[
    (component_life_df["tso_cycles"].notna()) &
    (component_life_df["tso_cycles"] > component_life_df["tsn_cycles"])
]

months = component_life_df[
    (component_life_df["tso_mos"].notna()) &
    (component_life_df["tso_mos"] > component_life_df["tsn_mos"])
]

if len(hours):
    raise ValueError("TSO Hours > TSN Hours")

if len(cycles):
    raise ValueError("TSO Cycles > TSN Cycles")

if len(months):
    raise ValueError("TSO MOS > TSN MOS")

# ----------------------------------------------------------
# TSR cannot exceed TSN
# ----------------------------------------------------------

hours = component_life_df[
    (component_life_df["tsr_hours"].notna()) &
    (component_life_df["tsr_hours"] > component_life_df["tsn_hours"])
]

cycles = component_life_df[
    (component_life_df["tsr_cycles"].notna()) &
    (component_life_df["tsr_cycles"] > component_life_df["tsn_cycles"])
]

months = component_life_df[
    (component_life_df["tsr_mos"].notna()) &
    (component_life_df["tsr_mos"] > component_life_df["tsn_mos"])
]

if len(hours):
    raise ValueError("TSR Hours > TSN Hours")

if len(cycles):
    raise ValueError("TSR Cycles > TSN Cycles")

if len(months):
    raise ValueError("TSR MOS > TSN MOS")

# ----------------------------------------------------------
# Negative values
# ----------------------------------------------------------

life_columns = [
    "tsn_hours",
    "tsn_cycles",
    "tsn_mos",
    "tso_hours",
    "tso_cycles",
    "tso_mos",
    "tsr_hours",
    "tsr_cycles",
    "tsr_mos"
]

for col in life_columns:

    if col in component_life_df.columns:

        invalid = component_life_df[
            component_life_df[col].fillna(0) < 0
        ]

        if len(invalid):

            raise ValueError(
                f"Negative values detected in {col}"
            )

# ==========================================================
# SUMMARY
# ==========================================================

print("=" * 60)
print("FACT COMPONENT LIFE VALIDATION COMPLETE")
print("=" * 60)

print(f"Rows : {len(component_life_df):,}")

print(
    f"Unique Components : "
    f"{component_life_df['component_serial_number'].nunique():,}"
)

print(
    f"Unique Engines : "
    f"{component_life_df['engine_serial_number'].nunique():,}"
)

print("=" * 60)

component_life_df.groupby(
    ["component_id", "component_serial_number"]
)
