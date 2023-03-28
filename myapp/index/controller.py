# -*- coding: utf-8 -*- 

from flask import Blueprint,render_template

home = Blueprint('main', __name__ , template_folder='templates')

@home.route('/')
def index():
    return render_template("index.html")