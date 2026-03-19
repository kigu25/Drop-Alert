from pre_scrapers.webhallen import get_productTypes, findItemsFromApi, get_store_id, matchItems, insert_matches
from DB_Config.Db_init import get_connection



def webhallen_stock_monitor():
    product_types = get_productTypes()
    products, store = findItemsFromApi()

    store_id = get_store_id(store)

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT externalID, quantity FROM inventory WHERE "
    "storeID = %s", (store_id,))

    rows_db = cur.fetchall()

    cur.close()
    conn.close()
    
    matching_items = matchItems(product_types, products)

    known_ids = [row[0] for row in rows_db]
    for key in matching_items:
        if key["id"] not in known_ids:
            insert_matches([key], store)
        else:
            for external_id, quantity in rows_db:
                if external_id == key["id"]:
                    if key["quantity"] > quantity:
                        print("STOCK HAS RISEN!!!")
                
