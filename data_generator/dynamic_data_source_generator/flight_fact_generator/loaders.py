import pandas as pd

def load_data():
    dim_engine = pd.read_csv("/home/jay/Python_DSA/python/projects/engine_maintenance_prediction/data_source/static_datasource/dim_engine.csv")
    dim_aircraft = pd.read_csv("/home/jay/Python_DSA/python/projects/engine_maintenance_prediction/data_source/static_datasource/dim_aircraft.csv")
    engine_installation = pd.read_csv("/home/jay/Python_DSA/python/projects/engine_maintenance_prediction/data_source/dynamic_datasource/engine_installation.csv")
    dim_airport = pd.read_csv("/home/jay/Python_DSA/python/projects/engine_maintenance_prediction/data_source/static_datasource/dim_airports.csv")
    dim_route = pd.read_csv("/home/jay/Python_DSA/python/projects/engine_maintenance_prediction/data_source/static_datasource/dim_routes.csv")

    # Keep only active aircraft
    dim_aircraft = dim_aircraft[
        dim_aircraft["aircraft_status"].str.upper() == "ACTIVE"
    ]

    return {
        "engine": dim_engine,
        "aircraft": dim_aircraft,
        "installation": engine_installation,
        "airport": dim_airport,
        "route": dim_route
    }