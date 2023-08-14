from lib.user import User

class UserRepository():
    def __init__(self,connection):
        self._connection = connection
        self.generated_errors = ""

    def login_user(self, username, user_password):
        self._login_form_is_valid(username, user_password)
        if self.generated_errors != "":
            return User(None, None, None, None, None)
        user = self.find_user(username)
        if user.user_password == user_password:
            return user
        else:
            self.generated_errors += "Incorrect password. "
            return User(None, None, None, None, None)
        
    def _login_form_is_valid(self, username, user_password):
        if username == "":
            self.generated_errors += "Username missing. "
        valid_usernames = [row['user_handle'] for row in self._connection.execute('SELECT user_handle FROM users')]
        if username != "" and username not in valid_usernames:
            self.generated_errors += "Incorrect username. "
        if user_password == "":
            self.generated_errors += "Password missing. "
        return None

        
    def find_user(self, user_handle):
        rows = self._connection.execute('SELECT * FROM users WHERE user_handle = %s',[user_handle])
        row = rows[0]
        user = User(row['id'], row['user_handle'], row['name_of_user'], row['email'], row['user_password'])
        return user
    

