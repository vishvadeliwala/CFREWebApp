
function myfunc(){
if(document.getElementById("prediction_history").innerHTML != ""){
    var inner = String(document.getElementById("prediction_history").innerHTML)
    inner = inner.split("\'").join("\"");
    var data = JSON.parse(inner);
    var html = "";
    crop_list = [
        'Barley',
        'Cotton',
        'Ground Nuts',
        'Maize',
        'Millets',
        'Oil seeds',
        'Paddy',
        'Pulses',
        'Sugarcane',
        'Tobacco',
        'Wheat'
    ]
    soil_list = [
        'Black',
        'Clayey',
        'Loamy',
        'Red',
        'Sandy'
    ]
    for(let count in data){
        data_history = data[count];
        var N = data_history["N"];
        var P = data_history["P"];
        var K = data_history["K"];
        var temp = data_history["temp"];
        var humidity = data_history["humidity"];
        if("RecommendedCrop" in data_history){
            html = html.concat("<div class='history_element' id='history" + count + "'>");
            var ph = data_history["ph"];
            var rainfall = data_history["rainfall"];
            var crop = data_history["RecommendedCrop"];
            html = html.concat("Nitrogen: " + N + "<br> Phosphorous: " + P + "<br> Potassium: " + K
            + "<br> Temperature: " + temp + "<br> Humidity: " + humidity + "<br> ph: " + ph +
            "<br> rainfall: " + rainfall + "<br> Recommended Crop: " + crop);
            html = html.concat("</div>");
        }
        else if("RecommendedFertilizer" in data_history){
            html = html.concat("<div class='history_element' id='history" + count + "'>");
            var moisture = data_history["ph"];
            var soil = soil_list[parseInt(data_history["rainfall"])];
            var crop = crop_list[parseInt(data_history["crop"])];
            var fertilizer = data_history["RecommendedFertilizer"]
            html = html.concat("Nitrogen: " + N + "<br> Phosphorous: " + P + "<br> Potassium: " + K
            + "<br> Temperature: " + temp + "<br> Humidity: " + humidity + "<br> Moisture: " + moisture +
            "<br> Crop Type: " + crop + "<br> Soil Type: " + soil + "<br> Recommended Fertilizer: " + fertilizer);
            html = html.concat("</div>");
        }
        else{
            continue;
        }
    }
    console.log(html)
    if(html !== ""){
        document.getElementById("prediction_history").innerHTML = html;
    }
}
else{
    document.getElementById("prediction_history").innerHTML = "No Prediction History";
}
}