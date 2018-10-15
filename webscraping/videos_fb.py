import requests
import ast

url = "https://graph.facebook.com/v2.6/57527494924/videos"

querystring = {"access_token":"EAALDSOOFi9EBAKBviOmNZALGeZAxUrRl7aeRyDk3zuz6ZBS6gMRrjACrSuY9JTPd8MZCmUMdNA2AxRZBVZClEeAl2aRksoLZCWz5cz6xdx4UIT9RvWlOB9nPIsGRy7lqPJogFw24gxPLNTOaaZBNjYiWiMmfTxNZCsmIZD"}

headers = {
    'token': "EAALDSOOFi9EBAKBviOmNZALGeZAxUrRl7aeRyDk3zuz6ZBS6gMRrjACrSuY9JTPd8MZCmUMdNA2AxRZBVZClEeAl2aRksoLZCWz5cz6xdx4UIT9RvWlOB9nPIsGRy7lqPJogFw24gxPLNTOaaZBNjYiWiMmfTxNZCsmIZD",
    'limit': "1",
    'fields': "id,live_status,embed_html",
    'cache-control': "no-cache",
    'postman-token': "c2b812e8-248c-b409-e0af-d7b4f0c7976d"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print("/////////////////")
print(type(response.content))
print("/////////////////")
lista = ast.literal_eval(response.content)['data']

for vv in lista:
    print(vv)

print("/////////////////")
print("/////////////////")
