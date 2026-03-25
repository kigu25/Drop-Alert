import requests



# TODO: Switcha så vi inte behöver hårdkoda url utan kan skicka in de från en lista av färdiga url vi sparat någonstans
def findItemsFromApi():
    url = "https://www.webhallen.com/api/productdiscovery/search/pokemon?page=1&touchpoint=DESKTOP&totalProductCountSet=false&origin=ORGANIC&sortBy=latest&limit=100"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36"
    }
    api_response = requests.get(url, headers=headers)

    data = api_response.json()


    products = data["products"]
    print(len(products))

    start = "https://www."
    end = ".com"
    store = (url[url.find(start)+len(start):url.rfind(end)])
    
    return products, store





def matchItems(product_types, products):

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

    print(matching_items)
    return matching_items