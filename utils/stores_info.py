# This variabel should also store how we build links 
LINK_DICT = {
        
    "Webhallen" : "https://www.webhallen.com/api/productdiscovery/search/pokemon?page=1&touchpoint=DESKTOP&totalProductCountSet=false&origin=ORGANIC&sortBy=latest&limit=100",
    "Manatorsk" : "https://manatorsk-elastic-filter-production.up.railway.app/api/search"

    }






def find_url(store):
    return LINK_DICT.get(store)



def build_product_url(store, product_id):
    URL = ""
    starting = "https://www."
    

    if store == "Webhallen":
        URL = starting + "webhallen.com/product/" + product_id
    elif store == "Manatorsk":
        URL = "manatorsk.com/products/" + product_id ##ProductID for mana is their handle

    return URL



def build_image_url():
    pass