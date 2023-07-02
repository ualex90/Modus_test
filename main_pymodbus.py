from pymodbus.client import ModbusTcpClient

client = ModbusTcpClient('192.168.3.8')
client.connect()
client.write_coil(1, False, 8)
result = client.read_coils(1, 1, 8)
print(result.bits[7])
client.close()
