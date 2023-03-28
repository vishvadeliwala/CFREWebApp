from flask import Blueprint, url_for, render_template, redirect, request, session
import pymongo

login = Blueprint('login', __name__, template_folder='templates')
client = pymongo.MongoClient("mongodb+srv://admin:CFREapp@cfre.1zs8dam.mongodb.net/?retryWrites=true&w=majority")
db = client.CFRE


@login.route('/login', methods=['GET', 'POST'])
def show():
    if request.method == 'POST':
        email = str(request.form['email'])
        pwd = str(request.form['pwd'])
        Users = db.Users
        result = Users.find_one({"email": email})
        if result:
            if result["pwd"] == pwd:
                session['username'] = result["name"]
                session['email'] = result['email']
                return redirect(url_for('homepage.show'))
            return render_template('index.html', login_error="Incorrect Password")
        return render_template('index.html', login_error="User not Found. Please Sign up")
    else:
        return render_template('index.html')