from pyspark.sql import SparkSession

def get_database():
    spark = (
        SparkSession
        .builder
        .appName('pipeline')
        .config('fs.s3a.endpoint', 'http://192.168.101.3:9000')
        .config('fs.s3a.access.key', 'gabriel')
        .config('fs.s3a.secret.key', '12345678')
        .config("fs.s3a.impl","org.apache.hadoop.fs.s3a.S3AFileSystem")
        .config("fs.s3a.path.style.access", "True")
        .getOrCreate()
    )

    data = (
        spark.read
        .format('parquet')
        .load('s3a://fraudlake/pyspark')
        .drop('created_at')
        .toPandas()
    )
    
    return data