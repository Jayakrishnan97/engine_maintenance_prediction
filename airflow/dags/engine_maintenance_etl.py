from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator

def test_etl_import():
	from ETL.extract.extract import fact_engine_removal_df

	print("Etl import successful")
	print(f"rows: {len(fact_engine_removal_df)}")


with DAG(
	dag_id = "engine_maintenance_etl",
	start_date=datetime(2026,1,1),
	schedule=None,
	catchup=False,
	tags=['engine-maintenance','etl'],
)as dag:
	test_import = PythonOperator(
	task_id = "test_etl_import",
	python_callable = test_etl_import,
)


