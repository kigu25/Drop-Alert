from pre_scrapers.webhallen import insert_matches
from DB_Config.Db_init import get_connection
from utils import items, db_calls, discord


def webhallen_stock_monitor():
    STORE = "Webhallen"
    
    product_types = db_calls.get_productTypes()
    products = items.findItemsFromApi(STORE)

    store_id = db_calls.get_store_id(STORE)

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT externalID, quantity FROM inventory WHERE "
    "storeID = %s", (store_id,))

    rows_db = cur.fetchall()

    cur.close()
    conn.close()
    
    matching_items = items.matchItems(product_types, products)

    known_ids = [row[0] for row in rows_db]
    for key in matching_items:
        if key["id"] not in known_ids:
            insert_matches([key], STORE)

        else:
            for external_id, quantity in rows_db:
                if external_id == key["id"]:
                    if key["quantity"] > quantity:
                        discord.discord_webhook(key["name"], key["price"], STORE, key["id"])
                    if key["quantity"] != quantity:
                        db_calls.update_quantity(store_id, key["id"], key["quantity"])


