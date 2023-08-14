from lib.user import User
from lib.user_repository import UserRepository

'''
Finds user from user id.
'''
def test_find_user(db_connection):
    db_connection.seed("seeds/chitter.sql")
    repository = UserRepository(db_connection)
    user = repository.find_user('telon_tusk')
    assert user == User(1, 'telon_tusk', 'Telon Tusk', 'telontusk999@server.com', 'NooneWillGuessMe')   

'''
Sets user login_status to True when correct login arguments are given.
return user arguments corresponds to.
'''
def test_valid_user_login(db_connection):
    db_connection.seed("seeds/chitter.sql")
    repository = UserRepository(db_connection)
    user = repository.login_user('telon_tusk', 'NooneWillGuessMe')
    assert user == User(1, 'telon_tusk', 'Telon Tusk', 'telontusk999@server.com', 'NooneWillGuessMe')




