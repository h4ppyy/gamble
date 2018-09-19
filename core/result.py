import requests

url = 'http://ntry.com/data/json/games/dari/result.json'
payload = {}

r = requests.get(url, params=payload)
