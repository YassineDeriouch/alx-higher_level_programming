#!/usr/bin/python3
'''
that lists all states from database where name matches the argument.
'''

import MySQLdb
import sys


def search_states(username, password, database, state_name):
    try:
        db = MySQLdb.connect(
            host="localhost", port=3306,
            user=username, passwd=password, db=database
        )
        cursor = db.cursor()
        sql_query = "SELECT * FROM states WHERE name=%s ORDER BY id ASC;"
        cursor.execute(sql_query, (state_name,))
        results = cursor.fetchall()
        for row in results:
            print(row)
        cursor.close()
        db.close()
    except MySQLdb.Error as e:
        print("MySQL Error:", e)
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python script.py <username> <password> <database>"
              " <state_name>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    search_states(username, password, database, state_name)
