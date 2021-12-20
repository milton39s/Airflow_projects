from airflow.models import DAG
from datetime import datetime


default_args = {
    'start_date': datetime(2020, 1, 1)
}

with DAG('user_processing',
        default_args=default_args,
        schedule_interval= '@daily',
        catchup = False
        ) as dag:
    # deine task
