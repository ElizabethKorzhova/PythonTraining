"""This module provides utility functions"""
import sqlite3

def connect_db(db_name: str) -> sqlite3.Cursor:
    """
    Connects to sqlite database and returns cursor object

    Args:
        db_name (str): name of database
    Returns:
        cursor: cursor object
    """
    with sqlite3.connect(db_name) as connection:
        return connection.cursor()
