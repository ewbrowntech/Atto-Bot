import requests
import json
import mimetypes
import pathlib

def upload_file(filepath, address, apiKey):
    headers = {
        "Authorization": "Bearer " + apiKey,
    }
    filename = pathlib.PurePath(filepath).name
    mimetype = mimetypes.guess_type(filepath)[0]
    file = {'filename': (filename, open(filepath, 'rb'), mimetype)}
    response = requests.post(address, headers=headers, files=file)
    url = json.loads(response.text)["url"]
    return url
