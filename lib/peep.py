class Peep:
    def __init__(self, id, user_id, post_date, content, tags = None ):
        self.id = id
        self.user_id = user_id
        self.post_date = post_date
        self.content = content
        self.tags = tags or ""

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"Peep by user {self.user_id} at {self.post_date}: {self.content} #{self.tags}"