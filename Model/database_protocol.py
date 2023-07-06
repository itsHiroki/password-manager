#Separate file that has all the credentials to access the mysql server
import database_credentials
import mysql.connector

#stores all the constants for the database connection
CREDENTIALS = database_credentials

class DatabaseProtocol:
    ''' Class will have all the functions necessary to interact with the database
    Including connecting, querying data, and adding new data to the database tables'''
    __slots__ = ['__database']

    def __init__(self):
        self.__database = 0

    def connect(self):
            '''Connects to the database'''
            try:
                self.__database = mysql.connector.connect(
                host = CREDENTIALS.HOST,
                user = CREDENTIALS.USER,
                password = CREDENTIALS.PASSWORD,
                database = CREDENTIALS.DATABASE
                )
                print("connection successful")
            except mysql.connector.Error as e:
                 print(f"Error connecting to the server: {e}")

    def is_connected(self):
        '''Checks if the server is connected'''
        if(self.__database == 0):
             return 'No connection'
        else:
             return 'connection active'