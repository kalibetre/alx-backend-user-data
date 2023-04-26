#!/usr/bin/env python3
"""
Filtered Logger module
"""
import logging
import re
from typing import List

PII_FIELDS = ['name', 'email', 'phone', 'ssn', 'password']


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """
    A function that returns a log message obfuscated
    """
    return separator.join([
        re.sub(r'=([^=]*)', f'={redaction}', v)
        if v.split('=')[0] in fields else v for v in message.split(separator)
    ])


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str] = None):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """filters incoming records using filter_datum
        """
        return filter_datum(self.fields, self.REDACTION,
                            super().format(record), self.SEPARATOR)


def get_logger() -> logging.Logger:
    """returns a logging.Logger object"""
    logger = logging.getLogger('user_data')
    logger.setLevel(logging.INFO)
    logger.propagate = False

    handler = logging.StreamHandler()
    handler.setFormatter(RedactingFormatter(PII_FIELDS))
    logger.addHandler(handler)
    return logger
