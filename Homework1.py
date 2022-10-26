from flask import Flask ,render_template        
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('TableHomework.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80,debug=True)