from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash_operator import BashOperator
from datetime import datetime
from airflow.providers.postgres.operators.postgres import PostgresOperator
from great_expectations_provider.operators.great_expectations import GreatExpectationsOperator
import os

def load_to_production_db(ts, **kwargs):
    """
    This is just a stub for an optional Python task that loads the output of the dbt pipeline
    to a production database or data warehouse for further consumption
    """
    print('Loading analytical_output output to production database.')
    print('Done.')

# Default settings applied to all tasks
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 1, 1)
}

# These could be set with environment variables
POSTGRES_CONN_ID = "postgres_default"
PROJECT_HOME = '/home/syauqikhosyi/airflow/'
GE_ROOT_DIR = os.path.join(PROJECT_HOME, 'gx')
GE_TARGET_DIR = os.path.join(GE_ROOT_DIR, 'uncommitted', 'data_docs')

dag = DAG(
    dag_id='payments_ge',
    schedule_interval=None,
    default_args=default_args
)

# This first step validates the source data files and only proceeds with loading
# if they pass validation with Great Expectations
validate_source_data = GreatExpectationsOperator(
    task_id='validate_source_data',
    conn_id=POSTGRES_CONN_ID,  
    data_context_root_dir=GE_ROOT_DIR,
    data_asset_name='payments',
    expectation_suite_name='my_payments_postgres_great_expectations',
    dag=dag
)

'''# This first step validates the source data files and only proceeds with loading
# if they pass validation with Great Expectations
validate_source_data = GreatExpectationsOperator(
    task_id='validate_source_data',
    assets_to_validate = [
        {
            'batch_kwargs': {
                'path': os.path.join(PROJECT_HOME, 'data', '...db'),
                'datasource': 'pg_datasource'
            },
            'expectation_suite_name': 'payments.my_payments_postgres_great_expectations'
        },        
    ],
    data_context_root_dir=GE_ROOT_DIR,
    dag=dag
)'''

'''# This step validates that the load is correct. I'm re-using the same
# Expectation Suite as for the source data load, but could use a different one,
# e.g. to account for different casing or datatypes of columns
validate_load = GreatExpectationsOperator(
    task_id='validate_load',
    assets_to_validate=[
        {
            'batch_kwargs': {
                'datasource': 'pg_datasource',
                'table': 'payments',
                'data_asset_name': 'payments'
            },
            'expectation_suite_name': 'payments.my_payments_postgres_great_expectations'
        },
    ],
    data_context_root_dir=GE_ROOT_DIR,
    dag=dag
)'''

'''# This step validates the final transformation output. This could also be done
# with dbt, but I'm using Great Expectations for the sake of this demo.
validate_transform = GreatExpectationsOperator(
    task_id='validate_transform',
    expectation_suite_name='analytical_output.final',
    batch_kwargs={
        'datasource': 'postgres_astro',
        'table': 'pickup_dropoff_borough_counts',
        'data_asset_name': 'pickup_dropoff_borough_counts'
    },
    data_context_root_dir=GE_ROOT_DIR,
    dag=dag
)'''

'''# This task re-builds the Great Expectations docs
ge_docs_generate = BashOperator(
    task_id='ge_docs_generate',
    bash_command=f'great_expectations docs build --directory {GE_ROOT_DIR} --assume-yes',
    dag=dag
)'''

'''# This task copies the Great Expectations docs to the include directory that's mapped to my local volume
# so I can open them locally. In production, I'd upload this to an S3 bucket!
ge_docs_copy = BashOperator(
    task_id='ge_docs_copy',
    bash_command=f'mkdir {GE_DOCS_DIR}; \
    cp -r {GE_TARGET_DIR} {GE_DOCS_DIR}',
    dag=dag
)'''

load_to_prod = PythonOperator(
    task_id='load_to_prod',
    python_callable=load_to_production_db,
    dag=dag
)

'''validate_source_data >> dbt_seed >> validate_load >> dbt_run >> validate_transform
validate_transform >> [dbt_docs_generate, ge_docs_generate]
dbt_docs_generate >> dbt_docs_copy
ge_docs_generate >> ge_docs_copy
[dbt_docs_copy, ge_docs_copy] >> load_to_prod'''

validate_source_data >> load_to_prod