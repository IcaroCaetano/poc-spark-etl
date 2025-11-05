from src.utils.spark_session import create_spark_session

def main():
    spark = create_spark_session("ETLExample")

    # Extraction: Read CSV
    df = spark.read.option("header", True).csv("data/input/sample_data.csv")

    # Transformation: cleaning and manipulating data
    df_clean = df.na.drop().dropDuplicates()

    # Load: save result as Parquet
    df_clean.write.mode("overwrite").parquet("data/output/cleaned_data.parquet")

    print("✅ ETL completed successfully.!")
    spark.stop()

if __name__ == "__main__":
    main()

