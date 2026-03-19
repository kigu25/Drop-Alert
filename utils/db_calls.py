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