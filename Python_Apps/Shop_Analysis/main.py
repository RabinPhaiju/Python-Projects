import psycopg2
from psycopg2 import sql
import datetime
import numpy as np

def credentials():
    conn = psycopg2.connect("""
    dbname='shop_data_analysis'
    user ='postgres'
    password='rabina00'
    host='localhost'
    port= '5432'
    """)
    return conn


def create_table():
    conn = credentials()
    cur = conn.cursor()
    cur.execute('CREATE TABLE If NOT EXISTS store(id serial PRIMARY KEY,date DATE,time TIME,item_id INTEGER,quantity INTEGER,price REAL,type_id INTEGER,cus_id INTEGER)')
    conn.commit()
    conn.close()


def insert_into_table(date,time,item_id,quantity,price,type_id,cus_id):
    conn = credentials()
    cur = conn.cursor()
    cur.execute('INSERT INTO store(date,time,item_id,quantity,price,type_id,cus_id) VALUES (%s,%s,%s,%s,%s,%s,%s)' ,(date,time,item_id,quantity,price,type_id,cus_id))
    conn.commit()
    conn.close()


def view_from_table():
    conn = credentials()
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows

def get_column(col_name):
    conn = credentials()
    cur = conn.cursor()
    cur.execute(sql.SQL("SELECT {} from store").format(sql.Identifier(col_name)))
    rows = cur.fetchall()
    conn.close()
    return rows


def delete_from_table(id):
    conn = credentials()
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE id=%s",(id,))
    conn.commit()
    conn.close()


def update_table(date,time,item_id,quantity,price,type_id,cus_id,id):
    conn = credentials()
    cur = conn.cursor()
    cur.execute("UPDATE store SET date=%s, time=%s, item_id=%s, quantity=%s, price=%s, type_id=%s, cus_id=%s WHERE id =%s",(date,time,item_id,quantity,price,type_id,cus_id,id))
    conn.commit()
    conn.close()

# ----- Must run -----
create_table()
date = datetime.datetime.now().date()
time = datetime.datetime.now().time()

# ----- choose and run ------
# insert_into_table(date,time,103,62,44,4,13)
# delete_from_table(3)
# update_table(date,time,103,6,1000,4,13, 3 )
    
# ----- run to view data -----
# for row in view_from_table():
#     print(row)

# ------- run to calculate co. of correlation ------
price  = np.array([ x[0] for x in get_column('price')])
quantity  = np.array([ x[0] for x in get_column('quantity')])
co_of_correlation = np.corrcoef(price,quantity)
co_of_correlation = co_of_correlation[0].tolist()
print(round(co_of_correlation[1],2))