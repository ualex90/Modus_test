import yaml
from yaml.loader import SafeLoader

from config.setting import CLIENTS, DEVICES
from src.models.TcpClient import TcpClient


def get_data(file):
    with open(file, 'r', encoding='UTF-8') as file_in:
        data = yaml.load(file_in, Loader=SafeLoader)
    return data


def init_tcp_client(index):
    """Инициализация нового клиента и устройств"""
    # Чтение данных из YML файлов
    clients: list = get_data(CLIENTS)
    devices: list = get_data(DEVICES)

    # Создаем новый клиент и добавляем в него устройства
    tcp_client = TcpClient(**clients[index])
    [tcp_client.add_devise(devices[i]) for i in range(len(devices))]
    return tcp_client


def get_mb_settings(device):
    ...
