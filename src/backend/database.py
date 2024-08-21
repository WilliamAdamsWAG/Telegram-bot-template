import sqlite3

class Database:
    def __init__(self) -> None:
        self.connection = sqlite3.connect("src/storage/database.db")
        self.cursor = self.connection.cursor()
        
        self.connection.commit()
        
    def create_users_table(self):
        self.cursor.execute('''
                        CREATE TABLE IF NOT EXISTS Users (
                        id INTEGER PRIMARY KEY,
                        username TEXT NOT NULL
                        )
                        ''')
        self.cursor.execute("INSERT INTO Users (id, username) VALUES (3, 'william')")
        self.connection.commit()
        x = self.cursor.execute("SELECT COUNT(*) FROM Users WHERE username='william'")
        print(x.fetchone()[0])
        
if __name__ == "__main__":
    x = Database().create_users_table()