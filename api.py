import requests

web_api = 'https://api.artic.edu/api/v1/'
local_archive = './artic-api-data/json/'

r = requests.get(web_api + 'artworks/9614')
print(r.json())