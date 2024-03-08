from __future__ import annotations
import os
import sys
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.operators.dummy import DummyOperator

dag = DAG(
    dag_id="aaa",
    description="",
    start_date=datetime.now(),
    schedule="@once",
    catchup=False,
)

task1 = DummyOperator(
    task_id="task1",
    dag=dag,
)

task_init_schema = PostgresOperator(
    task_id="init_schema",
    postgres_conn_id="postgres_conn",
    sql="""
    CREATE TABLE IF NOT EXISTS pet (
    pet_id SERIAL PRIMARY KEY,
    name VARCHAR NOT NULL,
    pet_type VARCHAR NOT NULL,
    birth_date DATE NOT NULL,
    OWNER VARCHAR NOT NULL);
    """,
)

# Définir la dépendance entre les tâches
task1 >> task_init_schema
