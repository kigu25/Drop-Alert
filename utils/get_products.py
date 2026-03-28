import requests
from utils import stores_info
from bs4 import BeautifulSoup



def get_webhallen_products(store):
    URL = stores_info.find_url(store)

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36"
    }

    api_response = requests.get(URL, headers=headers)
    
    data = api_response.json()
    products = data["products"]

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




def get_maxgaming_products():
    pass