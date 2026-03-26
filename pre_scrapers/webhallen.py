from utils import get_products, db_calls, match_products


def run():
    STORE = "Webhallen"
    product_types = db_calls.get_productTypes()
    products = get_products.get_webhallen_products(STORE)
    matching_items = match_products.match_items_webhallen(product_types, products)
    db_calls.insert_matches(matching_items, STORE)