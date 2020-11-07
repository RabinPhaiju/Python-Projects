import psycopg2 

def credentials():
    conn = psycopg2.connect("""
    dbname='PostgreSQL_Python'
    user ='postgres'
    password='rabina00'
    host='localhost'
    port= '5432'
    """)
    return conn


def create_table():
    conn = credentials()
    cur = conn.cursor()
    cur.execute('CREATE TABLE If NOT EXISTS store(item TEXT, quantity INTEGER, price REAL)')
    conn.commit()
    conn.close()


def insert_into_table(item, quantity, price):
    conn = credentials()
    cur = conn.cursor()
    cur.execute('INSERT INTO store VALUES (%s,%s,%s)' ,(item, quantity, price))
    conn.commit()
    conn.close()


def view_from_table():
    conn = credentials()
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows


def delete_from_table(item):
    conn = credentials()
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item=%s",(item,))
    conn.commit()
    conn.close()


def update_table(item, quantity, price):
    conn = credentials()
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity=%s, price=%s WHERE item =%s",(quantity, price, item))
    conn.commit()
    conn.close()


create_table()
insert_into_table("Water", 23, 3434.3)
# delete_from_table('Water')
update_table('Water', 10, 10.95)
    
values = view_from_table()
for row in values:
    print(row)

