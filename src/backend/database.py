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
        