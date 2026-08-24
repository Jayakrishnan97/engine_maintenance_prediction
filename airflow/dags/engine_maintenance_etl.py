import sys
from pathlib import Path

PROJECT_ROOT = Path("/home/jay/Python_DSA/python/projects/engine_maintenance_prediction")
sys.path.insert(0, str(PROJECT_ROOT))


from datetime import datetime

from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator

from ETL.transform.dimension_df import transform_all_dimensions

from ETL.load.dimension_load import load_all_dimensions
from ETL.load.fact_load import load_all_facts

with DAG(
	dag_id = "engine_maintenance_etl",
	start_date=datetime(2026,1,1),
	schedule=None,
	catchup=False,
)as dag:

	transform_dimension = PythonOperator(
		task_id ="dimension_transform",
		python_callable=transform_all_dimensions,
	)
	load_dimensions = PythonOperator(
		task_id = "dimension_table_load",
		python_callable = load_all_dimensions,
	)
	load_facts = PythonOperator(
		task_id = "fact_table_load",
		python_callable=load_all_facts,
	)

	transform_dimension >> load_dimensions >> load_facts

