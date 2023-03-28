# -*- coding: utf-8 -*- 

from flask import Blueprint,render_template,session,redirect, url_for

signout = Blueprint('signout', __name__ , template_folder='templates')

@signout.route('/signout')
def show():
    session.pop('email',None)
    session.pop('username',None)
    return redirect(url_for('main.index'))