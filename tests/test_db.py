import pytest
from dotenv import load_dotenv
from DB_Config.Db_init import get_connection


def test_db_connection():
    load_dotenv()
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT database()")
    db_name = cur.fetchone()[0]

    cur.close()
    conn.close()
    
    assert db_name == "drop_alert"