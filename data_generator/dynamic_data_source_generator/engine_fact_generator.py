import pandas as pd

# --------------------------
# Load Flight Data
# --------------------------

df = pd.read_csv("/home/jay/Python_DSA/python/projects/engine_maintenance_prediction/data_source/dynamic_datasource/fact_flight.csv")

# Keep only completed flights
df = df[df["flight_status"] == "COMPLETED"]

# Convert date
df["flight_date"] = pd.to_datetime(df["flight_date"])

# Sort flights
df = df.sort_values(
    ["flight_date", "aircraft_registration"]
)

# Running totals
engine_hours = {}
engine_cycles = {}

records = []

utilization_id = 1

# --------------------------
# Generate Utilization
# --------------------------

for _, row in df.iterrows():

    flight_id = row["flight_id"]
    flight_date = row["flight_date"]
    aircraft = row["aircraft_registration"]
    air_hours = row["air_hours"]
    cycles = row["flight_cycles"]

    left_engine = row["left_engine_serial_number"]
    right_engine = row["right_engine_serial_number"]

    for engine in [left_engine, right_engine]:

        if engine not in engine_hours:
            engine_hours[engine] = 0
            engine_cycles[engine] = 0

        engine_hours[engine] += air_hours
        engine_cycles[engine] += cycles

        records.append({
            "utilization_id": f"UTL{utilization_id:07d}",
            "utilization_date": flight_date.date(),
            "flight_id": flight_id,
            "engine_serial_number": engine,
            "aircraft_registration": aircraft,
            "flight_hours": round(air_hours, 2),
            "flight_cycles": cycles,
            "cumulative_engine_hours": round(engine_hours[engine], 2),
            "cumulative_engine_cycles": engine_cycles[engine],
            "engine_status": "INSTALLED"
        })

        utilization_id += 1

# --------------------------
# Save CSV
# --------------------------

util = pd.DataFrame(records)

util.to_csv(
    "/home/jay/Python_DSA/python/projects/engine_maintenance_prediction/data_source/dynamic_datasource/fact_engine_utilization.csv",
    index=False
)