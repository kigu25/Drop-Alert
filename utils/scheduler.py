from pre_scrapers import webhallen, manatorsk
from stock_monitors.webhallen import webhallen_stock_monitor


def pre_scrapers():
    webhallen.run()
    manatorsk.run()



def monitors():
    pass
    # webhallen_stock_monitor()


