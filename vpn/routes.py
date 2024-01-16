from vpn import app
from flask import render_template, redirect, url_for, flash, get_flashed_messages
from vpn.models import User
from vpn import db
# from vpn.forms import RegisterForm, LoginForm

@app.route('/')
@app.route('/login')
def home_page():
    return render_template('/login.html')
