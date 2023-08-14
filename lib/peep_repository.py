from lib.peep import Peep
from datetime import datetime

class PeepRepository():
    def __init__(self,connection):
        self._connection = connection

    def list_all_peeps(self):
        rows = self._connection.execute('SELECT users.user_handle, users.name_of_user, peeps.post_time, peeps.content, peeps.tags FROM peeps JOIN users on users.id = peeps.user_id ORDER BY post_time DESC')
        return self.list_peeps_formatting(rows)
    
    def peeps_by_user(self, id):
        rows = self._connection.execute('SELECT users.user_handle, users.name_of_user, peeps.post_time, peeps.content, peeps.tags FROM peeps JOIN users on users.id = peeps.user_id WHERE user_id = %s ORDER BY post_time DESC', [id])
        return self.list_peeps_formatting(rows)
    
    def create_peep(self, user_id, content, tags = None):
        post_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        if tags == None:
            self._connection.execute('INSERT INTO peeps (user_id, post_time, content) VALUES(%s,%s,%s)',[user_id, post_time, content])
        else:
            self._connection.execute('INSERT INTO peeps (user_id, post_time, content, tags) VALUES(%s,%s,%s,%s)',[user_id, post_time, content, tags])
        return None
    
    def list_peeps_formatting(self, rows):
        peeps_for_display = []
        for row in rows:
            item = f"Peep by {row['user_handle']} ({row['name_of_user']}) at {row['post_time'][11:16]} on {row['post_time'][0:6]}{row['post_time'][8:10]}: {row['content']}"
            if row['tags'] != None:
                tags_list = row['tags'].split(', ')
                for tag in tags_list:
                    item += ' #' + tag
            peeps_for_display.append(item)
        return peeps_for_display