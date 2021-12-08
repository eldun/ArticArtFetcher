import requests

web_api = 'https://api.artic.edu/api/v1/'
local_archive = './artic-api-data/json/'

data_source = web_api

r = requests.get(data_source + 'artworks/9614')
print(r.json())