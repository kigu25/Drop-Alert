import requests
from utils import stores_info



def get_webhallen_products(store):
    URL = stores_info.find_url(store)

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36"
    }
    api_response = requests.get(URL, headers=headers)

    data = api_response.json()

    products = data["products"]
    print(len(products))
    
    return products




def get_manatorsk_products(store):
    URL = stores_info.find_url(store)
    products = []
    cursor = None


    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36"
    }

    body = {
        "collection": { "handle": "alla-produkter", "id": "645384143186" },
        "pagination": { "size": 20, "searchAfter": None },
        "filters": [],
        "search": { "title": "pokemon" },
        "sort": "relevance",
        "includeAggregations": False,
        "isSearchPage": True
    }


    while True:
        body["pagination"]["searchAfter"] = cursor

        api_response = requests.post(
        URL, json=body, headers=headers).json()

        products.extend(api_response["products"])
        cursor = api_response.get("nextCursor")

        if cursor is None:
            break

    return products




def match_items_webhallen(product_types, products):

    matching_items = []

    for key in products:
       for type_name, type_id in product_types.items():
           if type_name in key["name"]:
               print(f"MATCH: {key['name']} {key['id']} {key['price']['price']}: {type_name}")
               matching_items.append({
                   "name": key["name"],
                   "id": key["id"],
                   "type_id": type_id,
                   "price": float(key["price"]["price"]),
                   "quantity": key["stock"]["web"]
               })
    return matching_items



def match_items_manatorsk(product_types, products):
    matching_items = []

    for key in products:
        for type_name, type_id in product_types.items():
            if type_name in key["title"]:
                print(f"MATCH: {key['title']} {key['id']} {key['variants'][0]['price']}: {type_name}")

                stripped_id = int(key["id"].split("/")[-1])

                matching_items.append({
                    "name" : key['title'],
                    "id": stripped_id,
                    "type_id": type_id,
                    "price": float(key["variants"][0]["price"]),
                    "quantity": max(0, key["variants"][0]["inventoryQuantity"])
                })
    return matching_items