from backend.database import Database

class User(Database):
    def __init__(self, user_id: int, username: str):
        print(1)
        super().__init__()
        
        if self.cursor.execute(f"SELECT COUNT(*) FROM Users WHERE id={user_id}").fetchone()[0] == 0:
            self.cursor.execute(f"INSERT INTO Users (id, username) VALUES ({user_id}, '{username}')")
            self.connection.commit()
        else:
            ...
        
        self.user_id = user_id
        self.username = username
        
    @property
    def user_info(self):
        return f"{self.username}:{self.user_id}"