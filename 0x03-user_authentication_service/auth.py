#!/usr/bin/env python3
"""
Auth Modules
"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """Hashes a plain string password"""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
