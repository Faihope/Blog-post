from app.main.forms import RegistrationForm
from flask import render_template,redirect,flash,url_for,Blueprint,request
from . import main
from .. import db
from flask_login import login_user,logout_user,login_required
from ..models import User
from .forms import RegistrationForm,LoginForm
from flask_sqlalchemy import SQLAlchemy




posts=[
    {
       'author':'Faith Hope',
       'title':'Blog Post one',
       'content':'content 1'  ,
       'date_posted':'20/3/2021' 
    },
    
        
         {
       'author':'Patrick Rop',
       'title':'Blog Post Two',
       'content':'content 2'  ,
       'date_posted':'22/3/2021' 
    }
    
  
    
]


#views

@main.route('/')
@main.route('/home')

def home():
    return render_template("home.html",posts=posts)

@main.route('/about')
def about():
    return render_template("about.html")

@main.route('/register',methods=['GET','POST'])
def register():
    form=RegistrationForm()
    if form.validate_on_submit():
        user = User(email = form.email.data, username = form.username.data,password = form.password.data)
        db.session.add(user)
        db.session.commit()
        
        
        flash(f'Account created for {form.username.data}!','success')
        return redirect(url_for('.login'))
        
    '''
    View root page function that returns the index page and its data
    '''
    title = 'Home - Register'
    return render_template("register.html",form=form,title=title)

@main.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    '''
    View root page function that returns the index page and its data
    '''
    if form.validate_on_submit():
         
        user = User.query.filter_by(email = form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user,form.remember.data)
            return redirect(request.args.get('next') or url_for('main.home'))

        flash('Invalid username or Password')

    return render_template('login.html', title='Login', form=form)

@main.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.home"))
