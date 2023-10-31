from airflow import DAG # Import the DAG
from airflow.operators.python import PythonOperator, BranchPythonOperator # Import the Python Operator
from airflow.operators.bash import BashOperator # Import the BashOperator
from datetime import datetime # Import the Datetime

from random import randint # Import to generate random numbers

# Randomize the training model function
def _training_model():
    return randint(1, 10) # Return an integer between 1 - 10


# Return the whether the model accurate or not, based on threshold function
def _choose_best_model(ti):
    # XCOM is a mechanism allowing to exchange small data 
    # between the tasks of a DAG.
    accuracies = ti.xcom_pull(task_ids=[
        'training_model_A',
        'training_model_B',
        'training_model_C'
    ])

    # The best accuracy is a number of accuracy 
    # that have the highest accuracy compared to 2 tasks
    best_accuracy = max(accuracies)

    # If-else
    if (best_accuracy > 8):
        return 'accurate'
    return 'inaccurate'

with DAG(
    dag_id='my_dag', # Dag id,
    start_date=datetime(2023, 1, 1), # Start date of the dag is running (1 Jan 2023)
    schedule_interval='@daily', # The interval of time at which your DAG gets triggered (once every day)
    catchup=False # Prevent from backfilling automatically the non triggered DAG Runs 
    # between the start date of your DAG and the current date 
    # (Don’t want to end up with many DAG runs running at the same time)
) as dag:
    
    # Training Model Task
    # Option 1 : Copy each training model
    training_model_A = PythonOperator(
        task_id="training_model_A",
        python_callable=_training_model  # Call the function
    )

    training_model_B = PythonOperator(
        task_id="training_model_B",
        python_callable=_training_model  # Call the function
    ) 

    training_model_C = PythonOperator(
        task_id="training_model_C",
        python_callable=_training_model  # Call the function
    )

    # Option 2 : Much more simpler
    # training_model_tasks = [
    #    PythonOperator(
    #        task_id=f"training_model_{model_id}",
    #        python_callable=_training_model,
    #        op_kwargs={
    #            "model": model_id
    #        }
    #    )
    #    for model_id in ['A', 'B', 'C']
    #]


    # Choose Best Model Task
    choose_best_model = BranchPythonOperator(
        task_id="choose_best_model", 
        python_callable=_choose_best_model # Call the function
    )

    # Accurate Task
    accurate = BashOperator(
        task_id="accurate",
        bash_command="echo 'accurate" # Print 'accurate'
    )

    # Inaccurate Task
    inaccurate = BashOperator(
        task_id="inaccurate",
        bash_command="echo 'inaccurate" # Print 'inaccurate'
    )

    # Definining dependencies
    # Option 1 : Copy each training model
    [training_model_A, training_model_B, training_model_C] >> choose_best_model >> [accurate, inaccurate]

    # Option 2 : Much more simpler
    # training_model_tasks >> choose_best_model >> [accurate, inaccurate]