import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import os

def load_parquet_data(file_path):
    """Carga datos desde archivo parquet"""
    return pd.read_parquet(file_path)

def plot_top_kanjis(df, title, output_path, top_n=20):
    """Grafica los kanjis más frecuentes"""
    plt.figure(figsize=(15, 8))
    top_kanjis = df.nlargest(top_n, 'count')
    
    sns.barplot(x='kanji', y='count', data=top_kanjis)
    plt.title(f'Top {top_n} Kanjis más frecuentes - {title}')
    plt.xlabel('Kanji')
    plt.ylabel('Frecuencia')
    plt.xticks(rotation=45)
    
    # Guardar gráfico
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()

def main():
    # Configurar estilo
    sns.set_style("whitegrid")
    plt.rcParams['font.family'] = 'DejaVu Sans'  # Fuente que soporta caracteres japoneses
    
    # Directorios
    output_dir = Path("output")
    viz_dir = Path("output/visualizations")
    viz_dir.mkdir(exist_ok=True)
    
    # Procesar cada archivo de resultados
    for file in output_dir.glob("*_kanji_counts.parquet"):
        dataset_name = file.stem.replace("_kanji_counts", "")
        print(f"Procesando visualización para {dataset_name}...")
        
        # Cargar datos
        df = load_parquet_data(file)
        
        # Crear visualización
        output_path = viz_dir / f"{dataset_name}_top_kanjis.png"
        plot_top_kanjis(df, dataset_name, output_path)
        
        print(f"Visualización guardada en {output_path}")

if __name__ == "__main__":
    main() 