class Client:
    def __init__(self, name, ip, port):
        self.name = name
        self.ip = ip
        self.port = port

    def __str__(self):
        return f'name: {self.name}\nip: {self.ip}\nport: {self.port}'
