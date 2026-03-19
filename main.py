from dotenv import load_dotenv
from DB_Config.Db_init import get_connection
from pre_scrapers.webhallen import get_productTypes, findItemsFromApi, matchItems, insert_matches
from utils.discord import discord_webhook

def main():

    load_dotenv()
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT DATABASE()")
    print("ACTIVE DATABASE: ", cur.fetchone()[0])

    cur.close()
    conn.close()

    productTypes = get_productTypes()
    products, store = findItemsFromApi()
    matching_items = matchItems(productTypes, products)
    insert_matches(matching_items, store)
    discord_webhook("151", "899", "Webhallen", 362583)



if __name__ == "__main__":
    main()