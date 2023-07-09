from pymodbus.client import ModbusTcpClient

client = ModbusTcpClient(host='192.168.3.9', port=502)
client.connect()
client.write_coil(1, False)
result = client.read_coils(4, 1)
print(result.bits[7])
client.close()
