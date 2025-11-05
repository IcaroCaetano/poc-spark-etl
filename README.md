# PoC Spark ETL

Repositório de prova de conceito para estudar Apache Spark com Python (PySpark).

Estrutura do projeto:

````
poc-spark-etl/
│
├── data/                         # Where will the input and output files (CSV, JSON, Parquet, etc.) be located?
│   ├── input/
│   └── output/
│
├── src/
│   ├── main/
│   │   └── etl_job.py            # Main ETL script
│   └── utils/
│       └── spark_session.py      # Function to create the SparkSession
│
├── notebooks/
│   └── exploratory.ipynb         # (Optional) For testing in Jupyter Notebook
│
├── requirements.txt              # Python Dependencies
├── .gitignore
└── README.md

````

Dependências
pyspark
pandas
pyarrow

Como rodar (local)
1. Crie e ative um ambiente virtual (recomendado):

````
python -m venv .venv

source .venv/bin/activate  # macOS / Linux

.venv\Scripts\activate     # Windows

pip install -r requirements.txt
````

2. Coloque os dados de entrada em `data/input/` (ex.: `sample_data.csv` já fornecido).

3. Execute o job ETL:

python -m src.main.etl_job

O resultado será gravado em `data/output/cleaned_data.parquet`.

Observações
- O projeto utiliza Spark em modo local para aprendizado (`master("local[*]")`).
- `data/output/.gitkeep` é usado para manter o diretório no repositório.
