## Hacemos un request 
import requests
## Ciclo infinito que se ejecuta cada minuto##
import time 

## Ahora importamos la pretty Table
import prettytable from PrettyTable

headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY' : 'c4ea79a6-9dd5-4686-acd7-1caf0d73ea65'
}

parameters = {
    'start':'1',
    'limit':'5',
    'convert':'EUR'

}


url = 'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

json = requests.get(url, params = parameters, headers = headers).json()

coins = json ["data"]

while True:
    print("Obteniendo datos ")
    for coin in coins:
        if coin  ["symbol"] == "BTC":
            file = open("./BTC.txt", "W")
            file.write(str(round(coin ["quote"]["EUR"]["price"],5) ) + "\n" )
        if coin  ["symbol"] == "ETH":
            file = open("./ETH.txt", "W")
            file.write(str(round(coin ["quote"]["EUR"]["price"],5) ) + "\n" )
        if coin  ["symbol"] == "USDT":
            file = open("./USDT.txt", "W")
            file.write(str(round(coin ["quote"]["EUR"]["price"],5) ) + "\n ")
        if coin  ["symbol"] == "USDC":
            file = open("./USDC.txt", "W")
            file.write(str(round(coin ["quote"]["EUR"]["price"],5) ) + "\n ")
        if coin  ["symbol"] == "BNB":
            file = open("./BNB.txt", "W")
            file.write(str(round(coin ["quote"]["EUR"]["price"],5) ) + "\n" )
        if coin  ["symbol"] == "BUSD":
            file = open("./BUSD.txt", "W")
            file.write(str(round(coin ["quote"]["EUR"]["price"],5) ) + "\n" )
            
  table = PrettyTable()
  table.add_column("BTC")
  table.add_column("price")

  
    print("PrettyTable")
    print("Datos obtenidos")
    time.sleep(60)
