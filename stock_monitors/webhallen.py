from pre_scrapers.webhallen import findItemsFromApi, matchItems, insert_matches
from DB_Config.Db_init import get_connection
from utils.discord import discord_webhook
from utils.db_calls import update_quantity, get_productTypes, get_store_id


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
                        discord_webhook(key["name"], key["price"], store, key["id"])
                    if key["quantity"] != quantity:
                        update_quantity(store_id, key["id"], key["quantity"])


