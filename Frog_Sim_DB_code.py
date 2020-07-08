import sqlite3
#import Frog_Sim_Code as FSC

print("running DB")

def delete_all_rows():
    Cursor.execute("DELETE FROM Frog_table")
    Frog_DB.commit()
    print("All rows in table have been deleted")

def delete_single_row(Name):
    # if the row with that name does not exist in the DB (hasn't been saved yet), there are still no errors
    Cursor.execute("DELETE FROM Frog_table WHERE Name = ?", (Name,))
    Frog_DB.commit()
    print("The row with {} has been deleted".format(Name))


def get_frog(Name):
    Cursor.execute("SELECT * FROM Frog_table WHERE Name = ?", (Name,))
    return Cursor.fetchone()

def get_all_frog():
    Cursor.execute("SELECT * FROM Frog_table")

    return Cursor.fetchall()

def printFrogDB():
    """
    * means all. You could instead do
    SELECT * FROM Frog_table WHERE Name = Kelli
    but then you would just the the row of Kelli's values
    """
    result = Cursor.execute("SELECT * FROM Frog_table")

    print(Cursor.fetchall())

def insert(Name, Gender, Health, Mate, Offsprings):
    # checking if data row for the same name has already been saved,
    # if data for the same name IS in the db, then it deletes that row
    # so new data row for that name can replace it
    Cursor.execute("SELECT * FROM Frog_Table WHERE Name = ?", (Name,))
    if Cursor.fetchall() == []:
        print("Not in system yet, proceed")
    else:
        print("Already in system, will delete now")
        Cursor.execute("DELETE FROM Frog_table WHERE Name = ?", (Name,))
        Frog_DB.commit()
        print("Past row with name deleted, may now proceed")

    Cursor.execute("INSERT INTO Frog_table VALUES (?, ?, ?, ?, ?)", (Name, Gender, Health, Mate, Offsprings))

    Frog_DB.commit()
    print("New Frog values inserted")
    printFrogDB()


def closeDB():
    Frog_DB.close()
    print("Database closed")

"""
if Frog_DB is already created, then this will just
connect to the already created Frog_DB, so no need to 
drop the db if it already exists like we do with tables
"""
"""
putting :memory: instead of a file name makes it so that
the DB will be in ram not in a file. This makes it so that
every time you run the code, it will be a fresh DB and you
don't have to worry about creating a table that already exists
or inserting values that you already inserted
"""
Frog_DB = sqlite3.connect("Frog_DB_file.db")
print("Database created")

Cursor = Frog_DB.cursor()
print("Cursor created")

Cursor.execute("""CREATE TABLE IF NOT EXISTS Frog_table (
                Name TEXT,
                Gender TEXT,
                Health INT,
                Mate TEXT,
                Offsprings TEXT)""")

Frog_DB.commit()
print("Table created")



