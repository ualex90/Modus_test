from pyModbusTCP.client import ModbusClient

from utils import init_tcp_client


def main():
    # Создаем клиент
    tcp_client = init_tcp_client(0)
    # Выбираем устройство
    device = tcp_client.devices[0]

    print(tcp_client)
    print(device)

    try:
        client: ModbusClient = ModbusClient(host=tcp_client.ip, port=tcp_client.port, unit_id=device.unit_id, debug=True)
        # client.write_single_register(0, 255)
        x = [hex(i) for i in client.read_holding_registers(0, 9)]
        client.write_single_register(1, int('0x104', 16))
        print(x)
        client.close()
    except ValueError:
        print("No Modbus server found")


if __name__ == '__main__':
    main()

# ['0x3', '0x104', '0x5', '0x9f', '0x0', '0x0', '0x3e8', '0xa', '0xffff']
