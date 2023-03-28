from flask import Blueprint, url_for, render_template, redirect, request, session
import pymongo
import requests

crop = Blueprint('crop', __name__, template_folder='templates')
client = pymongo.MongoClient("mongodb+srv://admin:CFREapp@cfre.1zs8dam.mongodb.net/?retryWrites=true&w=majority")
db = client.CFRE
crop_recommend = 'http://localhost:5001/crop_recommend'

@crop.route('/crop', methods=['GET', 'POST'])
def show():
    if request.method == 'POST':
        email = session.get('email')
        History = db.History
        N = float(request.form['N'])
        P = float(request.form['P'])
        K = float(request.form['K'])
        temp = float(request.form['temp'])
        humidity = float(request.form['humidity'])
        rainfall = float(request.form['rainfall'])
        ph = float(request.form['ph'])
        data = {
            "N": N,
            "P": P,
            "K": K,
            "temp": temp,
            "humidity": humidity,
            "ph": ph,
            "rainfall": rainfall
        }
        result = requests.post(crop_recommend,json=data)
        prediction = result.json()
        Recommended_crop = prediction.get("Crop")
        if Recommended_crop:
            data["email"] = email
            data["RecommendedCrop"] = Recommended_crop
            History.insert_one(data).inserted_id
            return render_template("crop.html", prediction=Recommended_crop,
            N=N,P=P,K=K,temp=temp,humidity=humidity,rainfall=rainfall,ph=ph)
        return render_template("crop.html", prediction="Failed to predict the recommendation for crop")
    else:
        return render_template("crop.html")
        