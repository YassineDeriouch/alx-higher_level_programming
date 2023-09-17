#!/usr/bin/python3
"""Python script to list all states with a name starting with letter N in hbtn_0e_0_usa DB"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    if len(argv) != 4:
        print("Usage: python script.py <username> <password> <database>")
    else:
        username, password, database = argv[1], argv[2], argv[3]

        db = MySQLdb.connect(host="localhost", user=username, port=3306, passwd=password, db=database)

        cur = db.cursor()
        cur.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY states.id ASC;")
        rows = cur.fetchall()

        for row in rows:
            print(row)

        cur.close()
        db.close()
