#!/usr/bin/env python3
"""
BasicAuth module for the API
"""
from uuid import uuid4

from api.v1.auth.auth import Auth


class SessionAuth(Auth):
    """A session auth class to manage the API authentication"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Creates a Session ID for a user_id"""
        if user_id is None or type(user_id) != str:
            return None
        session_id = str(uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id
