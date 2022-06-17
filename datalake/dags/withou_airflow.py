import os
import json
import logging
import requests

from sqlalchemy import create_engine
from datetime import datetime, timedelta
from pandas import read_sql_query, DataFrame

from minio import Minio
from utils import getInfos, BasePipeline

from pyspark.sql import SparkSession
from pyspark.sql import functions as psf


BASE_DIR = os.path.join(os.path.abspath('.'))
#JARS_DIR = os.path.join(BASE_DIR, 'jars')
DATETIME_REQUEST = datetime.now().strftime('%Y_%m_%d')

client = Minio(
    endpoint=getInfos().MINIO_HOST, #Without HTTP://
    access_key=getInfos().ACCESS_KEY,
    secret_key=getInfos().SECRET_KEY,
    secure=False
)

spark = (
    SparkSession
    .builder
    .appName('pipeline')
    .config('fs.s3a.endpoint', getInfos().MINIO_ENDPOINT)
    .config('fs.s3a.buffer.dir', 's3a://fraudlake/pyspark')
    .config('fs.s3a.fast.upload.buffer', 'bytebuffer')
    .config('fs.s3a.fast.upload.active.blocks', 1)
    .config('fs.s3a.access.key', 'minioadmin')
    .config('fs.s3a.secret.key', 'minioadmin')
    .config("fs.s3a.impl","org.apache.hadoop.fs.s3a.S3AFileSystem")
    .config("fs.s3a.path.style.access", "True")
   # .config('spark.jars', os.path.join(JARS_DIR, 'postgresql-42.3.2.jar'))
    .getOrCreate()
)

class BlockFraudPipe(BasePipeline):
    def __init__(self, tables: list):
        self.__tables = tables
        self.url = "https://blk-frd-api-new.herokuapp.com/predict"
        self.hdr = {"Content-type": "application/json"}


    def create_buckets(self, *args):
        for bucket in args:
            if not client.bucket_exists(bucket):
                client.make_bucket(bucket)
        return -1


    def data_collect(self):
        try:
            os.system(f"rm fraud_file_backup_{(datetime.now() - timedelta(days=1)).strftime('%Y_%m_%d')}.csv")
        except:
            print("Do Not Have Old CSV File to DELETE")

        db = create_engine(f"postgresql://{getInfos().H_DB_USER}:{getInfos().H_DB_PASS}@{getInfos().H_DB_HOST}:{getInfos().H_DB_PORT}/{getInfos().H_DB}")
        con = db.connect()

        df_raw = read_sql_query('select * from transactions', con=con)

        con.close()

        df_raw = json.dumps(df_raw.to_dict(orient='records'))

        return df_raw


    def api_request(self, data):
        try:
            r = requests.post(self.url, headers=self.hdr, data=data)
        except ValueError:
            print(f'[ERROR] Request on API at: {DATETIME_REQUEST}')

        if r.status_code == 200:
            df_fraud = DataFrame(r.json())
            df_fraud.to_csv(f'data_backup/fraud_file_backup_{DATETIME_REQUEST}.csv', index=False)
        
        else:
            print(f"\nStatus Code: {r.status_code}")


    def store_dataset_fraud(self):

        df = spark.read.format('csv').option('header', 'true').load(f'data_backup/fraud_file_backup_{DATETIME_REQUEST}.csv')

        df = df.withColumn('created_at', 
                           psf.date_format(
                            psf.current_timestamp(), 
                            'yyyy_MM_dd-HH_mm_ss'))
        try:
            df.write.format('parquet')\
                    .mode('overwrite')\
                    .partitionBy('created_at')\
                    .save('s3a://fraudlake/pyspark')
                    
        except ValueError:
            print(f'[ERROR] Cannot Store Spark Parquet on S3 Bucket at: {DATETIME_REQUEST}')
                

if __name__ == '__main__':

    if not os.path.exists('logs'):
        os.makedirs('logs')

    logging.basicConfig(level=logging.INFO,
                        datefmt='%Y-%m-%d %H:%M:%S',
                        filename='logs/geral_logs_fraud_etl.txt',
                        format='%(asctime)s - %(levelname)s - %(name)s - %(message)s',)

    logger = logging.getLogger('FraudETL')

    pipeline = BlockFraudPipe(['buckets'])

    pipeline.create_buckets('fraudlake')
    logger.info(f'[OK] Job ( Create Buckets ) Success!')    

    d = pipeline.data_collect()
    logger.info(f'[OK] Job ( Data Collect ) Success!')

    pipeline.api_request(d)
    logger.info(f'[OK] Job ( Api Request ) Success!')

    pipeline.store_dataset_fraud()
    logger.info(f'[OK] Job ( Dataset Store at S3 ) Success!')