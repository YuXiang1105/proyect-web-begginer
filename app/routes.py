from flask import abort, current_app
from flask_login import login_required, current_user
from flask import Blueprint, render_template, redirect, url_for, flash, request

from app.utils import is_safe_url
from .forms import editRelicForm, newClassAlien
from .models import Alien, AlienClass, AlienImage
from . import db
import os
import uuid
from flask import current_app
from werkzeug.utils import secure_filename

main = Blueprint("main", __name__)

@main.route('/')
@main.route('/index')
def index():
    aliens = Alien.query.all()
    return render_template('main/index.html', aliens = aliens, current_user = current_user)


@main.route('/information')
def information():
    return render_template('main/information.html', current_user = current_user)

@main.route('/species')
def species():
    page = request.args.get('page', 1, type=int)
    aliens = Alien.query.paginate(page=page, per_page=current_app.config['ALIENS_PER_PAGE'], error_out=False)
    return render_template('main/species.html', aliens = aliens , current_user = current_user)

@main.route('/form' ,methods =['GET', 'POST'])
@login_required #We need to be logged in to add an alien
def form():
    form = newClassAlien()
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
        flash('New alien added successfully!', 'success')
        
        next_url = request.args.get("next")
        if not next_url or not is_safe_url(next_url):
            next_url = url_for("main.index")
            
        return redirect(next_url or url_for('main.species'))
        
    return render_template('main/form.html', form=form, current_user = current_user)

#route for editing an alien, only possible by admin and the user that created it
@main.route('/species/<alien_id>/edit', methods=['GET','POST'])
@login_required
def edit_alien(alien_id):
    alien = Alien.query.get(alien_id)
    if current_user.id != alien.user_id and not current_user.is_admin:
        abort(403)
    form = editRelicForm()
    form.class_imput.choices = [(alienCLass.id, alienCLass.name) for alienCLass in AlienClass.query.order_by(AlienClass.name).all()]
    
    if form.validate_on_submit():
        if form.image.data: #if we sumbit an image, we make the security checks
            file = form.image.data 
            original_filename = secure_filename(file.filename)
            if not original_filename:
                flash('No selected file', 'warning')
                return render_template('main/edit_form.html', form=form, alien=alien)
            #We delete previous images, only an image can be displayed at the same time
            if alien.image:
                for img in alien.image:
                    os.remove(os.path.join(current_app.config["IMG_FOLDERS"], img.filename))
                    db.session.delete(img)
            #security and unique filename
            unique_prefix = uuid.uuid4().hex
            filename = f"{unique_prefix}_{original_filename}"
            upload_folder = current_app.config["IMG_FOLDERS"]
            os.makedirs(upload_folder, exist_ok=True)
            file_path = os.path.join(upload_folder, filename)
        
            file.save(file_path)
            new_image = AlienImage(filename=filename)
            alien.image.append(new_image)
        
        
        
        if form.name.data:
            alien.Name = form.name.data
        if form.danger.data:
            alien.Danger = form.danger.data
        if form.origin.data:
            alien.Origin = form.origin.data
        if form.description.data:
            alien.Description = form.description.data

        
        alien.classes.clear()#we delete the previous classes

        for class_id in form.class_imput.data:
            new_class = AlienClass.query.get(class_id)
            alien.classes.append(new_class)
        
        db.session.commit()
        flash('alien update succesful', 'success')
        next_url = request.args.get("next")
        if not next_url or not is_safe_url(next_url):
            flash("Login successful, welcome back!")
            next_url = url_for("main.index")
        
        return redirect(next_url or url_for('main.species'))
    return render_template("main/edit_form.html", form=form, alien=alien, current_user = current_user)


#route for deleting an alien, only possible by admin and the user that created it
@main.route('/species/<alien_id>/delete', methods=['GET','POST'])
@login_required
def delete_alien(alien_id):
    alien = Alien.query.get_or_404(alien_id)
    if current_user.id != alien.user_id and not current_user.is_admin:
        abort(403)
    db.session.delete(alien)
    db.session.commit()
    flash('Alien deleted', 'danger')
    next_url = request.args.get("next")
    if not next_url or not is_safe_url(next_url):
        next_url = url_for("main.index")
    return redirect(next_url or url_for('main.species'))

@main.route('/profile', methods=['GET','POST'])
@login_required
def profile():
    
    user_aliens = Alien.query.filter_by(user_id=current_user.id).all()
    return render_template('main/profile.html', aliens=user_aliens,  current_user = current_user)



