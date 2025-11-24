from flask import abort, current_app
from flask_login import login_user, logout_user, login_required, current_user
from flask import Blueprint, render_template, redirect, url_for, flash, request
from .forms import newClass, log_in_form, register_form, editRelicForm
from .models import Alien, AlienClass
from . import db
from .models import User

main = Blueprint("main", __name__)
auth = Blueprint("auth", __name__)

@main.route('/')
@main.route('/index')
def index():
    aliens = Alien.query.all()
    return render_template('main/index.html', aliens = aliens)


@main.route('/information')
def information():
    return render_template('main/information.html')

@main.route('/species')
def species():
    page = request.args.get('page', 1, type=int)
    aliens = Alien.query.paginate(page=page, per_page=current_app.config['ALIENS_PER_PAGE'], error_out=False)
    return render_template('main/species.html', aliens = aliens )

@main.route('/species/<alien_id>/edit', methods=['GET','POST'])
@login_required
def edit_alien(alien_id):
    alien = Alien.query.get(alien_id)
    if current_user.id != alien.user_id:
        abort(403)
    form = editRelicForm()
    form.class_imput.choices = [(c.id, c.name) for c in AlienClass.query.order_by(AlienClass.name).all()]
    if form.validate_on_submit():
        if form.name.data:
            alien.name = form.name.data
        if form.danger.data:
            alien.danger = form.danger.data
        if form.origin.data:
            alien.origin = form.origin.data
        if form.description.data:
            alien.description = form.description.data
        
        alien.classes.clear()#we delete the previous classes

        for class_id in form.class_imput.data:
            new_class = AlienClass.query.get(class_id)
            alien.classes.append(new_class)
        
        db.session.commit()
        flash('alien update succesful', 'success')
        return redirect(url_for('main.species'))
    return render_template('main/edit_form.html', form=form, alien=alien)


@main.route('/species/<alien_id>/delete', methods=['GET','POST'])
@login_required
def delete_alien(alien_id):
    alien = Alien.query.get_or_404(alien_id)
    if current_user.id != alien.user_id:
        abort(403)
    db.session.delete(alien)
    db.session.commit()
    flash('Alien deleted', 'danger')
    return redirect(url_for('main.species'))
