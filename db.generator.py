# -*- coding: utf-8 -*-
"""hacthonLadies_2023_sql_DB.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bB6zwdNa_iyoyE0FoznHn3-oYZfvhXqM

# **Creat SQL database**
"""

import sqlite3

# Create a connection to the database (or open an existing one)
conn = sqlite3.connect('WingWalker_database.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create a table with five columns
cursor.execute('''CREATE TABLE IF NOT EXISTS first_table(
                    seiral_number INTEGER PRIMARY KEY,
                    Product_Name TEXT,
                    manufacturar TEXT,
                    material TEXT,
                    production_year INTEGER,
                    expiration INTEGER)''')
# Save the changes and close the connection
conn.commit()
conn.close()

print("Database created successfully!")

"""# **Add information to our SQL database**"""

import sqlite3

# Open a new connection to the database
conn = sqlite3.connect('WingWalker_database.db')
cursor = conn.cursor()

# Define a list of rows to insert
rows = [
    (1079111,	'Wing',	'Airbus',	'Carbonfiber',	2020,	2025),
    (3210000,	'Stabilizer',	'Airbus',	'Aluminium',	2020,	2025),
    (1391000,	'Jet Engine',	'Airbus',	'Gold',	2019,	2030),
    (1822333,	'Cockpit',	'Airbus',	'Steel',	2020,	2025),
    (1222988,	'Fuselage',	'Airbus',	'Carbonfiber',	2020,	2025),
    (2001111,	'Elevator',	'Airbus',	'Aluminium',	2020,	2025)
]

# Insert multiple rows into the table
cursor.executemany("INSERT INTO first_table (seiral_number, Product_Name, manufacturar, material, production_year,expiration) VALUES (?, ?, ?, ?, ?, ?)", rows)

# Save the changes and close the connection
conn.commit()
conn.close()

print("Data added successfully!")

"""# **present our database**"""

# Open a new connection to the database
conn = sqlite3.connect('WingWalker_database.db')
cursor = conn.cursor()

# Retrieve all rows from the table
cursor.execute("SELECT * FROM first_table")
rows = cursor.fetchall()

# Display the data
for row in rows:
    print("seiral_number", row[0])
    print("Product_Name:", row[1])
    print("manufacturar:", row[2])
    print("material:", row[3])
    print("production_year:", row[4])
    print("expiration:", row[5])
    print("-------------------")

# Close the connection
conn.close()
