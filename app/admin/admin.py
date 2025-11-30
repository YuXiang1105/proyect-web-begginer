from flask import current_app, flash, redirect, render_template, url_for, request
from flask_login import current_user
from . import administrator
from ..utils import admin_required, is_safe_url
from ..models import User
from .. import db


@administrator.route('/manage_admin', methods=['GET','POST'])
@admin_required
def manage_admin():
    page = request.args.get('page', 1, type=int)
    users = User.query.paginate(page=page, per_page=current_app.config['USERS_PER_PAGE'], error_out=False)
    
    return render_template('admin/manage_admin.html', users=users, current_user = current_user)


@administrator.route('/manage_admin/<id>/delete', methods=['POST'])
@admin_required
def delete_user(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    flash('User deleted', 'danger')

    next_url = request.form.get("next") or request.args.get("next")
    if not next_url or not is_safe_url(next_url):

        next_url = url_for('administrator.manage_admin')
    
    return redirect(next_url)



    