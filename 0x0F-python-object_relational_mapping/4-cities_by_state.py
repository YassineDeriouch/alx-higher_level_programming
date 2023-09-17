#!/usr/bin/python3
"""Python script to list all
states with a name starting
with letter N in hbtn_0e_0_usa DB
safe from MySQL injections!
"""
import MySQLdb
import sys

if __name__ == '__main__':
    if len(sys.argv) != 5:
        print("Usage: python script.py\
            <username> <password> <database> <state_name>")
    else:
        username,
        password,
        database,
        state_name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

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
                SELECT cities.name
                FROM cities
                JOIN states ON cities.state_id = states.id
                WHERE states.name = %s
                ORDER BY cities.id ASC;
            """, (state_name,))

            rows = cur.fetchall()

            if rows:
                cities = [row[0] for row in rows]
                print(", ".join(cities))

        except MySQLdb.Error as e:
            print("MySQL Error:", e)
        finally:
            if 'cur' in locals():
                cur.close()
            if 'db' in locals():
                db.close()
