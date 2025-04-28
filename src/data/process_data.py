from pyspark.sql import SparkSession
from pyspark.sql.functions import udf, col, year, to_date, explode, count
from pyspark.sql.types import ArrayType, StringType
import re
from pathlib import Path

def extract_kanji(text):
    """Extrae kanjis de un texto (Unicode: 4E00-9FFF)"""
    if text is None:
        return []
    return re.findall(r'[\u4E00-\u9FFF]', text)

def create_spark_session():
    """Crea y configura una sesión de Spark"""
    return SparkSession.builder \
        .appName("KanjiTrends") \
        .config("spark.executor.memory", "4g") \
        .config("spark.driver.memory", "4g") \
        .getOrCreate()

def process_text_files(spark, input_path):
    """Procesa archivos de texto y extrae kanjis"""
    # Cargar textos
    df = spark.read.text(str(input_path))
    
    # Registrar UDF para extraer kanjis
    extract_kanji_udf = udf(extract_kanji, ArrayType(StringType()))
    
    # Extraer kanjis
    df_kanji = df.withColumn("kanjis", extract_kanji_udf(col("value")))
    
    # Explotar la lista de kanjis
    df_exploded = df_kanji.select(explode("kanjis").alias("kanji"))
    
    # Contar frecuencia de cada kanji
    df_counts = df_exploded.groupBy("kanji").agg(count("*").alias("count"))
    
    return df_counts

def main():
    # Crear sesión de Spark
    spark = create_spark_session()
    
    # Directorios de entrada y salida
    data_dir = Path("data")
    output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)
    
    # Procesar cada dataset
    datasets = ["aozora-books", "japanese-wikipedia-articles", "japanese-news-articles"]
    
    for dataset in datasets:
        input_path = data_dir / dataset
        if not input_path.exists():
            print(f"Dataset {dataset} no encontrado. Saltando...")
            continue
            
        print(f"Procesando {dataset}...")
        df_counts = process_text_files(spark, input_path)
        
        # Guardar resultados
        output_path = output_dir / f"{dataset}_kanji_counts.parquet"
        df_counts.write.parquet(str(output_path))
        print(f"Resultados guardados en {output_path}")

if __name__ == "__main__":
    main() 