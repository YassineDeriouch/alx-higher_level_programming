#!/usr/bin/python3
"""python script to lists all states with a name starting with letter N in hbtn_0e_0_usa DB"""
from sys import argv
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(
        user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], port=3306)

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY states.id ASC")
    states = cursor.fetchall()
    for state in states:
        print(state)
