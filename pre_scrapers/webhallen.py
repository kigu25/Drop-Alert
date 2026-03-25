from DB_Config.Db_init import get_connection
from utils.db_calls import get_store_id, get_productTypes
from utils import items


def run():
    product_types = get_productTypes()
    products, store = items.findItemsFromApi()
    matching_items = items.matchItems(product_types, products)
    insert_matches(matching_items, store)




def insert_matches(matching_items, store):
    conn = get_connection()
    cur = conn.cursor()

    store_id = get_store_id(store)

    for key in matching_items:
        cur.execute("INSERT IGNORE INTO Inventory (storeID, externalID, typeID, price, quantity) "
        "VALUES (%s, %s, %s, %s, %s)", (store_id, key["id"], key["type_id"], key["price"], key["quantity"]))

    conn.commit()
    cur.close()
    conn.close()
