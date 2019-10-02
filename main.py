from flask import Flask, request, redirect, render_template, session
from flask_sqlalchemy import SQLAlchemy
import re 

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://user-project:yess@localhost:8889/user-project'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)
app.secret_key = 'y337kGcys&zP3B'


class User(db.Model):

    username = db.Column(db.String(20), primary_key=True)
    password = db.Column(db.String(20))
    email = db.Column(db.String(20), unique = True)
    

    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email
 
    def isValidUsername(self, username):
        if len(username) > 2 and len(username) < 20:
            return True
        else: 
            return False

    def isValidPassword(self, password):
        if len(password) > 2 and len(password) < 20:
            return True
        else: 
            return False

    def isValidEmail(self, email):
        if len(email) > 2 and len(email) < 20:
            if '@' in email:
                return True
            else: 
                return False
        else: 
            return False



@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('register.html')


@app.route('/validate', methods=['POST', 'GET']) 
def validate():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        verify = request.form['verify']
        email = request.form['email']

        if User.isValidEmail(None, email) == True:
            None 
        else: 
            error = "this is not a valid email address"
            return "<h1> Invalid Email </h1>" 

        if User.isValidPassword(None, password) == True:
            None 
        else: 
            error = "this is not a valid password"
            return "<h1> Invalid Password </h1>" 

        if User.isValidUsername(None, username) == True:
            None
        else: 
            error = "this is not a valid username"
            return "<h1> Invalid Username </h1>" 



        
        new_user = User(username, password, email)
        db.session.add(new_user)
        db.session.commit()
        #session['username'] = username
        return redirect('/welcome')

 

@app.route('/welcome', methods=['POST', 'GET'])
def welcome(): 
    #username = request.form['username']
    return render_template('welcome.html')

if __name__ == '__main__':
    app.run()