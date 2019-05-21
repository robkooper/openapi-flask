import json


data = json.load(open("data.json", "rb"))


def search(searchString=None, skip=0, limit=10):
    if skip > len(data):
        return {}
    if skip + limit > len(data):
        limit = len(data) - skip
    return data[skip:limit]


def get(inventoryId):
    for x in data:
        if inventoryId == x['id']:
            return x
    return "Not found", 404


def post():
    return "Not implemented", 500


def manufacturer_search(inventoryId):
    x = get(inventoryId)
    if isinstance(x, tuple):
        return x
    elif 'manufacturer' in x:
        return x['manufacturer']
    else:
        return "Not found", 404
