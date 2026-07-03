import pandas as pd
import numpy as np

from weather import generate_weather, generate_delay, generate_status
from engine_assignment import assign_engines

def build_fact_table(schedule_df, aircraft_df, engine_map):

    n = len(schedule_df)

    # assign aircraft randomly (vectorized)
    aircraft_sample = aircraft_df.sample(n=n, replace=True).reset_index(drop=True)

    schedule_df["aircraft_registration"] = aircraft_sample["aircraft_registration"].values

    # engine assignment
    schedule_df = assign_engines(schedule_df, engine_map)

    # weather + delay + status
    schedule_df["weather"] = generate_weather(n)
    schedule_df["delay_minutes"] = generate_delay(n)
    schedule_df["flight_status"] = generate_status(n)

    # actual times
    schedule_df["actual_departure"] = schedule_df["scheduled_departure"] + \
        pd.to_timedelta(schedule_df["delay_minutes"], unit="m")

    schedule_df["actual_arrival"] = schedule_df["scheduled_arrival"] + \
        pd.to_timedelta(schedule_df["delay_minutes"], unit="m")

    # derived metrics
    schedule_df["block_hours"] = (
        (schedule_df["actual_arrival"] - schedule_df["actual_departure"])
        .dt.total_seconds() / 3600
    )

    schedule_df["air_hours"] = schedule_df["flight_duration_min"] / 60

    schedule_df["flight_cycles"] = 1

    schedule_df["flight_id"] = np.arange(1, n + 1)

    return schedule_df