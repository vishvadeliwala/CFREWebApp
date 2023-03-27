import numpy as np
from flask import Flask, request
import pickle
from json import JSONEncoder
import json
app = Flask(__name__)
cropmodel = pickle.load(open('crop_modelNB.pkl','rb'))
fertilizermodel = pickle.load(open('Fertlizer.pkl','rb'))

#Crop Result List
crops = ['Apple', 'Banana', 'Blackgram', 'Chickpea', 'Coconut', 'Coffee', 'Cotton', 'Grapes', 
        'Jute', 'Kidneybeans', 'Lentil', 'Maize', 'Mango', 'Mothbeans', 'Mungbean', 'Muskmelon', 
        'Orange', 'Papaya', 'Pigeonpeas', 'Pomegranate', 'Rice', 'Watermelon']

#Fertilizers Result List
fertilizers = ['10-26-26','14-35-14','17-17-17','20-20-3','28-28','DAP','Urea']

class NumpyArrayEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return JSONEncoder.default(self, obj)

@app.route('/crop_recommend',methods=['POST'])
def crop_recommend():
    # Get the data from the POST request.
    try:
        data = request.get_json(force=True)
        N = data["N"] if data.get("N") is not None else ""
        P = data["P"] if data.get("P") is not None else ""
        K = data["K"] if data.get("K") is not None else ""
        temp = data["temp"] if data.get("temp") is not None else ""
        humidity = data["humidity"] if data.get("humidity") is not None else ""
        ph = data["ph"] if data.get("ph") is not None else ""
        rainfall = data["rainfall"] if data.get("rainfall") is not None else ""
        params = [N, P, K, temp, humidity, ph, rainfall]
        single_pred = np.array(np.array(params, dtype=float)).reshape(1,-1)
        result = int(cropmodel.predict(single_pred))
        return json.dumps({"Crop":crops[result]}, cls=NumpyArrayEncoder)
    except Exception as e:
        return json.dumps({"Error": str(e)})
@app.route('/fertilizer_recommend',methods=['POST'])
def fertilizer_recommend():
    # Get the data from the POST request.
    try:
        data = request.get_json(force=True)
        N = data["N"] if data.get("N") is not None else ""
        P = data["P"] if data.get("P") is not None else ""
        K = data["K"] if data.get("K") is not None else ""
        temp = data["temp"] if data.get("temp") is not None else ""
        humidity = data["humidity"] if data.get("humidity") is not None else ""
        soil = data["soil"] if data.get("soil") is not None else ""
        moisture = data["moisture"] if data.get("moisture") is not None else ""
        crop = data["crop"] if data.get("crop") is not None else ""
        params = [temp, humidity, moisture, soil, crop, N, K, P]
        single_pred = np.array(np.array(params, dtype=float)).reshape(1,-1)
        result = int(fertilizermodel.predict(single_pred))
        return json.dumps({"Fertilizer":fertilizers[result]}, cls=NumpyArrayEncoder)
    except Exception as e:
        return json.dumps({"Error": str(e)})
if __name__ == '__main__':
    app.run(port=5001, debug=True)