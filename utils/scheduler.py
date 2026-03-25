from pre_scrapers import webhallen, manatorsk
from stock_monitors import webhallen, manatorsk


def pre_scrapers():
    webhallen.run()
    manatorsk.run()



def monitors():
    webhallen.webhallen_stock_monitor()
    manatorsk.manatorsk_stock_monitor()


