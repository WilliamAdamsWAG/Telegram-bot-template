import sqlite3

class Database:
    def __init__(self) -> None:
        self.connection = sqlite3.connect("src/storage/database.db")
        self.cursor = self.connection.cursor()
        
        self.create_users_table()
        
        self.connection.commit()
        
    def create_users_table(self) -> None:
        self.cursor.execute('''
                        CREATE TABLE IF NOT EXISTS Users (
                        id INTEGER PRIMARY KEY,
                        username TEXT NOT NULL
                        )
                        ''')
        self.connection.commit()
        
    def count_users(self, *, condition: list[str | int] = None) -> int:
        if condition is None:
            self.cursor.execute("SELECT COUNT(*) FROM Users")
            return self.cursor.fetchone()[0]
        else:
            self.cursor.execute(f"SELECT COUNT(*) FROM Users WHERE {list[0]} = {list[1]}")
            return self.cursor.fetchone()[0]
        