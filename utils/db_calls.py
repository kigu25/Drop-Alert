from DB_Config.Db_init import get_connection
from utils.discord import new_product_webhook

def update_quantity(storeID, external_id ,quantity):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("UPDATE inventory "
    "SET quantity = %s "
    "WHERE storeID = %s AND "
    "externalID = %s", (quantity, storeID, external_id,))

    conn.commit()
    cur.close()
    conn.close()


def get_productTypes():
    conn = get_connection()
    cur = conn.cursor(dictionary=True)
    cur.execute("SELECT typeName, typeID FROM producttype")

    product_types = {}
    for row in cur.fetchall():
        product_types[row["typeName"]] = row["typeID"]

    cur.close()
    conn.close()
    
    return product_types



def insert_matches(matching_items, store):
    conn = get_connection()
    cur = conn.cursor()

    store_id = get_store_id(store)

    for key in matching_items:
        cur.execute("INSERT IGNORE INTO inventory (storeID, externalID, typeID, price, quantity) "
        "VALUES (%s, %s, %s, %s, %s)", (store_id, key["id"], key["type_id"], key["price"], key["quantity"]))
        
        # If something is inserted then send the webhook
        if cur.rowcount == 1:
            new_product_webhook(store, key["name"], key["price"], key["id"], key.get("img_url", ""))
            

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