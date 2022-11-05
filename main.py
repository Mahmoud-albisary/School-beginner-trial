from flask import Flask, redirect, url_for, request, render_template, json
import programparents
import sqlite3
app = Flask(__name__)

@app.route('/login')
def logging():
    return render_template('final.html')

@app.route('/logins', methods = ['POST'])
def loganswer():
    conn = sqlite3.connect('datas.db')
    cur = conn.cursor()
    cur = cur.execute("SELECT * FROM students")
    rows = cur.fetchall()
    global username
    global password
    username = request.form['username']
    password = request.form['password']
    global logged
    logged = False
    for items in rows:
        if items[1] == username and items[2] == password:
            logged = True
        else:
            pass
    return redirect(url_for('meetings'))
@app.route('/file')
def meetings():
    if logged == True:
        row = []
        row1 = []
        z = []
        global conn
        conn = sqlite3.connect('datas.db')
        global cur
        global rows
        global usernames
        global passwords
        global times
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS meetings (id INTEGER PRIMARY KEY, username TEXT, password TEXT, teacher TEXT, time TEXT )")
        cur = cur.execute("SELECT teacher FROM meetings")
        rows = cur.fetchall()
        cur = cur.execute("SELECT username FROM meetings")
        usernames = cur.fetchall()
        cur = cur.execute("SELECT password FROM meetings")
        passwords = cur.fetchall()
        cur = cur.execute("SELECT time FROM meetings")
        times = cur.fetchall()
        cur = conn.cursor()
        for items in programparents.rows:
            items = list(items)
            row.append(items)
        for item in programparents.rows1:
            item = list(item)
            row1.append(item)
        print(row1)
        number = len(row)
        numbers = len(row1)
        first = row[0]
        firsts = row1[0]
        cur = conn.cursor()
        cur = cur.execute("SELECT * FROM meetings")
        all = cur.fetchall()
        unwantedtech = []
        unwantedtimes = []
        for i in range(len(rows)):
            if password not in str(all[i]):
                unwantedtech.append(list(rows[i]))
                unwantedtimes.append(list(times[i]))
        return render_template('file.html', row1 = row1, row = row, number = len(row), numbers = len(row1), first = row[0], firsts = row1[0], unwantedtech = unwantedtech, unwantedtimes = unwantedtimes, unwanted = len(unwantedtech))
    else:
        return "can not connect"

@app.route('/files', methods=['POST'])
def meetings_backend():
    conn = sqlite3.connect('datas.db')
    cur = conn.cursor()
    teacher =  request.form.getlist('uniqueteachers[]');
    time = request.form.getlist('uniquetimes[]');
    print(json.dumps({'status':'OK','teacher':teacher,'pass':time}))
    if len(rows) > 0:
        for i in range(len(teacher)):
            if "('" + teacher[i] + "',)" in str(rows) and "('" + username + "',)" in str(usernames) and  "('" + password + "',)" in str(passwords):
                cur = conn.cursor()
                print(1)
                cur.execute("DELETE FROM meetings WHERE teacher = ? AND username = ? AND password = ?", (teacher[i], username, password))
                cur.execute("INSERT INTO meetings VALUES(NULL, ?, ?, ?, ?)", (username, password, teacher[i], time[i],))
                conn.commit()
            elif "('" + teacher[i] + "',)" in str(rows) and "('" + username + "',)" not in str(usernames) and "('" + password + "',)" not in str(passwords) and "('" + time[i] + "',)" in str(times) :
       
                return redirect(url_for('meetings'))
            else:
                print(2)
                cur = conn.cursor()
                cur.execute("INSERT INTO meetings VALUES(NULL, ?, ?, ?, ?)", (username, password, teacher[i], time[i],))
                conn.commit()
        print(username, password, teacher[i], time[i])
    else:
        for i in range(len(teacher)):
            cur.execute("INSERT INTO meetings VALUES(NULL, ?, ?, ?, ?)", (username, password, teacher[i], time[i],))
            conn.commit()
    conn.close()
    return "hello"


if __name__ == '__main__' :
    app.run(debug = True)
