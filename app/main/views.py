from app.main.forms import RegistrationForm
from flask import render_template,redirect,flash,url_for,Blueprint
from . import main
from .forms import RegistrationForm,LoginForm




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
    title = 'Home - Login'
    return render_template('login.html' ,title=title,form = form )
