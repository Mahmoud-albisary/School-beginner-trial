import sqlite3
def view():
    global rows
    conn = sqlite3.connect("datas.db")
    cur = conn.cursor()
    cur = cur.execute("SELECT * FROM meetings")
    rows = cur.fetchall()
    conn.close()
    return rows
def delete():
    conn = sqlite3.connect("datas.db")
    cur = conn.cursor()
    cur = cur.execute("DROP TABLE meetings")
    conn.commit()
    conn.close()


print(view())
