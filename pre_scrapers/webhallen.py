from utils.db_calls import get_productTypes, insert_matches
from utils import items


def run():
    product_types = get_productTypes()
    products, store = items.findItemsFromApi()
    matching_items = items.matchItems(product_types, products)
    insert_matches(matching_items, store)





