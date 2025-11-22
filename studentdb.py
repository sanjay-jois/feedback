import sqlite3

connection = sqlite3.connect("student.db")
cursor = connection.cursor()

cmd = """
CREATE TABLE IF NOT EXISTS STUDENT(
    usn TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    branch TEXT NOT NULL,
    sem INTEGER NOT NULL
)
"""
cursor.execute(cmd)
connection.commit()

students = [
    ("1RV22CS001", "Jay", "CSE", 5),
    ("1RV22CS002", "Sanjay", "CSE", 5),
    ("1RV22CS003", "Rahul", "ISE", 3)
]

insert_cmd = "INSERT OR IGNORE INTO STUDENT(usn, name, branch, sem) VALUES (?, ?, ?, ?)"

cursor.executemany(insert_cmd, students)
connection.commit()


data = cursor.execute("SELECT * FROM STUDENT").fetchall()
print(data)

connection.close()
