#!/usr/bin/env python3
"""
Auth module for the API
"""
from typing import List, TypeVar

from flask import request


class Auth:
    """A class to manage the API authentication"""

    def require_auth(self, path: str, exclude_paths: List[str]) -> bool:
        """
        Require authentication for all the paths except the ones in
        exclude_paths
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
        Return the value of the header request Authorization
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Return the current user
        """
        return None
