from utils import db_calls, get_products, match_products



def run():
    STORE = "Manatorsk"

    product_types = db_calls.get_productTypes()
    products = get_products.get_manatorsk_products(STORE)
    matching_items = match_products.match_items_manatorsk(product_types, products)
    db_calls.insert_matches(matching_items, STORE)