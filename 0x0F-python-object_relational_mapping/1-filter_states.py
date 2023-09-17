#!/usr/bin/python3
"""python script to lists all states with a name starting with letter N in hbtn_0e_0_usa DB"""

import MySQLdb
import sys

def list_states_with_n(username, password, database):
    try:
        # Connect to MySQL server
        connection = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=username,
            passwd=password,
            db=database
        )

        # Create a cursor object to interact with the database
        cursor = connection.cursor()

        # Execute the SQL query to fetch states starting with 'N'
        query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
        cursor.execute(query)

        # Fetch all rows as a list of tuples
        states = cursor.fetchall()

        # Print the results
        for state in states:
            print(state)

    except MySQLdb.Error as e:
        print("MySQL Error:", e)
    finally:
        # Close the cursor and database connection
        cursor.close()
        connection.close()
