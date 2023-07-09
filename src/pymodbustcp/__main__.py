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
        client: ModbusClient = ModbusClient(host=tcp_client.ip, port=tcp_client.port, unit_id=device.unit_id)
        # Read holding registers
        hr = [hex(i) for i in client.read_holding_registers(0, 2)]

        # Read input registers
        ir = client.read_input_registers(1, 8)

        # Read discrete inputs
        di = [int(i) for i in client.read_discrete_inputs(1, 8)]

        # Read coils
        coils = [int(i) for i in client.read_coils(1, 12)]

        # # Write single register
        # client.write_single_register(1, int('0x104', 16))

        # # Write multiple registers
        # client.write_multiple_registers(0, [int('0x3', 16), int('0x104', 16)])

        # # Write single coil
        # client.write_single_coil(1, False)

        # # Write multiple coils
        # client.write_multiple_coils(1, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

        print('\nHolding Registers:', hr)
        print('Input Registers:', ir)
        print('Discrete Inputs:', di)
        print('Coils:', coils)

        client.close()
    except ValueError:
        print("No Modbus server found")


if __name__ == '__main__':
    main()

# ['0x3', '0x104', '0x5', '0x9f', '0x0', '0x0', '0x3e8', '0xa', '0xffff']
