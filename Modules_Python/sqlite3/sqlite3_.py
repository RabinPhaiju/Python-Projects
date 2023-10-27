import sqlite3


def create_table():
    conn = sqlite3.connect('Modules_Python/sqlite3/lite.db')
    cur = conn.cursor()
    cur.execute('CREATE TABLE If NOT EXISTS store(item TEXT, quantity INTERGER, price REAL)')
    conn.commit()
    conn.close()


def insert_into_table(item, quantity, price):
    conn = sqlite3.connect('Modules_Python/sqlite3/lite.db')
    cur = conn.cursor()
    cur.execute('INSERT INTO store VALUES (?,?,?)',(item, quantity, price))
    conn.commit()
    conn.close()


def view_from_table():
    conn = sqlite3.connect('Modules_Python/sqlite3/lite.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows


def delete_from_table(item):
    conn = sqlite3.connect('Modules_Python/sqlite3/lite.db')
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item=?",(item,))
    conn.commit()
    conn.close()


def update_table(item, quantity, price):
    conn = sqlite3.connect('Modules_Python/sqlite3/lite.db')
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity=?, price=? WHERE item =?",(quantity, price, item))
    conn.commit()
    conn.close()


insert_into_table("Water", 23, 3434.3)
# delete_from_table('Wine')
# update_table('Water', 10, 10)
    
values = view_from_table()
for row in values:
    print(row)