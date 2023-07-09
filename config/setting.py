from pathlib import Path

# Папки
ROOT = Path(__file__).resolve().parent.parent
CONFIG = Path(ROOT, 'config')

# Файлы
CLIENTS = Path(CONFIG, 'clients.yaml')
DEVICES = Path(CONFIG, 'devices.yaml')
