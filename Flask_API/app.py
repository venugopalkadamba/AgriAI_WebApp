from flask import Flask, request
from flask_cors import CORS, cross_origin

import os
import json
import pickle
import numpy as np
from scipy import stats

app = Flask(__name__)

cors = CORS(app)

@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept")
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  response.headers.add('Access-Control-Allow-Credentials', 'true')
  return response

# Loading all Crop Recommendation Models
crop_xgb_pipeline = pickle.load(
    open("./models/crop_recommendation/xgb_pipeline.pkl", "rb")
)
crop_rf_pipeline = pickle.load(
    open("./models/crop_recommendation/rf_pipeline.pkl", "rb")
)
crop_knn_pipeline = pickle.load(
    open("./models/crop_recommendation/knn_pipeline.pkl", "rb")
)
crop_label_dict = pickle.load(
    open("./models/crop_recommendation/label_dictionary.pkl", "rb")
)


# Loading all Fertilizer Recommendation Models
fertilizer_xgb_pipeline = pickle.load(
    open("./models/fertilizer_recommendation/xgb_pipeline.pkl", "rb")
)
fertilizer_rf_pipeline = pickle.load(
    open("./models/fertilizer_recommendation/rf_pipeline.pkl", "rb")
)
fertilizer_svm_pipeline = pickle.load(
    open("./models/fertilizer_recommendation/svm_pipeline.pkl", "rb")
)
fertilizer_label_dict = pickle.load(
    open("./models/fertilizer_recommendation/fertname_dict.pkl", "rb")
)
soiltype_label_dict = pickle.load(
    open("./models/fertilizer_recommendation/soiltype_dict.pkl", "rb")
)
croptype_label_dict = pickle.load(
    open("./models/fertilizer_recommendation/croptype_dict.pkl", "rb")
)


crop_label_name_dict = {}
for crop_value in croptype_label_dict:
    crop_label_name_dict[croptype_label_dict[crop_value]] = crop_value

soil_label_dict = {}
for soil_value in soiltype_label_dict:
    soil_label_dict[soiltype_label_dict[soil_value]] = soil_value


def convert(o):
    if isinstance(o, np.generic):
        return o.item()
    raise TypeError


def crop_prediction(input_data):
    prediction_data = {
        "xgb_model_prediction": crop_label_dict[
            crop_xgb_pipeline.predict(input_data)[0]
        ],
        "xgb_model_probability": max(crop_xgb_pipeline.predict_proba(input_data)[0])
        * 100,
        "rf_model_prediction": crop_label_dict[crop_rf_pipeline.predict(input_data)[0]],
        "rf_model_probability": max(crop_rf_pipeline.predict_proba(input_data)[0])
        * 100,
        "knn_model_prediction": crop_label_dict[
            crop_knn_pipeline.predict(input_data)[0]
        ],
        "knn_model_probability": max(crop_knn_pipeline.predict_proba(input_data)[0])
        * 100,
    }

    all_predictions = [
            prediction_data["xgb_model_prediction"],
            prediction_data["rf_model_prediction"],
            prediction_data["knn_model_prediction"],
        ]

    all_probs = [
            prediction_data["xgb_model_probability"],
            prediction_data["rf_model_probability"],
            prediction_data["knn_model_probability"],
        ]

    if len(set(all_predictions)) == len(all_predictions):
        prediction_data["final_prediction"] = all_predictions[all_probs.index(max(all_probs))]
    else:
        prediction_data["final_prediction"] = stats.mode(all_predictions)[0][0]

    return prediction_data


def fertilizer_prediction(input_data):
    prediction_data = {
        "xgb_model_prediction": fertilizer_label_dict[
            fertilizer_xgb_pipeline.predict(input_data)[0]
        ],
        "xgb_model_probability": max(
            fertilizer_xgb_pipeline.predict_proba(input_data)[0]
        )
        * 100,
        "rf_model_prediction": fertilizer_label_dict[
            fertilizer_rf_pipeline.predict(input_data)[0]
        ],
        "rf_model_probability": max(fertilizer_rf_pipeline.predict_proba(input_data)[0])
        * 100,
        "svm_model_prediction": fertilizer_label_dict[
            fertilizer_svm_pipeline.predict(input_data)[0]
        ],
        "svm_model_probability": max(
            fertilizer_svm_pipeline.predict_proba(input_data)[0]
        )
        * 100,
    }

    all_predictions = [
            prediction_data["xgb_model_prediction"],
            prediction_data["rf_model_prediction"],
            prediction_data["svm_model_prediction"],
        ]

    all_probs = [
            prediction_data["xgb_model_probability"],
            prediction_data["rf_model_probability"],
            prediction_data["svm_model_probability"],
        ]

    if len(set(all_predictions)) == len(all_predictions):
        prediction_data["final_prediction"] = all_predictions[all_probs.index(max(all_probs))]
    else:
        prediction_data["final_prediction"] = stats.mode(all_predictions)[0][0]

    return prediction_data


@app.route("/predict_crop", methods=["GET", "POST"])
def predictcrop():
    try:
        if request.method == "POST":
            form_values = request.form.to_dict()
            column_names = ["N", "P", "K", "temperature", "humidity", "ph", "rainfall"]
            input_data = np.asarray([float(form_values[i].strip()) for i in column_names]).reshape(
                1, -1
            )
            prediction_data = crop_prediction(input_data)
            json_obj = json.dumps(prediction_data, default=convert)
            return json_obj
    except:
        return json.dumps({"error":"Please Enter Valid Data"}, default=convert)


@app.route("/predict_fertilizer", methods=["GET", "POST"])
def predictfertilizer():
    try:
        if request.method == "POST":
            form_values = request.form.to_dict()
            column_names = [
                "Temparature",
                "Humidity",
                "Moisture",
                "soil_type",
                "crop_type",
                "Nitrogen",
                "Potassium",
                "Phosphorous",
            ]

            for key in form_values:
                form_values[key] = form_values[key].strip()

            form_values["soil_type"] = soil_label_dict[form_values["soil_type"]]
            form_values["crop_type"] = crop_label_name_dict[form_values["crop_type"]]
            input_data = np.asarray([float(form_values[i]) for i in column_names]).reshape(
                1, -1
            )
            prediction_data = fertilizer_prediction(input_data)
            json_obj = json.dumps(prediction_data, default=convert)
            return json_obj
    except:
        return json.dumps({"error":"Please Enter Valid Data"}, default=convert)


if __name__ == "__main__":
    app.run(debug=True)
