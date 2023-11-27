#!/usr/bin/python3
"""
Displays all cities from database
"""
import MySQLdb
import sys


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    databases = sys.argv[3]
    state_name_searched = sys.argv[4]

    db = MySQLdb.connect(
        host='localhost',
        user=username,
        passwd=password,
        db=databases,
        port=3306
    )

    cur = db.cursor()
    table_rows = cur.execute(
        "SELECT cities.id, cities.name, states.name FROM cities\
            JOIN states ON cities.state_id = states.id\
                WHERE states.name = '{}';".format(state_name_searched))
    cities = cur.fetchall()

    i = 1
    for city in cities:
        print(city[1], end='')
        if i < table_rows:
            print(end=', ')
        i += 1
    print()
