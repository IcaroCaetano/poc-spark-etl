from src.utils.spark_session import create_spark_session

def main():
    spark = create_spark_session("ETLExample")

    # 1️⃣ Extração: ler CSV
    df = spark.read.option("header", True).csv("data/input/sample_data.csv")

    # 2️⃣ Transformação: limpar e manipular dados
    df_clean = df.na.drop().dropDuplicates()

    # 3️⃣ Carga: salvar resultado como Parquet
    df_clean.write.mode("overwrite").parquet("data/output/cleaned_data.parquet")

    print("✅ ETL concluído com sucesso!")
    spark.stop()

if __name__ == "__main__":
    main()

