import database_protocol
import mysql.connector

def test_server_connection():
    #setup
    database = database_protocol.database_protocol()
    database.connect()
    expected = "connection active"

    #invoke
    actual = database.is_connected()

    #analyze
    assert actual == expected