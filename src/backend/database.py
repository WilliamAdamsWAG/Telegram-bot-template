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
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from user import User

class Database:
    """ Provides simple database functionality.

    This class provides a basic interface for interacting with the database. It creates an engine
    for connecting to the database and offers methods for managing users.

    Attributes:
        ENGINE (sqlalchemy.engine.base.Engine): Engine used to connect to the database.

    Methods defined here:
        get_user:
            Retrieves a user by their ID and updates their name if necessary.

    """
    ENGINE = create_engine('sqlite:///database.db')
    session = None

    @staticmethod
    def get_user(user_id: int, username: str) -> User:
        """
        Retrieve a user by their ID and update their name if different.

        This function takes a user's ID and a new username as arguments. If a user with the
        specified ID exists, it updates their name to the provided one and returns the user
        object. If the name matches the current user's name, the existing user object is returned
        without changes.

        :param user_id: The user's ID.
        :type user_id: int
        :param username: The new username.
        :type username: str
        :return: The user object.
        :rtype: User

        """
        session_maker = sessionmaker(bind=Database.ENGINE)
        session = session_maker()

        # select user by id
        user = session.query(User).filter_by(id=user_id).first()

        # Update username if necessary and return User object
        if user.name == username:
            return user

        user.name = username
        session.commit()
        session.close()

        return user

    def __enter__(self):
        session_maker = sessionmaker(bind=self.ENGINE)
        self.session = session_maker()

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()
