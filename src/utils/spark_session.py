from pyspark.sql import SparkSession

def create_spark_session(app_name: str = "SparkETL"):
    spark = (
        SparkSession.builder
        .appName(app_name)
        .master("local[*]")
        .config("spark.sql.shuffle.partitions", "2")
        .getOrCreate()
    )
    return spark
