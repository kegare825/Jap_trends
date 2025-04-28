import subprocess
import sys
from pathlib import Path
import time
from src.utils.helpers import ensure_directory

def run_script(script_path, description):
    """Ejecuta un script y maneja errores"""
    print(f"\n{'='*50}")
    print(f"Ejecutando: {description}")
    print(f"{'='*50}")
    
    try:
        result = subprocess.run([sys.executable, script_path], check=True)
        if result.returncode == 0:
            print(f"✓ {description} completado exitosamente")
            return True
    except subprocess.CalledProcessError as e:
        print(f"✗ Error en {description}: {str(e)}")
        return False
    except Exception as e:
        print(f"✗ Error inesperado en {description}: {str(e)}")
        return False

def main():
    # Crear directorios necesarios
    ensure_directory(Path("data"))
    ensure_directory(Path("output"))
    ensure_directory(Path("output/visualizations"))
    
    # Definir scripts a ejecutar en orden
    scripts = [
        ("src/data/download_datasets.py", "Descarga de datasets"),
        ("src/data/process_data.py", "Procesamiento de datos"),
        ("src/visualization/visualize_trends.py", "Visualización de resultados")
    ]
    
    # Ejecutar cada script
    for script_path, description in scripts:
        if not run_script(script_path, description):
            print("\nSe detuvo la ejecución debido a un error.")
            sys.exit(1)
        time.sleep(2)  # Pequeña pausa entre scripts
    
    print("\n¡Proceso completado exitosamente!")
    print("Los resultados se encuentran en el directorio 'output/'")

if __name__ == "__main__":
    main() 