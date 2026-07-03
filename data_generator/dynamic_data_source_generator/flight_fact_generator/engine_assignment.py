import pandas as pd

def build_engine_map(installation_df):
    # vectorized grouping instead of loops
    grouped = installation_df.groupby("aircraft_registration")[
        "engine_serial_number"
    ].apply(list).to_dict()

    return grouped


def assign_engines(df, engine_map):
    # vectorized apply (fast enough for 25k)
    left_engines = []
    right_engines = []

    for reg in df["aircraft_registration"]:
        engines = engine_map.get(reg, [None, None])

        left_engines.append(engines[0] if len(engines) > 0 else None)
        right_engines.append(engines[1] if len(engines) > 1 else None)

    df["left_engine_serial_number"] = left_engines
    df["right_engine_serial_number"] = right_engines

    return df