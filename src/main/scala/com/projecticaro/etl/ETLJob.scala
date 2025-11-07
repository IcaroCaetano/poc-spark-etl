package com.projecticaro.etl

import org.apache.spark.sql.SparkSession

object ETLJob {
  def main(args: Array[String]): Unit = {
    val spark = SparkSession.builder()
      .appName("ETLProjectIcaroScala")
      .master("local[*]")
      .config("spark.sql.shuffle.partitions", "2")
      .getOrCreate()

    // Extraction: read CSV
    val df = spark.read.option("header", true).csv("data/input/sample_data.csv")

    // Transformation: remove nulls and duplicates
    val dfClean = df.na.drop().dropDuplicates()

    // Load: save to Parquet
    dfClean.write.mode("overwrite").parquet("data/output/cleaned_data_scala.parquet")

    println("✅ ETL completed successfully (Scala)!")
    spark.stop()
  }
}
