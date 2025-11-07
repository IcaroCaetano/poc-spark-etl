from src.utils.spark_session import create_spark_session

def main():
    spark = create_spark_session("ETLExample")

    # Extraction: Read CSV
    df = spark.read.option("header", True).csv("data/input/sample_data.csv")

    # Cleans the data by removing any rows that contain null (missing) values and then removing duplicate rows.
    # df_clean will contain only unique and complete records with no missing data.
    # Transformation: cleaning and manipulating data
    df_clean = df.na.drop().dropDuplicates()

    # saves the cleaned data as a Parquet file in the folder data/output/cleaned_data.parquet.
    # The option "overwrite" means it will replace any existing file in that location.
    # Load: save result as Parquet
    df_clean.write.mode("overwrite").parquet("data/output/cleaned_data.parquet")

    print("✅ ETL completed successfully.!")
    spark.stop()

if __name__ == "__main__":
    main()

