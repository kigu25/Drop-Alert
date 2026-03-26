from dotenv import load_dotenv
from DB_Config.Db_init import get_connection
from utils.scheduler import monitors, pre_scrapers
import schedule
import time


def main():
    load_dotenv()
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT DATABASE()")
    print("ACTIVE DATABASE: ", cur.fetchone()[0])

    cur.close()
    conn.close()


    # Schedule pre_scraper and monitor
    schedule.every(6).hours.do(pre_scrapers)
    schedule.every(3).minutes.do(monitors)

    pre_scrapers()
    monitors()

    while True:
        schedule.run_pending()
        time.sleep(1)



if __name__ == "__main__":
    main()