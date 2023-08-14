class User():
    def __init__(self, id, user_handle, name_of_user, email, user_password, peeps = None):
        self.id = id 
        self.user_handle = user_handle
        self.name_of_user = name_of_user
        self.email = email
        self.user_password = user_password
        self.peeps = peeps or []

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"{self.user_handle} ({self.name_of_user})"
    

