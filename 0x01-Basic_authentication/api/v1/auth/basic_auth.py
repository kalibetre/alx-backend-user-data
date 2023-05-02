#!/usr/bin/env python3
"""
BasicAuth module for the API
"""
from typing import List, TypeVar

from api.v1.auth.auth import Auth
from flask import request


class BasicAuth(Auth):
    """A basic auth class to manage the API authentication"""
    pass
