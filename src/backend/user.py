from backend.database import Database

class User(Database):
    def __init__(self, user_id: int, username: str) -> None:
        super().__init__()
        
        self.check_user(user_id, username)
        
        self.user_id: int = user_id
        self.username: str = username
    
    def check_user(self, user_id: int, username: str) -> None:
        count_same_query = f"SELECT COUNT(*) FROM Users WHERE id={user_id} AND username='{username}'"
        count_id_query = f"SELECT COUNT(*) FROM Users WHERE id={user_id}"
        
        self.cursor.execute(count_id_query)
        
        if self.cursor.fetchone()[0] == 1:
            self.cursor.execute(count_same_query)
            if self.cursor.fetchone()[0] == 1:
                ...
            else:
                self.cursor.execute(f"UPDATE Users SET username='{username}' WHERE id={user_id}")
                self.connection.commit()
        else:
            self.cursor.execute(f"INSERT INTO Users (id, username) VALUES ({user_id}, '{username}')")
            self.connection.commit()
        
        
    @property
    def user_info(self):
        return f"{self.username}:{self.user_id}"