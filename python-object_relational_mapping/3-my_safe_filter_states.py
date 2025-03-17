#!/usr/bin/python3
"""
this script lists all states from the database
"""

import MySQLdb
import sys

if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name_searched = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name)

    cursor = db.cursor()

    query = "SELECT * FROM states WHERE BINARY name = %s ORDER BY id ASC"
    cursor.execute(query, (state_name_searched,))

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
