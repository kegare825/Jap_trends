# Análisis de Tendencias de Kanjis en Literatura Japonesa

Este proyecto utiliza PySpark para analizar la evolución en la frecuencia de uso de kanjis en textos japoneses a lo largo del tiempo.

## Estructura del Proyecto

```
.
├── data/                   # Directorio para datasets
├── notebooks/             # Jupyter notebooks para análisis
├── src/                   # Código fuente
│   ├── data/             # Scripts de procesamiento de datos
│   ├── visualization/    # Scripts de visualización
│   └── utils/            # Utilidades
├── config/               # Archivos de configuración
└── output/              # Resultados y visualizaciones
```

## Requisitos

- Python 3.8+
- PySpark 3.5.0
- Kaggle API
- Jupyter Notebook

## Instalación

1. Clonar el repositorio
2. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```
3. Configurar Kaggle API:
   - Crear cuenta en Kaggle
   - Descargar kaggle.json de tu perfil
   - Colocar kaggle.json en ~/.kaggle/

## Uso

1. Descargar datasets:
   ```bash
   python src/data/download_datasets.py
   ```

2. Procesar datos:
   ```bash
   python src/data/process_data.py
   ```

3. Visualizar resultados:
   ```bash
   python src/visualization/visualize_trends.py
   ```

## Datasets

- Aozora Bunko (Kaggle)
- Wikipedia Japanese Dumps
- NHK News Archives

## Licencia

MIT 