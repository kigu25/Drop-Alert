from dotenv import load_dotenv
from DB_Config.Db_init import get_connection

def main():

    load_dotenv()
    conn = get_connection()




    conn.close

if __name__ == "__main__":
    main()