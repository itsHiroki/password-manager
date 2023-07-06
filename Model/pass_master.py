import user
import database_protocol


def login():
    pass


def create_new_user(username, password):
    return user.User(username, password, 0)

def new_user():
    username = input ('Enter username: ')
    password = input ('Enter password: ')

    if(username != '' and password != ''):
        return create_new_user(username, password)
    else:
        new_user()

def main():
    option = input("Welcome to PassMaster \nPress 1 to login or 2 to create a new user: ")
    if option == '1':
        login()
    elif option == '2':
        user = new_user()
    else:
        main()


if __name__ == "__main__":
    main()