from pre_scrapers import webhallen, manatorsk
from stock_monitors.webhallen import webhallen_stock_monitor
from stock_monitors.manatorsk import manatorsk_stock_monitor


def pre_scrapers():
    webhallen.run()
    manatorsk.run()



def monitors():
    webhallen_stock_monitor()
    manatorsk_stock_monitor()


