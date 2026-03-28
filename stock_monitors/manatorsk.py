from DB_Config.Db_init import get_connection
from utils import get_products, db_calls, discord, match_products
from utils.discord import new_product_webhook

def manatorsk_stock_monitor():
    print("Running Manatorsk Monitor")
    STORE = "Manatorsk"

    product_types = db_calls.get_productTypes()
    products = get_products.get_manatorsk_products(STORE)

    store_id = db_calls.get_store_id(STORE)

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT externalID, quantity FROM inventory WHERE "
    "storeID = %s", (store_id,))

    rows_db = cur.fetchall()

    cur.close()
    conn.close()

    matching_products = match_products.match_items_manatorsk(product_types, products)

    known_ids = [row[0] for row in rows_db]
    for key in matching_products:
        # If the ID is not known, insert it to DB and send a webhook to notify of new product
        if key["id"] not in known_ids:
            db_calls.insert_matches([key], STORE)

        else:
            for external_id, quantity in rows_db:
                if external_id == key["id"]:
                    if key["quantity"] > quantity:
                        discord.restock_webhook(key["name"], key["price"], STORE, key["handle"], key["img_url"])
                    if key["quantity"] != quantity:
                        db_calls.update_quantity(store_id, key["id"], key["quantity"])
                    break
    print("Manatorsk Done")