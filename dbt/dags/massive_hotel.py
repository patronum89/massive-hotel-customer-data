from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator

# Define the dbt run command
dbt_run_command = 'dbt run --profiles-dir E:/Code/massive-hotel-customer-data/dbt/profiles.yml --project-dir E:/Code/massive-hotel-customer-data/dbt/dbt_project.yml'

DBT_ENV = {
    "DBT_USER": "{{ conn.postgres.login }}",
    "DBT_ENV_SECRET_PASSWORD": "{{ conn.postgres.password }}",
    "DBT_HOST": "{{ conn.postgres.host }}",
    "DBT_SCHEMA": "{{ conn.postgres.schema }}",
    "DBT_PORT": "{{ conn.postgres.port }}",
}

# Define the intervals at which you want to run dbt models
run_intervals = ['0 6 * * *', '0 14 * * *', '0 18 * * *']  # 6 AM, 14 PM, and 18 PM UTC

default_args={
            'owner': 'dbt_user',
            'start_date': datetime(2023, 12, 31),
            'retries': 1,
            'retry_delay': timedelta(minutes=5),
        }

list_of_dags = []

def create_dag(dag_id, schedule, default_args , task_id):
    dag = DAG(
        dag_id,
        schedule_interval=schedule,
        default_args=default_args)
    with dag:
        task = BashOperator(task_id=task_id,
                            bash_command=dbt_run_command,
                            dag=dag)
    return dag

# Instantiate a DAG for each interval
for interval in run_intervals:
    dag_id = f'dbt_daily_dag_{interval.split(" ")[0]}_{interval.split(" ")[1]}'  # Unique DAG ID
    task_id = f'run_dbt_models_{interval.split(" ")[0]}_{interval.split(" ")[1]}'  #Unique task ID
    list_of_dags.append((dag_id , interval , task_id))

for dag_item in list_of_dags:
    dag_id = dag_item[0]
    dag_schedule = dag_item[1]
    task_id = dag_item[2]
    globals()[dag_id] = create_dag(
        dag_id,
        dag_schedule,
        default_args,
        task_id
    )



# # Instantiate a BashOperator to run dbt models
# run_dbt = BashOperator(
#     task_id=f'run_dbt_models_{interval.split(" ")[0]}_{interval.split(" ")[1]}',
#     bash_command=dbt_run_command,
#     dag=dag,
#     env = DBT_ENV,
# )
