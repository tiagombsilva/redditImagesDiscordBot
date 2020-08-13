import json

with open('helper/config.json') as json_file:
    data = json.load(json_file)

class Config:
    subReddits = data["subReddits"]
    json = data
