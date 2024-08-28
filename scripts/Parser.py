import pandas as pd
from Scraper import GETResponse

items = GETResponse()
items.pop("_links")

def init_df():
    data = { "name" : [] }
    for item in items["items"]:
        if "effects" in item:
            for effect in item["effects"]:
                if "type" in effect and effect["type"]["name"] not in data:
                    data[effect["type"]["name"]] = []
    df = pd.DataFrame(data)
    return df

def populate_df():
    df = init_df()
    item = {}
    for item in items["items"]:
        if "effects" in item:
            for effect in item["effects"]:
                if "type" in effect:
                    item[effect["type"]["name"]] = max(effect["int_maximum"], effect["int_minimum"])
        df = df._append(item, ignore_index = True)
        item = {}
    df = df.drop("effects", axis = 1)
    return df
        
    
    