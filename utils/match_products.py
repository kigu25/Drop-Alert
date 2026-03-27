def match_items_webhallen(product_types, products):

    matching_items = []

    for key in products:
       for type_name, type_id in product_types.items():
           if type_name in key["name"]:
               matching_items.append({
                   "name": key["name"],
                   "id": key["id"],
                   "type_id": type_id,
                   "price": float(key["price"]["price"]),
                   "quantity": key["stock"]["web"]
               })
    return matching_items



def match_items_manatorsk(product_types, products):
    matching_items = []

    for key in products:
        for type_name, type_id in product_types.items():
            if type_name in key["title"]:

                stripped_id = int(key["id"].split("/")[-1])
                matching_items.append({
                    "name" : key['title'],
                    "id": stripped_id,
                    "type_id": type_id,
                    "price": float(key["variants"][0]["price"]),
                    "quantity": max(0, key["variants"][0]["inventoryQuantity"]),
                    "handle": key["handle"]
                })
    return matching_items