from flask import Blueprint, url_for, render_template, redirect, request, session
import pymongo
import requests

fertilizer = Blueprint('fertilizer', __name__, template_folder='templates')
client = pymongo.MongoClient("mongodb+srv://admin:CFREapp@cfre.1zs8dam.mongodb.net/?retryWrites=true&w=majority")
db = client.CFRE
fertilizer_recommend = 'http://localhost:5001/fertilizer_recommend'

@fertilizer.route('/fertilizer', methods=['GET', 'POST'])
def show():
    if request.method == 'POST':
        email = session.get('email')
        History = db.History
        N = float(request.form['N'])
        P = float(request.form['P'])
        K = float(request.form['K'])
        temp = float(request.form['temp'])
        humidity = float(request.form['humidity'])
        moisture = float(request.form['moisture'])
        soil = float(request.form['soil'])
        crop = float(request.form['crop'])
        data = {
            "N": N,
            "P": P,
            "K": K,
            "temp": temp,
            "humidity": humidity,
            "moisture": moisture,
            "soil": soil,
            "crop": crop
        }
        result = requests.post(fertilizer_recommend,json=data)
        prediction = result.json()
        Recommended_crop = prediction.get("Fertilizer")
        if Recommended_crop:
            data["email"] = email
            data["RecommendedFertilizer"] = Recommended_crop
            History.insert_one(data).inserted_id
            return render_template("fertilizer.html", prediction=Recommended_crop,
            N=N,P=P,K=K,temp=temp,humidity=humidity,moisture=moisture,soil=int(soil),crop=int(crop))
        return render_template("fertilizer.html", prediction="Failed to predict the recommendation for Fertilizer")
    else:
        return render_template("fertilizer.html")
        