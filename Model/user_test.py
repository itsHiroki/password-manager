#User class unit testing

import user
import random

def test_create_user_username():
    #setup
    expected = 'dragonMan44'

    #invoke
    actual = user.User('dragonMan44','kdakdmv394jklas',0)

    #analyze
    assert expected == actual.get_username()

def test_create_user_password():
    #setup
    expected = 'kdakdmv394jklas'

    #invoke
    actual = user.User('dragonMan44','kdakdmv394jklas',0)

    #analyze
    assert expected == actual.get_password()

def test_set_password():
    #setup
    expected = 'FootballFan1245'
    new_user = user.User('dragonMan44','kdakdmv394jklas',0)

    #invoke
    new_user.set_password('FootballFan1245')
    actual = new_user.get_password()

    #analyze
    assert expected == actual

def test_password_hash():
    #setup
    expected = 'c8447ff75c57cf3d5cd09c51d3fed7043aa1998db03d49d9ef051a75b8de69ce'

    #invoke
    actual = user.User('dragonMan44','kdakdmv394jklas',0)

    #analyze
    assert expected == actual.get_password_hash()

def test_get_id_new_user():
    #setup
    random.seed(1)
    expected = 623347347958
    new_user = user.User('dragonMan44','kdakdmv394jklas',0)
    #invoke
    actual = new_user.get_userID()

    #analyze
    assert expected == actual

def test_get_id_previous_user():
    #setup
    expected = 12
    new_user = user.User('dragonMan44','kdakdmv394jklas',12)
    #invoke
    actual = new_user.get_userID()

    #analyze
    assert expected == actual