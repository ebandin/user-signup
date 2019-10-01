from flask import Flask, request, redirect, render_template, session
from flask_sqlalchemy import SQLAlchemy
import re 

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://user-signup:T@c0surprise@localhost:8889/user-signup'
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
         if len(username) > 3 and len(username) < 20:
             return True
         else: 
             return False

    def isValidPassword(self, password):
         if len(password) > 3 and len(password) < 20:
             return True
         else: 
             return False

    def isValidEmail(self, email):
     if len(email) > 3 and len(email) < 20:
        if re.match("^.+@([?)[a-zA-Z0-9-.]+.([a-zA-Z]{2,3}|[0-9]{1,3})(]?)$", email) != None:
            return True
        else: 
            return False


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        verify = request.form['verify']
        email = request.form['email']

        if isValidEmail(email) == True:
           pass
        else: 
            error = "this is not a valid email address"
            return redirect("/?error"+ error)

        if isValidPassword(password) == True:
            pass
        else: 
            error = "this is not a valid password"
            return redirect("/?error"+ error)

        if isValidUsername(username) == True:
               pass
        else: 
            error = "this is not a valid username"
            return redirect("/?error"+ error)


        existing_user = User.query.filter_by(username = username).first()
        if not existing_user:
            new_user = User(username, password, email)
            db.session.add(new_user)
            db.session.commit()
            session['username'] = username
            return redirect('/')
        else:
            # TODO - user better response messaging
            return "<h1>Duplicate user</h1>"

    return render_template('register.html')

@app.route('/welcome', methods=['POST', 'GET'])
def welcome(): 
    username = request.form['username']
    return render_template('welcome.html', username = username)

if __name__ == '__main__':
    app.run()