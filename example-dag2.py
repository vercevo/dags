from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

# Default args applied to all tasks unless overridden
default_args = {
    "owner": "tobbe",
    "depends_on_past": False,
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

# Define the DAG
with DAG(
    "example_dag2",
    default_args=default_args,
    description="A simple test DAG",
    schedule_interval=timedelta(days=1),  # run once per day
    start_date=datetime(2025, 1, 1),
    catchup=False,
    tags=["example"],
) as dag:

    # Define tasks
    t1 = BashOperator(
        task_id="print_date",
        bash_command="date"
    )

    t2 = BashOperator(
        task_id="say_hello",
        bash_command="echo 'Hello from Raspberry Pi Airflow!'"
    )

    # Task pipeline (t1 >> t2 means run t1 first, then t2)
    t1 >> t2
