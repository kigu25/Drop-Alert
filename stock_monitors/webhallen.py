from DB_Config.Db_init import get_connection
from utils import get_products, db_calls, discord, match_products
from utils.discord import new_product_webhook



def webhallen_stock_monitor():
    print("Running Webhallen Monitor")
    STORE = "Webhallen"
    
    product_types = db_calls.get_productTypes()
    products = get_products.get_webhallen_products(STORE)

    store_id = db_calls.get_store_id(STORE)

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT externalID, quantity FROM inventory WHERE "
    "storeID = %s", (store_id,))

    rows_db = cur.fetchall()

    cur.close()
    conn.close()
    
    matching_items = match_products.match_items_webhallen(product_types, products)

    known_ids = [row[0] for row in rows_db]
    for key in matching_items:
        # If the ID is not known, insert it to DB and send a webhook to notify of new product
        if key["id"] not in known_ids:
            db_calls.insert_matches([key], STORE)
            new_product_webhook(STORE, key["name"], key["price"])

        else:
            for external_id, quantity in rows_db:
                if external_id == key["id"]:
                    if key["quantity"] > quantity:
                        discord.restock_webhook(key["name"], key["price"], STORE, key["id"])
                    if key["quantity"] != quantity:
                        db_calls.update_quantity(store_id, key["id"], key["quantity"])
    print("Webhallen done")

