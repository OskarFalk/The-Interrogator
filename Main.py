from flask import Flask, render_template, redirect, session, flash
from flask_session import Session
from sqlalchemy.orm import create_session
from werkzeug.security import generate_password_hash, check_password_hash
from config import Config
from forms import LoginForm, RegisterForm, QuesteningForm
from dbhelper import Users, Answers, engine

import sqlite3 as lite


app = Flask(__name__)
app.config.from_object(Config)
app.config["SESSION_PERMENENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)



@app.route('/', methods=["POST", "GET"])
def home():
    if not session.get("name"):
        return redirect("/login")

    form = QuesteningForm()
    user_session = create_session(autocommit=False, autoflush=False, bind=engine)


    
    if form.validate_on_submit():
        form.UserID.data = session.get("name")
        user = user_session.query(Answers).filter_by(UserID=form.UserID.data).first()

        if user:
            flash("You have already answered this")

        else:
            new_answer = Answers(
                Question1 = form.Question1.data,
                Question2 = form.Question2.data,
                Question3 = form.Question3.data,
                Question4 = form.Question4.data,
                Question5 = form.Question5.data,
                UserID = session.get("name")
            )
            user_session.add(new_answer)
            user_session.commit()
            flash("Answers have been submitted successfully")


    if session.get("name")=="ADMIN":
        return render_template('AdminIndex.html', form=form, title='ARhhRhhH', user=session["name"])
    else:
        return render_template('index.html', form=form, title='Home', user=session["name"])





@app.route('/login/', methods=["POST", "GET"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user_session = create_session(autocommit=False, autoflush=False, bind=engine)
        user =user_session.query(Users).filter_by(Username=form.username.data).first()

        if user:
            if check_password_hash(user.Password, form.password.data):
                user_session.close()
                session["name"] = form.username.data
                return redirect('/')
            else:
                flash("Entered password is wrong")

    return render_template("login.html", form=form, title='The Interrogator')





@app.route('/register/', methods=["POST", "GET"])
def register():
    form = RegisterForm()
    user_session = create_session(autocommit=False, autoflush=False, bind=engine)
    
    if form.validate_on_submit():
        print("Registation request recieved")
        user = user_session.query(Users).filter_by(Username=form.username.data).first()
        
        if user:
            return redirect('/login/')
        
        new_user = Users(
            Username = form.username.data, 
            Mail = form.mail.data, 
            Password = generate_password_hash(form.password.data, method='sha256')
        )
        user_session.add(new_user)
        user_session.commit()
        
        if new_user:
            user_session.close()
            return redirect('/login/')
    
    return render_template("register.html", form=form, title='Creating Account')





@app.route("/logout/")
def logout():
    session["name"] = None
    return redirect("/")

@app.route('/about/')
def about():
    if not session.get("name"): 
        return redirect("/login")

    return render_template('about.html', title='About')

if __name__ == '__main__':
    app.run(debug=True)
    #app.run(host='0.0.0.0', port=5000)