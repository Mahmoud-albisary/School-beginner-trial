import sqlite3

def insertgraphics():
    global rows
    conn = sqlite3.connect("datas.db")
    cur = conn.cursor()
    cur.execute("SELECT teacher FROM teachers")
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    print(rows)


def insertgraphics1():
    global rows1
    conn = sqlite3.connect("datas.db")
    cur = conn.cursor()
    cur.execute("SELECT duration FROM durations")
    rows1 = cur.fetchall()
    conn.commit()
    conn.close()
    print(rows1)

insertgraphics()
insertgraphics1()
