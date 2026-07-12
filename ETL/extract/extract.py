from pathlib import Path
import pandas as pd


BASE_DIR = Path("/home/jay/Python_DSA/python/projects/engine_maintenance_prediction/data_source")

dynamic_dir = BASE_DIR / "dynamic_datasource"

static_dir = BASE_DIR / "static_datasource"

#static directory

dim_aircraft_df = pd.read_csv(static_dir / "dim_aircraft.csv")
dim_engine_df = pd.read_csv(static_dir / "dim_engine.csv")
dim_airport_df = pd.read_csv(static_dir / "dim_airports.csv")
dim_routes_df = pd.read_csv(static_dir / "dim_routes.csv")
dim_engine_component_df = pd.read_csv(static_dir / "dim_engine_component.csv")

#dynamic directory


initial_engine_component_inventory_df = pd.read_csv(dynamic_dir / "engine_component_inventory.csv")
initial_engine_installation_df = pd.read_csv(dynamic_dir / "engine_installation.csv")

fact_component_life_df = pd.read_csv(dynamic_dir / "fact_component_life.csv")
fact_engine_removal_df = pd.read_csv(dynamic_dir / "fact_engine_removal.csv")
fact_engine_utilization_df = pd.read_csv(dynamic_dir / "fact_engine_utilization.csv")
fact_fault_event_df = pd.read_csv(dynamic_dir / "fact_fault_event.csv")
fact_flight_df = pd.read_csv(dynamic_dir / "fact_flight.csv")
fact_maintenance_event_df = pd.read_csv(dynamic_dir / "fact_maintenance_event.csv")
fact_shop_visit_df = pd.read_csv(dynamic_dir / "fact_shop_visit.csv")
fact_work_order_df =  pd.read_csv(dynamic_dir / "fact_work_order.csv")


