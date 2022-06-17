from airflow import DAG
from airflow.operators.python import PythonOperator

from datetime import datetime, timedelta
#from minio_pipe_fraud import BlockFraudPipe
from pyspark_pipe_fraud import BlockFraudPipe

pipeline = BlockFraudPipe(['buckets'])

DEFAULT_ARGS = {
    'retries': 2,
    'owner':'airflow',
    'email_on_retry': False,
    'depends_on_past': False,
    'email_on_failure': False,
    'start_date':  datetime(2022, 6, 13),
    'retry_delay': timedelta(minutes=5)
}

dag = DAG(
    'BlockerFraudClassification',
    description="Blocker Fraud Company Classification DAG",
    catchup=False,
    default_args=DEFAULT_ARGS,
    schedule_interval=timedelta(days=1)    
)

# Jobs Definition

create_bucket_task = PythonOperator(
    task_id='create_buckets',
    python_callable=pipeline.create_buckets,
    op_args=['fraudlake'],
    dag=dag
)

data_collect_task = PythonOperator(
    task_id="collect_raw_data",
    python_callable=pipeline.data_collect,
    provide_context=True,
    dag=dag
)

api_request_task = PythonOperator(
    task_id="model_api_request",
    python_callable=pipeline.api_request,
    provide_context=True,
    dag=dag
)

store_dataset_task = PythonOperator(
    task_id="store_dataset_on_s3",
    python_callable=pipeline.store_dataset_fraud,
    dag=dag
)

create_bucket_task >> data_collect_task >> api_request_task >> store_dataset_task