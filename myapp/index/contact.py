# -*- coding: utf-8 -*- 

from flask import Blueprint,render_template

contact = Blueprint('contact', __name__ , template_folder='templates')

@contact.route('/contact')
def show():
    return render_template("contact.html")