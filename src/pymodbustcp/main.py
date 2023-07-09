from config.setting import CLIENTS, DEVICES
from src.models.TcpClient import TcpClient
from utils import get_data

clients: list = get_data(CLIENTS)
devices = get_data(DEVICES)

client = TcpClient(**clients[0])
print(client)

print(devices)

# try:
#     client: ModbusClient = ModbusClient(host='192.168.3.9', port=502, unit_id=2, debug=True)
#     client.write_single_register(0, 13)
#     client.read_holding_registers(0, 4)
# except ValueError:
#     print("No Modbus server found")
