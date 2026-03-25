from utils import db_calls
from utils import items



def run():
    STORE = "Manatorsk"

    product_types = db_calls.get_productTypes()
    