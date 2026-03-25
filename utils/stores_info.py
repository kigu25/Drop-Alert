LINK_DICT = {
        
    "Webhallen" : "https://www.webhallen.com/api/productdiscovery/search/pokemon?page=1&touchpoint=DESKTOP&totalProductCountSet=false&origin=ORGANIC&sortBy=latest&limit=100",
    "Manatorsk" : "https://manatorsk-elastic-filter-production.up.railway.app/api/search"
    }




def find_url(store):
    return LINK_DICT.get(store)