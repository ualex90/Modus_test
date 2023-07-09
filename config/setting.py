from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONFIG = Path(ROOT, 'config')

CLIENTS = Path(CONFIG, 'clients.yaml')
DEVICES = Path(CONFIG, 'devices.yaml')
