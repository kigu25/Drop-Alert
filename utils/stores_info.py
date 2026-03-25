LINK_DICT = {
        
    "Webhallen" : "https://www.webhallen.com/api/productdiscovery/search/pokemon?page=1&touchpoint=DESKTOP&totalProductCountSet=false&origin=ORGANIC&sortBy=latest&limit=100",
        
    }




def find_url(store):
    return LINK_DICT.get(store)