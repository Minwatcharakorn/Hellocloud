import sqlite3 
from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route("/")
def index():
    x = sqlite3.connect('Homework.sqlite3')
    cur = x.cursor()
    cur.execute("SELECT Students.student_id, Students.f_name, Students.l_name, Subject.subject_id, Subject.subject_name, Registration.grade, Teachers.f_name, Teachers.l_name \
                FROM Students\
                join Registration\
                on Registration.student_id = Students.student_id\
                JOIN Subject\
                on Registration.subject_id = Subject.subject_id\
                JOIN Teachers\
                on Subject.teacher_id = Teachers.teacher_id;")
    test = cur.fetchall()
    return render_template("index.html", test=test)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)