import requests

url = "https://api.dofusdu.de/dofus2/fr/items/equipment?filter%5Bmin_level%5D=100&filter%5Bmax_level%5D=200&page%5Bsize%5D=-1&page%5Bnumber%5D=1&fields%5Bitem%5D=effects"

def GETResponse():
    response = requests.get(url)
    return response.json()