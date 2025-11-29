from flask_login import login_required, current_user
from flask import abort
from . import administrator

@administrator.route('/login_admin', methods=['GET','POST'])
def login_admin():
    #security layer
    if not current_user.is_admin:
        abort(403)
    