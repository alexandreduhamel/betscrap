from __future__ import annotations
import os
import sys
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from retreive_data.winamax import *


# Define DAG args
default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2023, 1, 1),
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

# Créer une instance de DAG
dag = DAG(
    "dag_scrap_winamax",
    default_args=default_args,
    description="",
    schedule_interval=timedelta(days=1),  # daily
)


# Tâche 1 : Imprimer "Hello"
def print_hello():
    print("Hello")


task_hello = PythonOperator(
    task_id="print_hello",
    python_callable=print_hello,
    dag=dag,
)


# Tâche 2 : Imprimer "World"
def print_world():
    print("World")


task_world = PythonOperator(
    task_id="print_world",
    python_callable=print_world,
    dag=dag,
)

# Définir la dépendance entre les tâches
task_hello >> task_world
