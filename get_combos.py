import os
import sys

import psycopg2
from dotenv import load_dotenv

#Load environment variables from the .env file into the program
load_dotenv()

#Read each database connection value from the environment (.env file)and store it in a Python variable so we can use it later
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")
db_name = os.getenv("DB_NAME")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")

#The SQL query we want to run against the database
QUERY = """SELECT canonical_value_keys, combo_odds FROM betbuilder.combo_price_current WHERE source_received_at::date = CURRENT_DATE;"""

def main():

    #Start with no connection object
    conn = None
    try:
        #Attempt to open connection to the PostgreSQL database using the credentials we loaded from .env
        conn = psycopg2.connect(host=db_host, port=db_port, dbname=db_name, user=db_user, password=db_password)

        #A "cursor" is the object we use to send SQL commands to the database and retrieve results
        cur = conn.cursor()

        #Execute our SQL query on the database
        cur.execute(QUERY)

        #We extract just the column names so we know what each value in a row represents
        colnames = [desc[0] for desc in cur.description]
        print(colnames)

        #Fetch all the rows returned by the query and store them in a list called "rows"
        rows = cur.fetchall()

        #Loop through each row in the results and print it out, one row at a time
        for row in rows:
            print(row)

        #Print how many rows were returned in total
        print(f"\nResults Total: {len(rows)}")

        #Close the cursor since we are done using it
        cur.close()

    except Exception as e:
        #If anything goes wrong, catch the error here instead of crashing and print a message about it
        print("There is an error:", e)

    finally:
        if conn is not None:
            #If connection was successfully opened, close it properly to avoid leaving open connections to the database
            conn.close()

#This checks whether this file is being run directly
#If so, call the mai() function to actually start the program
if __name__ == "__main__":
    main()
