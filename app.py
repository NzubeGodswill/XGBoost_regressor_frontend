import streamlit as st
import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the Base URL from the environment variables
base_url = os.getenv("Base_URL", "http://localhost:8000")

# Set page configuration
st.set_page_config(
    page_title="Insurance Charges Prediction",
    page_icon="💸",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Add a title and description
st.markdown(
    """
    <style>
    .main {
        background-color: #f9f9f9;
        padding: 20px;
        border-radius: 10px;
    }
    .title {
        font-size: 30px;
        font-weight: bold;
        color: #4CAF50;
    }
    .subtitle {
        font-size: 16px;
        color: #555;
        margin-bottom: 20px;
    }
    .footer {
        text-align: center;
        font-size: 14px;
        font-weight: bold;
        color: #777;
        margin-top: 50px;
    }
    </style>
    <div class="main">
        <h1 class="title">💸 Insurance Charges Prediction</h1>
        <p class="subtitle">Easily predict insurance charges based on user details. 
        Fill out the form below!</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# User Inputs
with st.form("user_input_form"):
    st.write("### User Details")

    age = st.number_input("Age:", min_value=0, max_value=120)
    sex = st.radio("🧑‍🤝‍🧑 Sex:", ["Female", "Male"], horizontal=True)
    sex = 0 if sex == "Female" else 1
    bmi = st.number_input("BMI (Body Mass Index):", min_value=0.0, max_value=100.0, value=25.0, step=0.1)
    children = st.slider("Number of Children:", min_value=0, max_value=10, value=0, step=1)
    smoker = st.radio("🚬 Smoker:", ["No", "Yes"], horizontal=True)
    smoker = 0 if smoker == "No" else 1
    region = st.selectbox("Region:", ["Northwest", "Southeast", "Southwest", "Northeast"])

    northwest, southeast, southwest = 0, 0, 0
    if region == "Northwest":
        northwest = 1
    elif region == "Southeast":
        southeast = 1
    elif region == "Southwest":
        southwest = 1

    # Submit button
    submitted = st.form_submit_button("Predict")

    if submitted:
        # Make API request
        api_url = f"{base_url}/api/predict"
        data = {
            "age": age,
            "sex": sex,
            "bmi": bmi,
            "children": children,
            "smoker": smoker,
            "northwest": northwest,
            "southeast": southeast,
            "southwest": southwest
        }

        with st.spinner("Fetching prediction..."):
            try:
                response = requests.post(api_url, json=data, timeout=10)  # Added timeout
                response.raise_for_status()  # Raise an error for HTTP error codes
                prediction = response.json().get("predicted_charges", None)

                if prediction is not None:
                    st.success(f"Predicted Insurance Charges: **${prediction:.2f}**")
                    st.balloons()
                else:
                    st.error("Error: Could not fetch prediction. Please check API response format.")
            except requests.exceptions.RequestException as e:
                st.error(f"API Error: {e}")

# Footer
st.markdown(
    """
    <div class="footer">
        Made with ❤️ using Streamlit
    </div>
    """,
    unsafe_allow_html=True,
)

