#!/usr/bin/python3
"""
Module to list all cities from database
"""
import MySQLdb
import sys


if __name__ == "__main__":
    """Function that lists all cities database"""

    cnx = MySQLdb.connect(
        host="localhost",
        port=3306,
        charset="utf8",
        user=sys.argv[1],
        passwd=sys.argv[2],
        database=sys.argv[3])

    cur = cnx.cursor()

    cur.execute("SELECT cities.id, cities.name, states.name FROM cities\
                INNER JOIN states ON cities.state_id = states.id\
                ORDER BY cities.id ASC")

    query_rows = cur.fetchall()

    for row in query_rows:
        print(row)

    cur.close()

    cnx.close()
