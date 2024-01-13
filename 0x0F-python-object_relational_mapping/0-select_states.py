#!/usr/bin/python3
"""lists all states from database"""
import sys
import MySQLdb


def list_states(username, password, database):
    """list all states from database"""

    db = MySQLdb.connect
    (
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
    )
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    rows = cursor.fetchall()

    for row in rows:
        print(row)
    db.close()

if __name__ = '__main__':
    list_states(sys.argv[1], sys.argv[2], sys.argv[3])
