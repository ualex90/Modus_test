class TcpClient:
    def __init__(self, **kwargs):
        self.name = kwargs.get('name') or 'localhost'
        self.ip = kwargs.get('ip') or '127.0.0.1'
        self.port = kwargs.get('ip') or '502'
        self.devices = list()
        self.devices_list = list()

    def add_devise(self, devices):
        for device in devices:
            pass

    def __str__(self):
        return f'name: {self.name}\nip: {self.ip}\nport: {self.port}'
