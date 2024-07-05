import sqlite3 as st
import pandas as pd
import tkinter as tk
from tkinter import simpledialog
from tkinter import ttk

conn = st.connect('student.db')
cur = conn.cursor()

def create():
    cur.execute("DROP TABLE IF EXISTS student")
    cur.execute("""CREATE TABLE student (
                first_name text,
                last_name text,
                major text,
                grade INTEGER)
    """)
    conn.commit()

def display():
    items = cur.execute("SELECT * FROM student")
    z = []
    k = []
    m = []
    g = []
    for item in items:
        z.append(item[0])
        k.append(item[1])
        m.append(item[2])
        g.append(item[3])
    data = {
        "first_name": z,
        "last_name": k,
        "major": m,
        "grade": g
    }
    df = pd.DataFrame(data)
    print(df)

def insert():
    ch = input('''Do you want to insert one or many?\nIf you want to enter one, type 'one'.\nElse type 'many': ''')
    if ch.lower() == 'one':
        f = input("Enter the first name: ")
        l = input("Enter the second name: ")
        m = input("Enter the major: ")
        z = int(input("Enter grade: "))
        cur.execute("INSERT INTO student VALUES (?,?,?,?)", (f, l, m, z))
        conn.commit()
        display()
    elif ch.lower() == 'many':
        lop = int(input("How many data do you need to input: "))
        z = []
        for i in range(lop):
            f = input("Enter the first name: ")
            l = input("Enter the second name: ")
            m = input("Enter the major: ")
            p = int(input("Enter grade: "))
            z.append((f, l, m, p))
        cur.executemany("INSERT INTO student VALUES (?,?,?,?)", z)
        conn.commit()
        display()

def delete_one():
    items = cur.execute("SELECT rowid,* FROM student")
    for item in items:
        print(item)
    k = input("Enter row id you want to delete: ")
    cur.execute("DELETE FROM student WHERE rowid = ?", (k,))
    conn.commit()
    display()

def orderby():
    ch = int(input("""If you want to order them using grade, enter '1'.\nIf you want to order them by first name, enter '0': """))
    if ch == 1:
        items = cur.execute('SELECT * FROM student ORDER BY grade DESC')
        z = []
        k = []
        m = []
        g = []
        for item in items:
            z.append(item[0])
            k.append(item[1])
            m.append(item[2])
            g.append(item[3])
        data = {
            "first_name": z,
            "last_name": k,
            "major": m,
            "grade": g
        }
        df = pd.DataFrame(data)
        print(df)
    else:
        items = cur.execute('SELECT * FROM student ORDER BY first_name')
        z = []
        k = []
        m = []
        g = []
        for item in items:
            z.append(item[0])
            k.append(item[1])
            m.append(item[2])
            g.append(item[3])
        data = {
            "first_name": z,
            "last_name": k,
            "major": m,
            "grade": g
        }
        df1 = pd.DataFrame(data)
        print(df1)

def password():
    pas = 'this'
    max_at = 3
    at = 0
    while at < max_at:
        n = get_pas()
        if n == pas:
            print("Access granted!")
            return True
        else:
            at += 1
            print(f"Wrong password, {max_at - at} tries left.")

    print("Too many attempts. Access denied!")
    return False

def get_pas():
    root = tk.Tk()
    root.withdraw()
    password = simpledialog.askstring("Password", "Enter password:", show='*')
    root.destroy()
    return password
