from flask import Flask,render_template,request  
from flask_sqlalchemy import SQLAlchemy 
from Homework import STUDENT ,REGISTRATION,SUBJECT,TEACHER, session
app =  Flask(__name__)

@app.route('/')
def index():
    test = session.query(STUDENT.student_id,STUDENT.f_name,STUDENT.l_name,STUDENT.e_mail,REGISTRATION.subject_id,SUBJECT.subject_name,REGISTRATION.grade,
    TEACHER.teacher_f_name,TEACHER.teacher_l_name)\
        .join(REGISTRATION,STUDENT.student_id == REGISTRATION.student_id).join(SUBJECT,REGISTRATION.subject_id == SUBJECT.subject_id)\
        .join(TEACHER,SUBJECT.teacher_id == TEACHER.teacher_id)
    return render_template('index.html',TEST = test) 
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
