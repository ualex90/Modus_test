from pyModbusTCP.client import ModbusClient

from setting import CLIENTS
from utils import get_data

clients = get_data(CLIENTS)
client = Client()
print(clients)

# try:
#     client: ModbusClient = ModbusClient(host='192.168.3.9', port=502, unit_id=2, debug=True)
#     client.write_single_register(0, 13)
#     client.read_holding_registers(0, 4)
# except ValueError:
#     print("No Modbus server found")

