import AttoAPI


def get_apikey():
    with open('config/tokens/atto-api-key', 'r') as file:
        return file.read()

def get_atto_address():
    with open('config/atto-address', 'r') as file:
        return file.read()
def upload_file(filepath):
    address = get_atto_address()
    apikey = get_apikey()
    url = AttoAPI.upload_file(filepath, address, apikey)
    return url
