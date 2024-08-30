import requests
import json

URL = "https://0ou26ybc5i.execute-api.sa-east-1.amazonaws.com/default/serveless_api1"

data = {
    "nome" : "rafael",
    "sobrenome" : "pereira",
    "idade" : 19
}

headers = {
    "Content-Type": "application/json"
}

response = requests.post(URL, data=json.dumps(data), headers=headers)

print("Status Code:", response.status_code)
print("Response Body:", response.json())


