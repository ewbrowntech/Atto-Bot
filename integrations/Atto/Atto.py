import AttoAPI
import json

def get_apikey():
    with open('config/tokens/atto-api-key', 'r') as file:
        return file.read()

def get_atto_addresses():
    address_file = open('config/atto-addresses.json', 'r')
    addresses = json.load(address_file)
    address_file.close()
    return addresses

def upload_file(filepath):
    address = get_atto_addresses()["upload"]
    apikey = get_apikey()
    url = AttoAPI.upload_file(filepath, address, apikey)
    return url