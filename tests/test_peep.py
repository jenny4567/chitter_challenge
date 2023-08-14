from lib.peep import Peep

'''
Test identical peeps are equivalent.
'''
def test_eq():
    peep1 = Peep(2, 1, '23/05/23 12:00:00', 'Just reset chitter...')
    peep2 = Peep(2, 1, '23/05/23 12:00:00', 'Just reset chitter...')
    assert peep1 == peep2