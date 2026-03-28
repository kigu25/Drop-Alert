def match_items_webhallen(product_types, products):

    matching_items = []

    sorted_product_types = sorted(product_types.items(), key=lambda x: len(x[0]), reverse=True)


    for key in products:
        if not isinstance(key.get("stock"), dict):
            print(f"SKIPPED (invalid stock) ID: {key['id']} Name: {key['name']}")
            continue
        
        for type_name, type_id in sorted_product_types:
           if type_name in key["name"]:
               matching_items.append({
                   "name": key["name"],
                   "id": key["id"],
                   "type_id": type_id,
                   "price": float(key["price"]["price"]),
                   "quantity": key["stock"]["web"]
               })
               break
    return matching_items



def match_items_manatorsk(product_types, products):
    matching_items = []

    sorted_product_types = sorted(product_types.items(), key=lambda x: len(x[0]), reverse=True)

    for key in products:
        for type_name, type_id in sorted_product_types:
            if type_name in key["title"]:

                stripped_id = int(key["id"].split("/")[-1])
                matching_items.append({
                    "name" : key['title'],
                    "id": stripped_id,
                    "type_id": type_id,
                    "price": float(key["variants"][0]["price"]),
                    "quantity": max(0, key["variants"][0]["inventoryQuantity"]),
                    "handle": key["handle"],
                    "img_url": key["imgUrl"],
                })
                break
    return matching_items