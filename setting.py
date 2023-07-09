from pathlib import Path

ROOT = Path(__file__).resolve().parent
DEV = Path(ROOT, 'dev')

CLIENTS = Path(DEV, 'clients.yaml')
DEVICES = Path(DEV, 'devices.yaml')
