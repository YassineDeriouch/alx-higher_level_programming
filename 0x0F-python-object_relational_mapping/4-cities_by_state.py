#!/usr/bin/python3

import MySQLdb
import sys

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database>")
    else:
        username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

        try:
            db = MySQLdb.connect(
                host="localhost",
                user=username,
                port=3306,
                passwd=password,
                db=database
            )

            cur = db.cursor()

            cur.execute("""
                SELECT cities.id, cities.name, states.name
                FROM cities
                JOIN states ON cities.state_id = states.id
                ORDER BY cities.id ASC;
            """)

            rows = cur.fetchall()

            for row in rows:
                print(row)

        except MySQLdb.Error as e:
            print("MySQL Error:", e)
        finally:
            if 'cur' in locals():
                cur.close()
            if 'db' in locals():
                db.close()
