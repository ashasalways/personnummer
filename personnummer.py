import requests
import random

looping = True
randomtal = random.randint(1, 10000)

print("\n Hämta Personnummer från Skatteverket! \n")

while looping:

    url = f"https://skatteverket.entryscape.net/rowstore/dataset/b4de7df7-63c0-4e7e-bb59-1f156a591763/json?_offset=[randomtal]&_limit=1"

    req = requests.get(url)


    jsondata = req.json()
    lista = jsondata['results']
    personnummer = lista[0]['testpersonnummer']
    print(lista)

    entill = input("\n vill du slå in ett personnummer till? Y/N \n")
    if (entill == "N" or entill == "n"):
        break