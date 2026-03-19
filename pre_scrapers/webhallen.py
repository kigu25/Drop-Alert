from DB_Config.Db_init import get_connection
import requests


def get_productTypes():
    conn = get_connection()
    cur = conn.cursor(dictionary=True)
    cur.execute("SELECT typeName, typeID FROM productType")

    product_types = {}
    for row in cur.fetchall():
        product_types[row["typeName"]] = row["typeID"]

    cur.close()
    conn.close()
    
    return product_types



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
               matching_items.append((key['name'], key["id"], type_id, float(key["price"]["price"]), key["stock"]["web"]))

    print(matching_items)
    return matching_items




def insert_matches(matching_items, store):
    conn = get_connection()
    cur = conn.cursor()

    store_id = get_store_id(store)

    for key in matching_items:
        cur.execute("INSERT IGNORE INTO Inventory (storeID, externalID, typeID, price, quantity) "
        "VALUES (%s, %s, %s, %s, %s)", (store_id, key[1], key[2], key[3], key[4]))

    conn.commit()
    cur.close()
    conn.close()






def get_store_id(store):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT storeID FROM store "
    "WHERE storename = %s", (store,))
    store_id = cur.fetchone()[0]

    cur.close()
    conn.close()

    return store_id