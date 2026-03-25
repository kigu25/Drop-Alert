from utils.db_calls import get_productTypes, insert_matches
from utils import items


def run():
    STORE = "Webhallen"
    product_types = get_productTypes()
    products = items.findItemsFromApi(STORE)
    matching_items = items.matchItems(product_types, products)
    insert_matches(matching_items, STORE)





