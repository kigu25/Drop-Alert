from DB_Config.Db_init import get_connection

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
    cur.execute("SELECT typeName, typeID FROM productType")

    product_types = {}
    for row in cur.fetchall():
        product_types[row["typeName"]] = row["typeID"]

    cur.close()
    conn.close()
    
    return product_types
