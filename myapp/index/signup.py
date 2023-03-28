from flask import Blueprint, url_for, render_template, redirect, request, session
import pymongo
signup = Blueprint('signup', __name__, template_folder='templates')
client = pymongo.MongoClient("mongodb+srv://admin:CFREapp@cfre.1zs8dam.mongodb.net/?retryWrites=true&w=majority")
db = client.CFRE


@signup.route('/signup', methods=['GET', 'POST'])
def show():
    if request.method == 'POST':
        email = str(request.form['email'])
        pwd = str(request.form['pwd'])
        name = str(request.form['name'])
        Users = db.Users
        result = Users.find_one({"email": email})
        if result:
            return render_template('index.html',signup_error="An account already exists with this email. Please login")
        data = {
            "email": email,
            "pwd": pwd,
            "name": name
        }
        Users.insert_one(data).inserted_id
        session["username"] = name
        session["email"] = email
        return redirect(url_for("homepage.show"))
    else:
        return render_template('index.html')