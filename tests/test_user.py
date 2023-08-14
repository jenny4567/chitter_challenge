from lib.user import User

'''
Test identical users are equivalent.
'''
def test_eq():
    user1 = User(1, 'telon_tusk', 'Telon Tusk', 'telontusk999@service.com', 'NooneWillGuessMe')
    user2 = User(1, 'telon_tusk', 'Telon Tusk', 'telontusk999@service.com', 'NooneWillGuessMe')
    assert user1 == user2