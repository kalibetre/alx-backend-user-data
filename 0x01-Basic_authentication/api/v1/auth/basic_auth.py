#!/usr/bin/env python3
"""
BasicAuth module for the API
"""
from base64 import b64decode
from typing import Tuple

from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """A basic auth class to manage the API authentication"""

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """
        Returns the base64 part of the Authorization header for a Basic Auth
        """
        if authorization_header is None or type(
                authorization_header
        ) is not str or authorization_header[:6] != 'Basic ':
            return None
        return authorization_header[6:]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """
        Returns the decoded value of a Base64 string
        """
        if base64_authorization_header is None or type(
                base64_authorization_header) is not str:
            return None
        try:
            b64_bytes = b64decode(base64_authorization_header)
            return b64_bytes.decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> Tuple[str, str]:
        """
        Extracts and returns the user credentials from the decoded Base64
        string
        """
        if decoded_base64_authorization_header is None or type(
                decoded_base64_authorization_header
        ) is not str or ':' not in decoded_base64_authorization_header:
            return (None, None)
        return tuple(decoded_base64_authorization_header.split(':', 1))
