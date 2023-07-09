class Device:
    def __init__(self, **kwargs):
        self.name = kwargs.get('name')
        self.model = kwargs.get('model')
        self.description = kwargs.get('description')
        self.unit_id = int(kwargs.get('modbus').get('unit_id'))
        self.baud_rate = int(kwargs.get('modbus').get('baud_rate'))
        self.data_bits = int(kwargs.get('modbus').get('data_bits'))
        self.parity = kwargs.get('modbus').get('parity')
        self.stop_bits = int(kwargs.get('modbus').get('stop_bits'))
        self.coils = kwargs.get('modbus').get('coils')
        self.discrete_inputs = kwargs.get('modbus').get('discrete_inputs')
        self.holding_registers = kwargs.get('modbus').get('holding_registers')
        self.input_registers = kwargs.get('modbus').get('input_registers')
        if 'razumdom' in self.name.lower():
            self.rd_scenarios = kwargs.get('razumdom').get('rd_scenarios')

    def coil(self, coil):
        ...

    def __str__(self):
        return f'''Device name: {self.name}
                 \rModel: {self.model}
                 \rDescription: {self.description}
                 \rmodbus: {self.baud_rate}/{self.data_bits}-{self.parity}-{self.stop_bits}'''
