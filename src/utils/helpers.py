import re
from typing import List, Dict
from pathlib import Path

def is_kanji(char: str) -> bool:
    """Verifica si un carácter es un kanji (Unicode: 4E00-9FFF)"""
    return bool(re.match(r'[\u4E00-\u9FFF]', char))

def extract_kanji_from_text(text: str) -> List[str]:
    """Extrae todos los kanjis de un texto"""
    if not text:
        return []
    return re.findall(r'[\u4E00-\u9FFF]', text)

def count_kanji_frequency(text: str) -> Dict[str, int]:
    """Cuenta la frecuencia de cada kanji en un texto"""
    kanjis = extract_kanji_from_text(text)
    frequency = {}
    for kanji in kanjis:
        frequency[kanji] = frequency.get(kanji, 0) + 1
    return frequency

def ensure_directory(path: Path) -> None:
    """Asegura que un directorio existe"""
    path.mkdir(parents=True, exist_ok=True)

def get_file_size(path: Path) -> int:
    """Obtiene el tamaño de un archivo en bytes"""
    return path.stat().st_size if path.exists() else 0

def format_file_size(size_bytes: int) -> str:
    """Formatea el tamaño de un archivo en una cadena legible"""
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size_bytes < 1024.0:
            return f"{size_bytes:.2f} {unit}"
        size_bytes /= 1024.0
    return f"{size_bytes:.2f} TB" 