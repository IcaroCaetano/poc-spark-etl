# 🧩 What is Apache Spark?
Apache Spark is a distributed processing framework that allows you to manipulate large amounts of data in memory, quickly and scalably. In the context of this POC, Spark is used as the main ETL processing engine—that is, it reads CSV/JSON files, applies transformations, and writes the processed output.

## 📦 Initial project structure

````
poc-spark-etl/
│
├── data/
│   ├── input/
│   │   └── sample_data.csv
│   └── output/
│
├── src/
│   ├── main/
│   │   ├── python/
│   │   │   ├── etl_job.py
│   │   │   └── utils/
│   │   │       └── spark_session.py
│   │   │
│   │   └── scala/
│   │       └── com/projecticaro/etl/
│   │           └── ETLJob.scala
├── build.sbt              
├── requirements.txt        
└── README.md
````

## ⚙️ Local Installation and Execution

### 🔹 Prerequisites

- Windows 11

- Java 17 (installed and configured)

- Python 3.13+

- pip installed

Check with:

### 🔹 1. Clone the repository

````
git clone https://github.com/IcaroCaetano/poc-spark-etl.git
cd poc-spark-etl
````

### 🔹 2. Create and activate the virtual environment (optional, but recommended)

````
python -m venv venv
venv\Scripts\activate
````

### 🔹 3. Install dependencies

````
pip install -r requirements.txt
Contents of requirements.txt:

pyspark
pandas
pyarrow
````

### 🔹 4. Run the ETL locally

#### ▶️ Python (PySpark)
````
py -m src.main.etl_job
````

#### ▶️ Scala (native Spark)

Using sbt (you can install it with Chocolatey: choco install sbt)
````
cd poc-spark-etl
sbt "runMain com.projecticaro.etl.ETLJob"
````

 ✅ If everything is configured correctly, Spark will start and process the file data/input/sample_data.csv, generating clean output in data/output/cleaned_data.parquet.

### 🔍 What is Apache Spark in the context of your project?

Apache Spark is the distributed processing engine responsible for executing your ETL code in parallel.

In the project, you don't run Spark directly: you interact with it through PySpark, the official Spark Python API.

### 👉 PySpark acts as a bridge between Python and the Spark core (written in Scala/Java).

When you run the script:

````
py src/main/etl_job.py
````

PySpark:

1 - Initializes the Apache Spark engine within the JVM (Java Virtual Machine).

2 - Creates a SparkContext that coordinates the processing.

3 - Executes transformations and actions in parallel, even in local mode.

### ⚡ Where Spark "enters" your code
Spark is initialized when you create a SparkSession, as in the snippet below:

````
from pyspark.sql import SparkSession

spark = (
SparkSession.builder

.appName("ETLExample")

.master("local[*]")

.getOrCreate()

)
````

- appName("ETLExample"): Name of the Spark application.

- master("local[*]"): Uses all available CPU cores as Spark "executors".

- getOrCreate(): Initializes Spark locally.

From then on, all operations (such as spark.read.csv(), df.write.parquet(), etc.) are executed by the Apache Spark distributed engine, not by pure Python.

### 🧩 Example of how Spark is processing your data
Excerpt from etl_job.py:

````
df = spark.read.option("header", True).csv("data/input/sample_data.csv")
df_clean = df.na.drop().dropDuplicates()
df_clean.write.mode("overwrite").parquet("data/output/cleaned_data.parquet")
````

### ✨ What Spark does:

- Extraction: reads CSV files in parallel.

- Transformation: executes operations (na.drop, dropDuplicates) across multiple CPU cores.

- Loading: saves the result as Parquet in distributed mode.

Even on your computer, Spark simulates a local cluster environment, executing tasks in parallel.

## 🧠 Where Spark “lives” in your environment
By installing PySpark with:

````
pip install pyspark
````

It installs the complete Apache Spark within your Python installation, typically located at:

````
C:\Users\<your-username>\AppData\Local\Programs\Python\Python313\Lib\site-packages\pyspark\
````

In other words, you already have Spark working within your Python environment—no need to download the binary separately to run locally.

### 🧩 Visual Summary

````
Python script (etl_job.py)
↓
PySpark API (pyspark.sql, pyspark.ml, etc.)
↓
SparkSession → initializes the Apache Spark engine
↓
Spark executes transformations (RDD/DataFrame) in the JVM
↓
Results saved to Parquet/CSV/DB, etc.
````

## 💾 Example of input data

File: data/input/sample_data.csv

````
id,name,age,city
1,Ana,25,São Paulo
2,Bruno,30,Rio de Janeiro
3,Carlos,28,Belo Horizonte
4,Ana,25,São Paulo
5,,27,Curitiba
````

After execution, Spark will:

- Remove duplicate records.

- Remove rows with null values.

- Save the clean output as Parquet in data/output/cleaned_data.parquet.
