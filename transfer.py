

import pandas as pd
import csv
import sqlite3
import random as rd

"""seen = []
time = []

for i in range(600):
    per = ""
    x1 = rd.randrange(1, 24)
    x2 = rd.randrange(1, 60)
    sec = rd.randrange(1, 60)
    if x1 < 12:
        per = "AM"
    else:
        per = "PM"

    if len(str(x1)) == 1:
        x1 = "0" + str(x1)
    if len(str(x2)) == 1:
        x2 = "0" + str(x2)
    if len(str(sec)) == 1:
        sec = "0" + str(sec)

    full = "20220309" + str(x1) + str(x2)
    t = "2022-03-09" + " "+ str(x1) + ":" + str(x2) + ":" + str(sec) + " " + per
    time.append(t)
    seen.append(full)
    
set_seen = set(seen)
set_time = set(time)
ls = list(set_seen)
ls_time = list(set_time)

# formated day

d = "2022-03-09"

path = "omar_stock.xlsx"
path2 = "omar_stock.csv"

conn = sqlite3.connect("store.db")
with conn:
    conn.execute("DELETE FROM store1")

new = []

data = pd.read_excel(path, header  = None)
data.to_csv(path2, index = None, header = True)



with open("omar_stock.csv", "r") as file:
    read = csv.reader(file)
    # ITERATE
    index = 0
    for row in read:
        row[10] = "2022-03"
        row[9] = d
        row[12] = ls[index]
        row[5] = ls_time[index]
        new.append(row)
        index += 1
del new[0]
del new[1]
del new[2]
del new[0]

with conn:
    conn.executemany("INSERT INTO store1 VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)", new)
    print("transfer is done successfully!")"""

# COMPARE STORE
def add_rest():
    new = []
    conn1 = sqlite3.connect("store2.db")
    with conn1:
        data = conn1.execute("SELECT * FROM store1")
        for row in data.fetchall():
            new.append(row)
    new = list(set(new))
    conn = sqlite3.connect("store.db")
    with conn:
        conn.executemany("INSERT INTO store1 VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)", new)
        print("transfer is done successfully!")


# OPEN STORE
sold = {}

def all_sales():
    conn = sqlite3.connect("sales.db")
    with conn:
        all_data = conn.execute("SELECT item, qty FROM sales1")
        return all_data.fetchall()
Sales = all_sales()

for row in Sales:
    if row[0] not in sold.keys():
        sold.setdefault(row[0], row[1])
    else:
        sold[row[0]] += row[1]
        

stock = []
def all_store():
    conn = sqlite3.connect("store.db")
    with conn:
        data = conn.execute("SELECT * FROM store1")
        for row in data.fetchall():
            stock.append(list(row))
#all_store()
#print(stock)

for row in stock:
    if row[0] in sold.keys():
        row[1] = row[1] - sold[row[0]]

def update():
    conn = sqlite3.connect("store.db")
    with conn:
        conn.execute("DELETE FROM store1")

    with conn:
        conn.executemany("INSERT INTO store1 VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)", stock)
    
#update()
add_rest()