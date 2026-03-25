from utils.db_calls import get_productTypes, insert_matches
from utils import get_products, db_calls, match_products


def run():
    STORE = "Webhallen"
    product_types = get_productTypes()
    products = get_products.get_webhallen_products(STORE)
    matching_items = match_products.match_items_webhallen(product_types, products)
    insert_matches(matching_items, STORE)





