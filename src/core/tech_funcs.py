import json
from pathlib import Path
import os

current_file = Path(__file__).resolve()
project_root = current_file.parent.parent.parent
config_path = project_root / "config" / "config.json"

def load_config():
    default_config = {
        "header_color": "#1f538d",    # Темно-синій (стандарт CTK)
        "mainframe_color": "#2b2b2b", # Темно-сірий
        "time_color": "#ffffff"       # Білий
    }

    if not os.path.exists(config_path):
        print(f"Попередження: {config_path} не знайдено. Використовую стандартні кольори.")
        return default_config

    try:
        with open(config_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (json.JSONDecodeError, Exception) as e:
        print(f"Помилка при читанні конфігу: {e}")
        return default_config