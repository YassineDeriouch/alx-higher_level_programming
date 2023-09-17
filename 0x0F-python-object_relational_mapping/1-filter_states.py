#!/usr/bin/python3
"""python script to lists all states with a name starting with letter N in hbtn_0e_0_usa DB"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(
        user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], port=3306)

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%';")

    states = cur.fetchall()
    for state in states:
        print(state)
