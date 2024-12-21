""" MIT License

Copyright (c) 2024 WilliamAdamsWAG

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

"""
import sqlite3

class Database:
    """ Database
    Simple interface

    """
    def __init__(self) -> None:
        self.connection = sqlite3.connect("src/storage/database.db")
        self.cursor = self.connection.cursor()

        self.create_users_table()

        self.connection.commit()

    def create_users_table(self) -> None:
        """ Create users table in databse """
        self.cursor.execute('''
                        CREATE TABLE IF NOT EXISTS Users (
                        id INTEGER PRIMARY KEY,
                        username TEXT NOT NULL
                        )
                        ''')
        self.connection.commit()

    def count_users(self, *, condition: list[str | int] = None) -> int:
        """ Count users in databse """
        if condition is None:
            self.cursor.execute("SELECT COUNT(*) FROM Users")
            return self.cursor.fetchone()[0]

        self.cursor.execute(f"SELECT COUNT(*) FROM Users WHERE {list[0]} = {list[1]}")
        return self.cursor.fetchone()[0]
