#!/usr/bin/python3
'''
that lists all states from database where name matches the argument.
'''
import MySQLdb
from sys import argv


def all_states_filter_entry():
    username, password, database_name, state_name = argv[1:5]
    state_name = state_name.split(';')[0].strip("'")
    conn = MySQLdb.connect(
                           host="localhost",
                           port=3306,
                           user=username,
                           passwd=password,
                           db=database_name,
                           charset="utf8"
                            )
    cur = conn.cursor()
    cur.execute("""
                SELECT * FROM states
                WHERE states.name = Binary('{}')
                ORDER BY id ASC
                """.format(state_name)
                )
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()


if __name__ == '__main__':
    all_states_filter_entry()
