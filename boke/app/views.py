from app import app
from flask import redirect, render_template, flash



@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/index')
def index():
    user = { 'nickname': 'Miguel' } # fake user
    posts = [ # fake array of posts
        {
            'author': { 'nickname': 'John' },
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': { 'nickname': 'Susan' },
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template("index.html",
        title = 'Home',
        user = user,
        posts = posts)
from .forms import LoginForm
@app.route('/login',methods = ['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OPendi"'+form.openid.data+'",remember_me=' + str(form.remember_me.data))
        return redirect('/index')
    return render_template('login.html',
            title = 'Sign In',
            form = form)






