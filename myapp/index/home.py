# -*- coding: utf-8 -*- 

from flask import Blueprint,render_template,session,redirect, url_for

homepage = Blueprint('homepage', __name__ , template_folder='templates')

@homepage.route('/home')
def show():
    if session.get("email"):
        return render_template("home.html")
    return redirect(url_for('main.index'))