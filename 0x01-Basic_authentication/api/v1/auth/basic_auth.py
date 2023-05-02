#!/usr/bin/env python3
"""
BasicAuth module for the API
"""
from typing import List, TypeVar

from api.v1.auth.auth import Auth
from flask import request


class BasicAuth(Auth):
    """A basic auth class to manage the API authentication"""

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """
        Returns the base64 part of the Authorization header 
        """
        if authorization_header is None or type(
                authorization_header
        ) is not str or authorization_header[:6] != 'Basic ':
            return None
        return authorization_header[6:]
