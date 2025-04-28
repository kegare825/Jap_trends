import os
import kaggle
from pathlib import Path
import shutil
from dotenv import load_dotenv

def setup_kaggle():
    """Configura la API de Kaggle usando las credenciales del archivo .env"""
    load_dotenv()
    os.environ['KAGGLE_USERNAME'] = os.getenv('KAGGLE_USERNAME')
    os.environ['KAGGLE_KEY'] = os.getenv('KAGGLE_KEY')

def download_dataset(dataset_name, output_dir):
    """Descarga un dataset de Kaggle"""
    try:
        kaggle.api.dataset_download_files(
            dataset_name,
            path=output_dir,
            unzip=True,
            quiet=False
        )
        print(f"Dataset {dataset_name} descargado exitosamente en {output_dir}")
    except Exception as e:
        print(f"Error al descargar {dataset_name}: {str(e)}")

def main():
    # Configurar directorios
    data_dir = Path("data")
    data_dir.mkdir(exist_ok=True)
    
    # Configurar Kaggle
    setup_kaggle()
    
    # Lista de datasets a descargar
    datasets = [
        "aceofspades914/top-japanese-wikipedia-pages-nlp",  # Wikipedia japonesa
        "vyhuholl/japanese-newspapers-20052021",  # Periódicos japoneses
        "annazhabina/aozora-bunko"  # Aozora Bunko
    ]
    
    # Descargar cada dataset
    for dataset in datasets:
        dataset_name = dataset.split('/')[-1]
        output_path = data_dir / dataset_name
        download_dataset(dataset, str(output_path))

if __name__ == "__main__":
    main() 