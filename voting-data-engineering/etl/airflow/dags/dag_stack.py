'''# Import libraries for Airflow, dbt, and Great Expectations
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash_operator import BashOperator
from datetime import datetime
from airflow_dbt.operators.dbt_operator import DbtSeedOperator, DbtRunOperator
from great_expectations_provider.operators.great_expectations import GreatExpectationsOperator
import os

# Default settings applied to all tasks
default_args = {
    'owner' : 'airflow',
    'start_date' : datetime(2023, 1, 1)
}

# Set the environment variables
PROJECT_HOME = '/usr/local/airflow'
DBT_PROJECT_DIR = os.path.join(PROJECT_HOME, 'dbt')
DBT_TARGET_DIR = os.path.join(DBT_PROJECT_DIR, 'target')
DBT_DOCS_DIR = os.path.join(PROJECT_HOME, 'include', 'dbt_docs')
GE_ROOT_DIR = os.path.join(PROJECT_HOME, 'great_expectations')
GE_TARGET_DIR = os.path.join(GE_ROOT_DIR, 'uncommitted', 'data_docs')
GE_DOCS_DIR = os.path.join(PROJECT_HOME, 'include', 'great_expectations_docs')

# Set the dag
dag = DAG(
    dag_id='dag_stack',
    schedule_interval=None,
    catchup=False, 
    default_args=default_args
)

# Task
# Validate Source Data
validate_source_data = GreatExpectationsOperator(
    task_id='validate_source_data',
    data_context_root_dir=GE_ROOT_DIR,
    data_asset_name='voting',
    expectation_suite_name='voting_suite',
    dag=dag,
     assets_to_validate = [
        {
            'batch_kwargs': {
                'path': os.path.join(PROJECT_HOME, 'data', 'taxi_zone_lookup.csv'),
                'datasource': 'data_dir'
            },
            'expectation_suite_name': 'taxi_zone.source'
        },
        {
            'batch_kwargs': {
                'path': os.path.join(PROJECT_HOME, 'data', 'yellow_tripdata_sample_2019-01.csv'),
                'datasource': 'data_dir'
            },
            'expectation_suite_name': 'taxi_trips.source'
        },
    ]
)'''