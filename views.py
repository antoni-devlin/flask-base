from flask import render_template
from app import app
from models import Member
from forms import LoginForm

@app.route('/index')
def goindex():
    return redirect('/')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/query')
def query():
    firstmember = Member.query.first()
    return '<h1> The first member is:' + firstmember.name +'.</h1>'

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', form=form)
