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
from backend.database import Database

class User(Database):
    """ User
    Simple user interface

    """
    def __init__(self, user_id: int, username: str) -> None:
        super().__init__()

        self.check_user(user_id, username)

        self.user_id: int = user_id
        self.username: str = username

    def check_user(self, user_id: int, username: str) -> None:
        """ Check user exist """
        count_same_query = "SELECT COUNT(*) FROM Users" \
                          f"WHERE id={user_id} AND username='{username}'"
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
            self.cursor.execute("INSERT INTO Users (id, username)" \
                                f"VALUES ({user_id}, '{username}')")
            self.connection.commit()

    @property
    def user_info(self):
        """ get user info username:id """
        return f"{self.username}:{self.user_id}"
