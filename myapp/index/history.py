from flask import Blueprint, url_for, render_template, redirect, request, session
import pymongo

history = Blueprint('history', __name__, template_folder='templates')
client = pymongo.MongoClient("mongodb+srv://admin:CFREapp@cfre.1zs8dam.mongodb.net/?retryWrites=true&w=majority")
db = client.CFRE

@history.route('/history')
def index():
    email = session.get('email')
    History = db.History
    count = 0
    data_history = {}
    for data in History.find({"email": email}):
        count = count + 1
        data.pop("_id")
        data_history[str(count)] = data
    if count>0:
        return render_template("history.html", data=data_history)
    return render_template("history.html")
        