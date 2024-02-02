from __future__ import annotations
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator


# Définir les arguments par défaut du DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Créer une instance de DAG
dag = DAG(
    'hello_world_dag',
    default_args=default_args,
    description='Un simple DAG qui imprime Hello World',
    schedule_interval=timedelta(days=1),  # Planification quotidienne
)

# Tâche 1 : Imprimer "Hello"
def print_hello():
    print("Hello")

task_hello = PythonOperator(
    task_id='print_hello',
    python_callable=print_hello,
    dag=dag,
)

# Tâche 2 : Imprimer "World"
def print_world():
    print("World")

task_world = PythonOperator(
    task_id='print_world',
    python_callable=print_world,
    dag=dag,
)

# Définir la dépendance entre les tâches
task_hello >> task_world
