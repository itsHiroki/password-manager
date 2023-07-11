#Terminal version of the password manager

#imports
import user
import database_protocol


class PassMaster:
    '''Function calls used by the user'''
    def __init__(self):
        pass

    def login(self):
        pass


    def create_new_user(self,username, password):
        return user.User(username, password, 0)

    def new_user(self):
        username = input ('Enter username: ')
        password = input ('Enter password: ')

        if(username != '' and password != ''):
            return self.create_new_user(username, password)
        else:
            self.new_user()

def main():
    pm = PassMaster()
    option = input("Welcome to PassMaster \nPress 1 to login or 2 to create a new user: ")
    if option == '1':
        pm.login()
    elif option == '2':
        user = pm.new_user()
    else:
        main()


if __name__ == "__main__":
    main()