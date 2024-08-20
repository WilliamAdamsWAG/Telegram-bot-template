

class User:
    def __init__(self, user_id: int, username: str):
        self.user_id = user_id
        self.username = username
        
    @property
    def user_info(self):
        return f"{self.username}:{self.user_id}"