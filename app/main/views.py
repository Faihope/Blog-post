from app.main.forms import RegistrationForm
from flask import render_template,redirect,flash,url_for,Blueprint
from . import main
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
        
        flash(f'Account created for {form.username.data}!','success')
        return redirect(url_for('.home'))
        
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
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)
   