import numpy as np
import pandas as pd
from datetime import datetime, timedelta

def generate_flight_schedule(n, routes_df):
    routes_sample = routes_df.sample(n=n, replace=True).reset_index(drop=True)

    base_date = datetime(2025, 1, 1)

    flight_dates = [
        base_date + timedelta(days=int(x))
        for x in np.random.randint(0, 365, n)
    ]

    scheduled_departure = [
        dt + timedelta(hours=int(np.random.randint(0, 24)))
        for dt in flight_dates
    ]

    duration = routes_sample["typical_duration_min"].values

    scheduled_arrival = [
        dep + timedelta(minutes=int(dur))
        for dep, dur in zip(scheduled_departure, duration)
    ]

    return pd.DataFrame({
        "route_id": routes_sample["route_id"],
        "origin": routes_sample["origin"],
        "destination": routes_sample["destination"],
        "flight_date": flight_dates,
        "scheduled_departure": scheduled_departure,
        "scheduled_arrival": scheduled_arrival,
        "flight_duration_min": duration
    })