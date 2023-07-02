# Импортируем библиотеку
import modbus_tk
import modbus_tk.defines as cst
import modbus_tk.modbus_tcp as modbus_tcp

master = modbus_tcp.TcpMaster(host='192.168.3.8', port=int(502))  # Создаем подключение к слэйву
master.set_timeout(1.0)                                           # Таймаут

# get_di = master.execute(3, cst.READ_DISCRETE_INPUTS, 0, 8)         # Чтение DISCRETE INPUTS
# get_coils = master.execute(3, cst.READ_COILS, 0, 12)               # Чтение COILS
# get_ir = master.execute(3, cst.READ_INPUT_REGISTERS, 0, 1)         # Чтение INPUT REGISTERS
get_hr = master.execute(3, cst.READ_HOLDING_REGISTERS, 0, 10)      # Чтение HOLDING REGISTERS

print(f'{get_hr}')
print(type(get_hr))
