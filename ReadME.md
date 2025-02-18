##  Insurance Prediction API(FastAPI)
This project provides an API for predicting insurance charges based on user input using a trained machine learning model 

##  Table of Contents
- [Description](...)
- [Requirements](...)
- [Getting Started](...)
- [1. Train and Save the Model](...)
- [2. Deploy FastAPI](...)
- [3. Run Streamlit](...)
- [Usage](...)
- [Endpoints](#endpoints)
- [Example Input and Output](...)
- [File Structure](...)
- [License](#lisence) 

##  Description


This streamlit application provides an API and a Streamlit application for predicting insurance charges based on users input. The model is trained on the following features:

- Age
- Gender
- BMI
- Number of children
- Smoker status
- Region

- ##  Requirements
To set up and run this project, you’ll need the following Python packages:
- `fastapi`
- `uvicorn`
- `scikit-learn`
- `pandas`
- `joblib`
- `numpy`
- `streamlit`
you can install these dependencies by running:
```bash
pip install -r requirements.txt
```

## Getting started 
follow these steps to set up and run the project.

1. Ensure the FASTAPI server is running on `http://127.0.0.1:8000`
2. Declare the `base_url` to your API in the `.env` file e.g. `BASE_URL=http://127.0.0.1:8000`
3. Run streamlit
The Streamlit app allows users to input values and retrieve prediction from the FASTAPI server. To start streamlit, run:
```bash
streamlit run app.py
```
The streamlit app will open in a browser window at `http:localhost:8501`.

## Usage

Streamlit Frontend
![streamlit frontend Image](![frontend_app.png](src%2Ffrontend_app.png)frontend_app.png)

-Input insurance features in the provided fields.
-Click the predict button to get the prediction.
-The prediction will display predicted insurance charges.

### Streamlit Application

The Streamlit app provides an interface for the users to input feature values and get predictions. When the predict button is clicked, the app sends the data to the FASTAPI server and displays whether predicted insurance charges 
Example Input and Output
Example Input:

Age= 45
Gender = Female
BMI = 28.7
Number of children = 2
Smoker status = yes
Region = Southeast

Example Output:

Predicted charges: $17,900.55
File Structure
The project directory is structured as follows:

📦 XGBoost_regressor frontend
├─ data
│  └─ data.csv
├─ model
│  ├─ model.pkl
├─ src
├─ .gitignore
├─ app.py
├─ api.py
├─ README.md
└─ requirements.txt

##License
This project is licensed under [![License: MIT](...)](...)