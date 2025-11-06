from pyspark import SparkConf
from pyspark.sql import SparkSession

def create_spark_session(app_name: str = "SparkETL"):
    conf = (
        SparkConf()
        .setAppName(app_name)
        .setMaster("local[*]")
        .set("spark.driver.extraJavaOptions", "--add-opens=java.base/javax.security.auth=ALL-UNNAMED")
        .set("spark.executor.extraJavaOptions", "--add-opens=java.base/javax.security.auth=ALL-UNNAMED")
    )
    return SparkSession.builder.config(conf=conf).getOrCreate()
