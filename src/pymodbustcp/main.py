from pyModbusTCP.client import ModbusClient

from utils import init_tcp_client


def main():
    # Выбираем устройство
    tcp_client = init_tcp_client()
    device = tcp_client.devices[0]

    print(tcp_client)
    print(device)

    try:
        client: ModbusClient = ModbusClient(host=tcp_client.ip, port=tcp_client.port, unit_id=device.unit_id, debug=True)
        client.write_single_register(0, 256)
        client.read_holding_registers(0, 4)
        client.close()
    except ValueError:
        print("No Modbus server found")


if __name__ == '__main__':
    main()
