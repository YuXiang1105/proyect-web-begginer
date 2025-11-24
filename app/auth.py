from flask_login import login_user, logout_user, login_required, current_user
from flask import Blueprint, render_template, redirect, url_for, flash, request
from .forms import newClass, log_in_form, register_form
from .models import Alien, AlienClass, AlienImage
from . import db
from .models import User
from urllib.parse import urlparse, urljoin
from werkzeug.utils import secure_filename
import os
import uuid
from flask import current_app
auth = Blueprint("auth", __name__)

def is_safe_url(target):
    
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ('http', 'https') and ref_url.netloc == test_url.netloc


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

@auth.route('/form' ,methods =['GET', 'POST'])
@login_required #We need to be logged in to add an alien
def form():
    form = newClass()
    form.class_imput.choices = [(classes.id, classes.name) for classes in AlienClass.query.order_by(AlienClass.name).all()]
    if form.validate_on_submit():
        image = None
        
        if form.image.data:     
            file = form.image.data   
            original_filename = secure_filename(file.filename)
            if not original_filename:
                flash('No selected file', 'warning')
                return render_template(url_for('auth.form'), form=form)
            
            unique_prefix = uuid.uuid4().hex #we create a unique prefix to avoid name conflicts
            filename = f"{unique_prefix}_{original_filename}" #we create the final filename
            upload_folder = current_app.config["IMG_FOLDERS"] #the folder for the storage
            os.makedirs(upload_folder, exist_ok=True)#we create the folder if it does not exist
            file_path = os.path.join(upload_folder, filename)#the complete path for the storage
        
            file.save(file_path)#we upload the image
            image = filename  #we store the filename in the database
        
        
        #When sumbitting, I append the we alien to the 'Alien' array and redirects and refresh the page 'species'
        new_alien = Alien(
            Name=form.name.data,
            Danger=form.danger.data,
            Origin=form.origin.data,
            Description=form.description.data,
            user_id=current_user.id
        )
        if image is not None:
            new_image = AlienImage(filename=image)
            new_alien.image.append(new_image)

            
        for class_id in form.class_imput.data:  
            new_class = AlienClass.query.get(class_id)
            new_alien.classes.append(new_class)
            
        db.session.add(new_alien)
        db.session.commit()
        
        return redirect(url_for('main.species'))
        
    return render_template('auth/form.html', form =form)


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