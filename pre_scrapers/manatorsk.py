from utils import db_calls
from utils import items



def run():
    STORE = "Manatorsk"

    product_types = db_calls.get_productTypes()
    products = items.get_manatorsk_products(STORE)
    matching_items = items.match_items_manatorsk(product_types, products)
    db_calls.insert_matches(matching_items, STORE)