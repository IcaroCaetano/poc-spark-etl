from pyspark import SparkConf
from pyspark.sql import SparkSession

# This function creates and configures a Spark session named "SparkETL" (by default).
# It runs Spark locally using all CPU cores (local[*]) and sets Java options needed for compatibility.
# Finally, it returns the created Spark session to be used in the ETL process.
def create_spark_session(app_name: str = "SparkETL"):
    conf = (
        SparkConf()
        .setAppName(app_name)
        .setMaster("local[*]")
        .set("spark.driver.extraJavaOptions", "--add-opens=java.base/javax.security.auth=ALL-UNNAMED")
        .set("spark.executor.extraJavaOptions", "--add-opens=java.base/javax.security.auth=ALL-UNNAMED")
    )
    return SparkSession.builder.config(conf=conf).getOrCreate()
