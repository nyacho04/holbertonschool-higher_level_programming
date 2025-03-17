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
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name)

    cursor = db.cursor()

    query = "SELECT cities.name FROM cities \
            JOIN states ON cities.state_id = states.id \
            WHERE states.name = %s ORDER BY cities.id ASC"
    cursor.execute(query, (state_name,))

    rows = cursor.fetchall()

    city_names = [row[0] for row in rows]
    print(", ".join(city_names))

    cursor.close()
    db.close()
