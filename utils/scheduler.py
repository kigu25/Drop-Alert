from pre_scrapers.webhallen import get_productTypes, findItemsFromApi, matchItems, insert_matches
from stock_monitors.webhallen import webhallen_stock_monitor


def pre_scrapers():
    productTypes = get_productTypes()
    products, store = findItemsFromApi()
    matching_items = matchItems(productTypes, products)
    insert_matches(matching_items, store)



def monitors():
    webhallen_stock_monitor()


