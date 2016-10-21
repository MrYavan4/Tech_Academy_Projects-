# Python Version 3.6.0
#
# Author: Tanvir Khondakar
#
# Practicing with Sqlite by creating a roster of people

import sqlite3

roster_value = (

    ("Jean-Baptise Zorg", "Human", 122),
    ("Korben Dallas", "Meat Popsicle", 100),
    ("Ak'not", "Mangalore", -5)
    
    )

connection = sqlite3.connect(':memory:') # Connecting to one time use database

with sqlite3.connect('test.db') as connection:

    c = connection.cursor()

    c.execute("DROP TABLE IF EXISTS Roster")

    c.execute("CREATE TABLE Roster(Name TEXT, Species TEXT, IQ INT)")

    c.executemany("INSERT INTO Roster VALUES(?,?,?)", roster_value)

    c.execute("UPDATE Roster SET Species=? WHERE Name=? AND IQ=?",
              ("Human","Korben Dallas", 100))

# Select names and IQs of everyone in the table who is classified as Human\

    c.execute("SELECT Name, IQ FROM Roster WHERE Species == 'Human'")

    for row in c.fetchall():
        print(row)
