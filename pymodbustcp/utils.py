import yaml
from yaml.loader import SafeLoader


def get_data(file):
    with open(file, 'r', encoding='UTF-8') as file_in:
        data = yaml.load(file_in, Loader=SafeLoader)
    return data
