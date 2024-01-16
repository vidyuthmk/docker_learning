'''
This dag is to check if requirment.txt can install packages into the docker image  

'''
from datetime import datetime, timedelta

from airflow.models.dag import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

default_args={
        "owner": 'Vidyadhar',
        "retries": 2,
        "retry_delay": timedelta(minutes=5)
    }
CONFIG ={ 'name' : 'vidyahar'}


with DAG(
    dag_id="my_first_dag",
    start_date=datetime(2022,7,28),
    schedule=timedelta(minutes=30),
    catchup=False,
    tags=["tutorial"],
    default_args=default_args
):
    t1 = BashOperator(
    task_id="say_my_name",
    bash_command=f"echo {CONFIG.name}"
)