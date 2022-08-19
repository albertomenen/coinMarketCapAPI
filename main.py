## Hacemos un request 
import requests
## Ciclo infinito que se ejecuta cada minuto##
import time 

headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY' : 'c4ea79a6-9dd5-4686-acd7-1caf0d73ea65'
}

parameters = {
    'start':'1',
    'limit':'10',
    'convert':'EUR'

}

url = 'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

json = requests.get(url, params = parameters, headers = headers).json()

print(json)
