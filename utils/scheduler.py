from pre_scrapers import webhallen
from stock_monitors.webhallen import webhallen_stock_monitor


def pre_scrapers():
    webhallen.run()



def monitors():
    webhallen_stock_monitor()


