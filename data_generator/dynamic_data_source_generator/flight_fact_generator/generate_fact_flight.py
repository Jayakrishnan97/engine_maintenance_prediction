import pandas as pd

from loaders import load_data
from schedule import generate_flight_schedule
from engine_assignment import build_engine_map
from fact_builder import build_fact_table
from config import NUM_FLIGHTS

def main():

    data = load_data()

    engine_map = build_engine_map(data["installation"])

    schedule_df = generate_flight_schedule(
        NUM_FLIGHTS,
        data["route"]
    )

    fact_df = build_fact_table(
        schedule_df,
        data["aircraft"],
        engine_map
    )

    # reorder columns
    fact_df = fact_df[[
        "flight_id",
        "flight_date",
        "aircraft_registration",
        "route_id",
        "origin",
        "destination",
        "left_engine_serial_number",
        "right_engine_serial_number",
        "scheduled_departure",
        "actual_departure",
        "scheduled_arrival",
        "actual_arrival",
        "flight_duration_min",
        "block_hours",
        "air_hours",
        "flight_cycles",
        "weather",
        "delay_minutes",
        "flight_status"
    ]]

    fact_df.to_csv("/home/jay/Python_DSA/python/projects/engine_maintenance_prediction/data_source/dynamic_datasource/fact_flight.csv", index=False)

    print("fact_flight.csv generated successfully with", len(fact_df), "rows")

if __name__ == "__main__":
    main()