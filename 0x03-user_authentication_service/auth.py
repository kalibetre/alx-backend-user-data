#!/usr/bin/env python3
"""
Auth Modules
"""
from uuid import uuid4

import bcrypt
from db import DB
from sqlalchemy.orm.exc import NoResultFound
from user import User


def _hash_password(password: str) -> bytes:
    """Hashes a plain string password"""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def _generate_uuid() -> str:
    """Generates a UUID"""
    return str(uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Registers a user with the given email and password

        raises:
            - ValueError if user already exists
        """
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            return self._db.add_user(email, _hash_password(password))

    def valid_login(self, email: str, password: str) -> bool:
        """validates the user email and password
        Returns:
            - True if user password id valued else False

        raises:
            - Exception if user does not exist or if other exception occurs
        """
        try:
            user = self._db.find_user_by(email=email)
            return bcrypt.checkpw(password.encode('utf-8'),
                                  user.hashed_password)
        except Exception:
            return False

    def create_session(self, email: str) -> str:
        """Creates a session ID for the user email
        Returns:
            - the session ID as a string
        """
        try:
            user = self._db.find_user_by(email=email)
            session_id = _generate_uuid()
            self._db.update_user(user.id, session_id=session_id)
            return session_id
        except Exception:
            return None

    def get_user_from_session_id(self, session_id: str) -> User:
        """Gets a user from a session ID
        Returns:
            - the user or None if the session ID is None or no user is found
        """
        try:
            if session_id is None:
                return None
            return self._db.find_user_by(session_id=session_id)
        except Exception:
            return None

    def destroy_session(self, user_id: int) -> None:
        """Destroys the session ID for the user ID
        Returns:
            - None
        """
        try:
            self._db.update_user(user_id, session_id=None)
        except Exception:
            pass
        return None
