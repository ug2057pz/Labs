"""
A menu - you need to add the database and fill in the functions. 
"""
# Import sqlite3 library 
import sqlite3

# Connect to the database 
conn = sqlite3.connect('chainsaw_records.db')

def main():
    menu_text = """
    1. Display all records
    2. Search by name
    3. Add new record
    4. Edit existing record
    5. Delete record 
    6. Quit
    """

    while True:
        print(menu_text)
        choice = input('Enter your choice: ')
        if choice == '1':
            display_all_records()
        elif choice == '2':
            search_by_name()
        elif choice == '3':
            add_new_record()
        elif choice == '4':
            edit_existing_record()
        elif choice == '5':
            delete_record()
        elif choice == '6':
            break
        else:
            print('Not a valid selection, please try again')

# Create a table in the database
db = 'records_db.sqlite'

def create_table():
    with sqlite3.connect('records_db.sqlite') as conn:
        conn.execute ('''CREATE TABLE IF NOT EXISTS records (name TEXT, country TEXT, num_catches INTEGER)''')
    conn.close()

# Insert data into the table 
def insert_data():
    with sqlite3.connect('records_db.sqlite') as conn:
        conn.execute("INSERT INTO records VALUES ('Janne Mustonen', 'Finland', 98)")
        conn.execute("INSERT INTO records VALUES ('Ian Stewart', 'Canada', 94)")
        conn.execute("INSERT INTO records VALUES ('Aaron Gregg', 'Canadian', 88)")
        conn.execute("INSERT INTO records VALUES ('Chad Taylor', 'deer', 78)")
    conn.close()
    
def display_all_records():
        with sqlite3.connect('records_db.sqlite') as conn:
            results = conn.execute("SELECT name, country, num_catches FROM records")
        for row in results:
            print('Name: {}, Country: {}, Number of Catches: {}'.format(row[0], row[1], row[2]))
    
        conn.close()


def search_by_name(name):
    name_search = input('please enter a name to search')
    with sqlite3.connect('records_db.sqlite') as conn:
        results = conn.execute("SELECT name, country, num_catches FROM records WHERE name=?", (name,))
    row = results.fetchone()
    if row:
       print('Name: {}, Country: {}, Number of Catches: {}'.format(row[0], row[1], row[2]))
    else:
       print('Record not found')
    conn.close

def add_new_record():
    name = input('Enter name: ')
    country = input('Enter country: ')
    num_catches = input('Enter number of catches: ')
    with sqlite3.connect('records_db.sqlite') as conn:
        conn.execute(f'INSERT INTO records VALUES (?, ?, ?)', (name, country, num_catches))
    conn.close()

def edit_existing_record():
   name = input('Enter name of record to edit: ')
   with sqlite3.connect('records_db.sqlite') as conn:
        results = conn.execute("SELECT name, country, num_catches FROM records WHERE name=?", (name,))
   row = results.fetchone()
   if row:
       country = input('Enter new country ({}): '.format(row[1]))
       num_catches = input('Enter new number of catches ({}): '.format(row[2]))
       conn.execute("UPDATE records SET country=?, num_catches=? WHERE name=?", (country, num_catches, name))
       conn.close()
   else:
       print('Record not found')
       conn.close
def delete_record():
    name = input('Enter name of record to delete: ')
    with sqlite3.connect('records_db.sqlite') as conn:
        results = conn.execute("SELECT name, country, num_catches FROM records WHERE name=?", (name,))
    row = results.fetchone()
    if row:
       conn.execute("DELETE FROM records WHERE name=?", (name,))
       conn.commit()
    else:
       print('Record not found')
    conn.close

if __name__ == '__main__':
    create_table()
    main()
