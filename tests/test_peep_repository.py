from lib.peep_repository import PeepRepository
from lib.peep import Peep
from datetime import datetime

'''
Test that the list_all_peeps function returns a list of all peeps in reverse chronological order.
'''
def test_list_all_peeps(db_connection):
    db_connection.seed("seeds/chitter.sql")
    repository = PeepRepository(db_connection)
    peeps = repository.list_all_peeps()
    assert peeps == [
        'Peep by no_vowel_bot (Vowel Hater) at 17:21 on 24/05/23: Nw y gys r jst bng rd.',
        'Peep by telon_tusk (Telon Tusk) at 17:20 on 24/05/23: Now you guys are just being rude.',
        'Peep by telon_tusk (Telon Tusk) at 12:12 on 23/05/23: Wow, my peep is lonely, and so am I!',
        'Peep by telon_tusk (Telon Tusk) at 12:00 on 23/05/23: Just reset chitter...'
        ]

'''
Finds all peeps by a user id.
'''
def test_peeps_by_user(db_connection):
    db_connection.seed("seeds/chitter.sql")
    repository = PeepRepository(db_connection)
    peeps = repository.peeps_by_user(1)
    assert peeps == [
        'Peep by telon_tusk (Telon Tusk) at 17:20 on 24/05/23: Now you guys are just being rude.',
        'Peep by telon_tusk (Telon Tusk) at 12:12 on 23/05/23: Wow, my peep is lonely, and so am I!',
        'Peep by telon_tusk (Telon Tusk) at 12:00 on 23/05/23: Just reset chitter...'
        ]
    
'''
Create new peep without tags.
'''
def test_new_peep_no_tags(db_connection):
    db_connection.seed("seeds/chitter.sql")
    repository = PeepRepository(db_connection)
    post_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    print(post_time)
    repository.create_peep(1, 'My new peep')
    peeps = repository.list_all_peeps()
    assert peeps == [
        f'Peep by telon_tusk (Telon Tusk) at {post_time[11:16]} on {post_time[0:6]}{post_time[8:10]}: My new peep',
        'Peep by no_vowel_bot (Vowel Hater) at 17:21 on 24/05/23: Nw y gys r jst bng rd.',
        'Peep by telon_tusk (Telon Tusk) at 17:20 on 24/05/23: Now you guys are just being rude.',
        'Peep by telon_tusk (Telon Tusk) at 12:12 on 23/05/23: Wow, my peep is lonely, and so am I!',
        'Peep by telon_tusk (Telon Tusk) at 12:00 on 23/05/23: Just reset chitter...'
        ] 

'''
Create new peep with one tag.
'''
def test_new_peep_one_tag(db_connection):
    db_connection.seed("seeds/chitter.sql")
    repository = PeepRepository(db_connection)
    post_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    print(post_time)
    repository.create_peep(1, 'My new peep', 'no_vowel_bot')
    peeps = repository.list_all_peeps()
    assert peeps == [
        f'Peep by telon_tusk (Telon Tusk) at {post_time[11:16]} on {post_time[0:6]}{post_time[8:10]}: My new peep #no_vowel_bot',
        'Peep by no_vowel_bot (Vowel Hater) at 17:21 on 24/05/23: Nw y gys r jst bng rd.',
        'Peep by telon_tusk (Telon Tusk) at 17:20 on 24/05/23: Now you guys are just being rude.',
        'Peep by telon_tusk (Telon Tusk) at 12:12 on 23/05/23: Wow, my peep is lonely, and so am I!',
        'Peep by telon_tusk (Telon Tusk) at 12:00 on 23/05/23: Just reset chitter...'
        ] 

'''
Create new peep with multiple tags.
'''
def test_new_peep_multiple_tags(db_connection):
    db_connection.seed("seeds/chitter.sql")
    repository = PeepRepository(db_connection)
    post_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    print(post_time)
    repository.create_peep(1, 'My new peep', 'no_vowel_bot, myself, chitter')
    peeps = repository.list_all_peeps()
    assert peeps == [
        f'Peep by telon_tusk (Telon Tusk) at {post_time[11:16]} on {post_time[0:6]}{post_time[8:10]}: My new peep #no_vowel_bot #myself #chitter',
        'Peep by no_vowel_bot (Vowel Hater) at 17:21 on 24/05/23: Nw y gys r jst bng rd.',
        'Peep by telon_tusk (Telon Tusk) at 17:20 on 24/05/23: Now you guys are just being rude.',
        'Peep by telon_tusk (Telon Tusk) at 12:12 on 23/05/23: Wow, my peep is lonely, and so am I!',
        'Peep by telon_tusk (Telon Tusk) at 12:00 on 23/05/23: Just reset chitter...'
        ] 