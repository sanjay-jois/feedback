import sqlite3

connection = sqlite3.connect("feedback.db")
cursor = connection.cursor()

cmd = """
CREATE TABLE IF NOT EXISTS FEEDBACK(
   id INTEGER PRIMARY KEY AUTOINCREMENT, 
   fullname TEXT NOT NULL,
   usn VARCHAR(10) NOT NULL,
   contact VARCHAR(10) NOT NULL,
   email TEXT NOT NULL,
   message TEXT NOT NULL
)
"""
cursor.execute(cmd)
connection.commit()

cmd = "INSERT INTO FEEDBACK(fullname, usn, contact, email, message) VALUES (?, ?, ?, ?, ?)"
cursor.execute(cmd, ("jay", "457dd", "1234567894", "asd@gmail.com", "this is good time to learn"))
connection.commit()

f = cursor.execute("SELECT * FROM FEEDBACK").fetchall()
print(f)
r = cursor.execute("select * from FEEDBACK where fullname = ?",('jay',)).fetchall()
print(r)
connection.close()
