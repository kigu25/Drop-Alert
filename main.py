from dotenv import load_dotenv
from DB_Config.Db_init import get_connection
from fill_inventory import get_productTypes, findItemsFromApi, matchItems

def main():

    load_dotenv()
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT DATABASE()")
    print("ACTIVE DATABASE: ", cur.fetchone()[0])

    cur.close()
    conn.close

    productTypes = get_productTypes()
    products, store = findItemsFromApi()
    matchItems(productTypes, products, store)

if __name__ == "__main__":
    main()