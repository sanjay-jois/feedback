import sqlite3
from flask import Flask, render_template, request
app = Flask(__name__)
@app.route("/")
def index():
    return render_template('index.html')
@app.route('/submit',methods=['post'])
def submit():

    fullname = request.form.get('fullname')
    usn = request.form.get('usn')
    contact = request.form.get('contact')
    email = request.form.get('email')
    message = request.form.get('message')
    connetion = sqlite3.connect('feedback.db')
    cursor = connetion.cursor()
    cursor.execute('INSERT INTO FEEDBACK(fullname, usn, contact, email, message) VALUES (?, ?, ?, ?, ?)',(fullname, usn, contact, email, message))

    connetion.commit()
    feedbacks = cursor.execute('select fullname,message from FEEDBACK').fetchall()
    connetion.close()

    return render_template('success.html',feedbacks = feedbacks,name = fullname)
    
if __name__ == '__main__':
    app.run(debug=True)