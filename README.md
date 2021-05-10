<div align="center">

# AgriAI Web Application

</div>

## About

<b>AgriAI</b> is a machine learning based we application build using React and Flask. AgriAI is used for recommending Crop and Fertilizers based on the soil features. The application used three accuractely predciting models to make the final predictions. The link for the python notebooks containing the implementation for the models are present in the <b>Links</b> section of this Readme.<br/>

An API was built using Flask and was deployed on Heroku. This Flask API is used to get the recommendation made by the machine learning models in JSON format. The input data is sent as a POST request to the API to get the predicted information.<br/>

React JS was used to build the frontend part of the application. JS packages such as MaterialUI, Axios, react-router-dom were used for frontend part of the web application.<br/>

<b>Deployed Web Application Link: </b>https://agriai-app-a9c34.web.app
<br/>

<h3><b>About Flask API</b><h3>

1. Crop Recommendation End Point: https://agriculture-api.herokuapp.com/predict_crop
2. Fertilizer Recommendation End Point: https://agriculture-api.herokuapp.com/predict_fertilizer
   <br/>

<h3><b>About Data returned by Flask API</b><h3>

The data is returned in JSON format:<br/>

1. <b>For Crop Recommendation</b>

```
{
    xgb_model_prediction: "rice",
    xgb_model_probability: 99.2%,
    rf_model_prediction: "rice",
    rf_model_probability: 99.3%,
    knn_model_prediction: "rice",
    knn_model_probability: 99.5%,
    final_prediction: "rice",
}
```

<br/>

2. <b>For Fertilizer Recommendation</b>

```
{
    xgb_model_prediction: "Urea",
    xgb_model_probability: 99.2%,
    rf_model_prediction: "Urea",
    rf_model_probability: 99.3%,
    svm_model_prediction: "Urea",
    svm_model_probability: 99.5%,
    final_prediction: "Urea",
}
```

<br/>
<b>Note:</b> This API can be used in your Web Application or Mobile Application by just sending a POST request with the necessary input data to the above mentioned end points.

## Tech Stack Used

<img src="./readme_assets/react.png" width="200px" height="200px" />

<img src="./readme_assets/firebase.png" width="200px" height="200px" />

<img src="./readme_assets/flask.png" width="200px" height="200px" />

<img src="./readme_assets/heroku.jpg" width="200px" height="200px" />

<br/>
<img src="./readme_assets/scikit.png" width="400px" height="200px" />

<br/>

<div align="center">

Please do ⭐ this repo if you liked my work.

</div>
