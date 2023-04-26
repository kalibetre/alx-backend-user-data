#!/usr/bin/env python3
"""
Filtered Logger module
"""
import re
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """
    A function that returns a log message obfuscated
    """
    return separator.join([
        re.sub(r'=([^=]*)', f'={redaction}', v)
        if v.split('=')[0] in fields else v for v in message.split(separator)
    ])
