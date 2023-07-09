from config.setting import CLIENTS, DEVICES
from src.models.TcpClient import TcpClient
from utils import get_data

# Чтение данных из YML файлов
clients: list = get_data(CLIENTS)
devices: list = get_data(DEVICES)

# Создаем новый клиент и добавляем в него устройства
tcp_client = TcpClient(**clients[0])
[tcp_client.add_devise(devices[i]) for i in range(len(devices))]

# Выбираем устройство
device = tcp_client.devices[0]

print(tcp_client)
print(device)

# try:
#     client: ModbusClient = ModbusClient(host='192.168.3.9', port=502, unit_id=2, debug=True)
#     client.write_single_register(0, 13)
#     client.read_holding_registers(0, 4)
# except ValueError:
#     print("No Modbus server found")
