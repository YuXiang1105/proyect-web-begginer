from flask_login import login_user, logout_user, login_required, current_user
from flask import render_template, redirect, url_for, flash, request
from .forms import log_in_form, register_form
from .. import db
from ..models import User
from . import auth
from ..utils import is_safe_url


#auth blueprints routes
@auth.route('/log_in',methods =['GET', 'POST'])
def log_in():
    form = log_in_form()
    
    if current_user.is_authenticated:
        return redirect(url_for('main.index')) #if already logged in, redirect to home
    
    if form.validate_on_submit():
        email = form.email.data.lower().strip()
        user = User.query.filter_by(email=email).first()
        
        if user and user.check_password(form.password.data):
            login_user(user)
            next_url = request.args.get("next")
            if not next_url or not is_safe_url(next_url):
                flash("Login successful, welcome back!")
                next_url = url_for("main.index")

            return redirect(next_url or url_for("main.index"))
        else:
            flash("Invalid email or password")
    
    return render_template("auth/log_in.html", form=form)

@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = register_form()
    if form.validate_on_submit():
        user = form.user.data
        existing_user = User.query.filter_by(email=form.email.data).first()
        if existing_user:
            flash('User already exists')
        else: 
            NewUser = User(email= form.email.data, user=user)
            NewUser.set_password(form.password.data)
            db.session.add(NewUser)
            db.session.commit()
            login_user(NewUser)
            flash('Registration successful')
            
        
        return redirect(url_for("main.index"))    
    
    return render_template('auth/register.html', form = form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out successfully', 'info')
    return redirect(url_for('main.index'))