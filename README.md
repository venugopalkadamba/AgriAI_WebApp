<div align="center">

# AgriAI Web Application

</div>

## About

<b>AgriAI</b> is a machine learning based we application build using React and Flask. AgriAI is used for recommending Crop and Fertilizers based on the soil features. The application used three accuractely predciting models to make the final predictions. The link for the python notebooks containing the implementation for the models are present in the <b><a href="#links">All Links</a></b> section of this Readme.<br/>

An API was built using Flask and was deployed on Heroku. This Flask API is used to get the recommendation made by the machine learning models in JSON format. The input data is sent as a POST request to the API to get the predicted information.<br/>

React JS was used to build the frontend part of the application. JS packages such as MaterialUI, Axios, react-router-dom were used for frontend part of the web application.<br/>

<b>Deployed Web Application Link: </b>https://agriai-app-a9c34.web.app
<br/>

<h3><b>Flask API End Points</b></h3>

1. Crop Recommendation End Point: https://agriculture-api.herokuapp.com/predict_crop
2. Fertilizer Recommendation End Point: https://agriculture-api.herokuapp.com/predict_fertilizer
   <br/>

<h3><b>About Data returned by Flask API</b></h3>

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

## Steps to run the React Application in local

1. Clone this repo.
2. Open command prompt in the following folder "React_Frontend/agri-ai"
3. Install all the npm packages

```
npm install
```

4. Start the application

```
npm start
```

The Application Runs on localhost:3000

## Steps to run the Flask API in local

1. Clone this repo
2. Open command prompt in "Flask_API"
3. Create a virtual environment

```
mkvirtualenv environment_name
```

4. Install all the packages

```
pip install -r requirements.txt
```

5. Run the app.py file

```
python app.py
```

## <span id="links">All Links</span>

1. <a href="https://www.kaggle.com/venugopalkadamba/croprecommendation-eda-visualization-modeling-99" target="_blank">Crop Recommender Notebook Link</a>
2. <a href="https://www.kaggle.com/venugopalkadamba/fertilizersrecommendation-acc-100-eda-upsampling" target="_blank">Fertilizer Recommender Notebook Link</a>
3. <a href="https://www.kaggle.com/atharvaingle/crop-recommendation-dataset" target="_blank">Crop Dataset Link</a>
4. <a href="https://www.kaggle.com/gdabhishek/fertilizer-prediction" target="_blank">Fertilizer Dataset Link</a>
5. <a href="https://agriai-app-a9c34.web.app" target="_blank">Deployed Web Application Link</a>

<b>NOTE: </b>Please do support by upvoting the kaggle notebooks if you liked my work.

## Tech Stack Used

<div align="center">

<table>
    <tr>
        <td><img src="./readme_assets/react.png" width="200px" height="200px" /></td>
        <td><img src="./readme_assets/firebase.png" width="200px" height="200px" /></td>
    </tr>
    <tr>
        <td><img src="./readme_assets/flask.png" width="200px" height="200px" /></td>
        <td><img src="./readme_assets/heroku.jpg" width="200px" height="200px" /></td>
    </tr>
</table>

<img src="./readme_assets/scikit.png" width="400px" height="200px" />
</div>

<br/>

## Demo Of Web Application

<img src="./readme_assets/lappy_gif.gif" />

<div align="center">

Please do ⭐ this repo if you liked my work.

</div>
