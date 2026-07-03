import pandas as pd

aircraft = pd.read_csv("/home/jay/Python_DSA/python/projects/engine_maintenance_prediction/data_source/dim_aircraft.csv")

engine = pd.read_csv("/home/jay/Python_DSA/python/projects/engine_maintenance_prediction/data_source/dim_engine.csv")


installed_engines = engine[engine["engine_status"] == "INSTALLED"].reset_index(drop=True)

active_aircraft = aircraft[aircraft["aircraft_status"].isin(["ACTIVE", "MAINTENANCE"])].reset_index(drop=True)

installation = []

installation_id = 1

for i in range(len(active_aircraft)):
    reg = active_aircraft.loc[i, "aircraft_registration"]

    left = installed_engines.loc[2*i, "engine_serial_number"]
    right = installed_engines.loc[2*i+1, "engine_serial_number"]

    installation.append({
        "installation_id": installation_id,
        "aircraft_registration": reg,
        "engine_serial_number": left,
        "engine_position": "ENG1"
    })

    installation_id += 1

    installation.append({
        "installation_id": installation_id,
        "aircraft_registration": reg,
        "engine_serial_number":right,
        "engine_position": "ENG2"
    })

    installation_id += 1

installation_df = pd.DataFrame(installation)

installation_df.to_csv("/home/jay/Python_DSA/python/projects/engine_maintenance_prediction/data_source/engine_installation.csv", index = False)


