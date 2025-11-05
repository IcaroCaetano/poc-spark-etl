# 🧩 O que é o Apache Spark

O Apache Spark é um framework de processamento distribuído que permite manipular grandes quantidades de dados em memória, de forma rápida e escalável.
No contexto desta POC, o Spark é usado como motor principal de processamento ETL — ou seja, ele lê arquivos CSV/JSON, aplica transformações e grava a saída processada.

## 📦 Estrutura inicial do projeto

````
poc-spark-etl/
│
├── data/
│   ├── input/                    # Arquivos de entrada (CSV, JSON, etc.)
│   │   └── sample_data.csv
│   └── output/                   # Dados transformados gerados pelo Spark
│
├── src/
│   ├── main/
│   │   └── etl_job.py            # Script principal de ETL
│   └── utils/
│       └── spark_session.py      # Criação da SparkSession (inicialização do Spark)
│
├── notebooks/
│   └── exploratory.ipynb         # (Opcional) Análises exploratórias com Spark
│
├── requirements.txt              # Dependências Python
├── .gitignore
└── README.md
````

## ⚙️ Instalação e execução local
###🔹 Pré-requisitos

- Windows 11

- Java 17 (instalado e configurado)

- Python 3.13+

- pip instalado

Verifique com:

````
java -version
py --version
````

### 🔹 1. Clonar o repositório

````
git clone https://github.com/IcaroCaetano/poc-spark-etl.git
cd poc-spark-etl
````

### 🔹 2. Criar e ativar o ambiente virtual (opcional, mas recomendado)

````
python -m venv venv
venv\Scripts\activate
````

### 🔹 3. Instalar dependências

````
pip install -r requirements.txt
````

Conteúdo do requirements.txt:

````

pyspark
pandas
pyarrow
````

### 🔹 4. Rodar o ETL localmente

````
py src/main/etl_job.py
````

✅ Se tudo estiver configurado corretamente, o Spark iniciará e processará o arquivo data/input/sample_data.csv, gerando uma saída limpa em data/output/cleaned_data.parquet.

### 🔍 O que é o Apache Spark no contexto do seu projeto

O *Apache Spark* é o motor de processamento distribuído responsável por executar o seu código ETL em paralelo.

No projeto, você não executa o Spark diretamente: você interage com ele através do *PySpark*, a API Python oficial do Spark.

👉 O *PySpark atua como uma ponte* entre o Python e o núcleo do Spark (escrito em Scala/Java).

Quando você roda o script:

````
py src/main/etl_job.py
````

O PySpark:

1 - Inicializa o motor Apache Spark dentro da JVM (Java Virtual Machine).

2 - Cria um SparkContext que coordena o processamento.

3 - Executa as transformações e ações em paralelo, mesmo em modo local.

## ⚡ Onde o Spark “entra” no seu código
O Spark é inicializado quando você cria uma SparkSession, como no trecho abaixo:

````
from pyspark.sql import SparkSession

spark = (
    SparkSession.builder
    .appName("ETLExample")
    .master("local[*]")
    .getOrCreate()
)
````

- appName("ETLExample"): nome da aplicação Spark.

- master("local[*]"): usa todos os núcleos de CPU disponíveis como “executors” Spark.

- getOrCreate(): inicializa o Spark localmente.

A partir daí, todas as operações (como spark.read.csv(), df.write.parquet(), etc.) são executadas pelo motor distribuído do Apache Spark, e não pelo Python puro.

