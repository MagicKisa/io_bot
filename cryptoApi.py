import requests
import json

def data_from_json(filename):
    with open(filename, 'r') as file:
        return json.load(file)

apis_dict = data_from_json("apis_dict.json")

def get_source_code(address, platform):
    for api in apis_dict["apis"]:
        if api["scan_name"] == platform:
            url = api["url"]
            apikey = api["apikey"]

    params = {"module": "contract", "action" : "getsourcecode", "address" : address, "apikey": apikey}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()  # Извлечение данных из JSON-ответа
        try:
            source_code = data['result'][0]['SourceCode']
        except TypeError:
            return None
        return source_code

    
