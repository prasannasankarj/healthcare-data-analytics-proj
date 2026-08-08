from python.database.db_connection import engine

def test_database_connection():
    conn = engine.connect()
    assert conn is not None
    conn.close()
