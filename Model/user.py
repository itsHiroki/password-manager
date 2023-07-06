#imports
import hashlib
import random
import database_constants

class User:
    '''class will have all the data needed for a user to be added to the database when creating a new user or login in'''
    slots = ['__username','__password','__userID','__password_hash']

    def __init__(self,username,password,userID):
        if userID == 0:
            self.__username = username
            self.__password = password
            self.__userID = random.randint(1, database_constants.MAX_USERS)
            self.__password_hash = hashlib.sha256(self.__password.encode('utf-8')).hexdigest()
        else:
            self.__username = username
            self.__password = password
            self.__userID = userID
            self.__password_hash = password
        
        def get_username():
            return self.__username

        def get_password():
            return self.__password
        
        def set_password(password):
            self.__password = password