from airflow.models import DAG
from datetime import datetime
from airflow.providers.sqlite.operators.sqlite import SqliteOperator


default_args = {
    'start_date': datetime(2020, 1, 1)
}

with DAG('user_processing',
        default_args = default_args,
        schedule_interval = '@daily',
        catchup = False
        ) as dag:
    
    creating_table = SqliteOperator(
        task_id = 'creating_table',
        sqlite_conn_id = 'db_sqlite',
        sql = '''
            CREATE TABLE users (
                firstname TEXT NOT NULL,
                lastname TEXT NOT NULL,
                country TEXT NOT NULL,
                username TEXT NOT NULL,
                password TEXT NOT NULL,
                email TEXT NOT NULL PRIMARY KEY
            );
        '''
    )

creating_table