from datetime import datetime, timedelta
import requests
import ast

hoy = datetime.now()
hace_7_dias = hoy - timedelta(days=7)

url = "https://ecoid.pe/api/v1/userapinewsletter/547a1802dfdcaa443d08c92c8dac62e9"
querystring = {
"date_start": hace_7_dias.strftime("%Y-%m-%d"),
"date_end": hoy.strftime("%Y-%m-%d")
}

headers = {
    'authorization': "dadef83712b0eed7a5342a477627ed5136ca860b",
    'cache-control': "no-cache",
    'postman-token': "9740f654-d638-7368-9bb3-0bf46b01d139"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print("%%%%%%%%%%%%%%%%%%%%%%%%%%%")
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%")
print(querystring)
print(response.status_code)
lista = ast.literal_eval(response.content)

for datus in lista:
    print(type(datus))
    print(datus)
    break

print("%%%%%%%%%%%%%%%%%%%%%%%%%%%")
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%")


