from utils.db_calls import get_productTypes, insert_matches
from utils import items


def run():
    STORE = "Webhallen"
    product_types = get_productTypes()
    products = items.get_webhallen_products(STORE)
    matching_items = items.match_items_webhallen(product_types, products)
    insert_matches(matching_items, STORE)





