import json
import os

def load_config():
    config_path = 'config.json'
    
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