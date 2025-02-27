import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os
from sklearn.preprocessing import StandardScaler

st.title("Welcome to our Osteoporosis Risk Predictor")
#FOR SUPPORT VECTOR CLASSIFIER: factors that have a postive feature importance: age, prior factures, gender, hormonal changes, body weight, race ethnicity, alcohol consumption, physical activity, vitamin D intake, calcium intake

# Name Input
name = st.text_input("Enter your name!")
if name:
    st.write(f"Hello, {name}. Please provide the information below.")

# Age Input
age = st.slider("Choose your age.", 0, 150, 1)
if age:
    st.write(f"You are {age} years old.")

base_dir = os.path.dirname(os.path.abspath(__file__))

curr_path = os.path.join(base_dir, "scalers", "logistic_regression_scaler.pkl")
logistic_regression_scaler = joblib.load(curr_path)
logistic_regression_age_scaled = logistic_regression_scaler.transform([[age]])

curr_path = os.path.join(base_dir, "scalers", "support_vector_machine_scaler.pkl")
support_vector_machine_scaler = joblib.load(curr_path)
support_vector_machine_age_scaled = support_vector_machine_scaler.transform([[age]])

curr_path = os.path.join(base_dir, "scalers", "decision_tree_scaler.pkl")
decision_tree_scaler = joblib.load(curr_path)
decision_tree_age_scaled = decision_tree_scaler.transform([[age]])

# Gender Input
gender = st.selectbox("What is your gender?", ["Female", "Male"])
gender_encoded = 1 if gender == "Male" else 0

# Hormonal Changes Input
hormonal_changes = st.selectbox("Describe your hormonal changes.", ["Normal", "Postmenopausal"])
hormonal_changes_encoded = 1 if hormonal_changes == "Postmenopausal" else 0

# Family History Input
family_history = st.selectbox("Does your family have a history of osteoporosis?", ["No", "Yes"])
family_history_encoded = 1 if family_history == "Yes" else 0

# Race/Ethnicity Input
race = st.selectbox("Describe your race/ethnicity.", ["African American", "Asian", "Caucasian"])
race_map = {"African American": 0, "Asian": 1, "Caucasian": 2}
race_encoded = race_map[race]

# Body Weight Input
body_weight = st.selectbox("Describe your body weight.", ["Normal", "Underweight"])
body_weight_encoded = 1 if body_weight == "Underweight" else 0

# Calcium Intake Input
calcium_intake = st.selectbox("Describe your calcium intake.", ["Adequate", "Low"])
calcium_intake_encoded = 1 if calcium_intake == "Low" else 0

# Vitamin D Intake Input
vitamin_d_intake = st.selectbox("Describe your vitamin D intake.", ["Sufficient", "Insufficient"])
vitamin_d_intake_encoded = 1 if vitamin_d_intake == "Insufficient" else 0

# Physical Activity Input
physical_activity = st.selectbox("Describe your physical activity.", ["Active", "Sedentary"])
physical_activity_encoded = 1 if physical_activity == "Active" else 0

# Smoking Input
smoking = st.selectbox("Do you smoke?", ["No", "Yes"])
smoking_encoded = 1 if smoking == "Yes" else 0

# Alcohol Consumption Input
alcohol_consumption = st.selectbox("Describe your alcohol consumption.", ["None", "Moderate"])
alcohol_consumption_encoded = 1 if alcohol_consumption == "Moderate" else 0

# Medical Condition Input
medical_condition = st.selectbox("Do you have any of these medical conditions?", ["Hyperthyroidism", "None", "Rheumatoid Arthritis"])
medical_condition_map = {"Hyperthyroidism": 0, "None": 1, "Rheumatoid Arthritis": 2}
medical_condition_encoded = medical_condition_map[medical_condition]

# Medications Input
medications = st.selectbox("Do you take this medication?", ["Corticosteroids", "None"])
medications_encoded = 1 if medications == "None" else 0

# Prior Fractures Input 
prior_fracture = st.selectbox("Do you have prior fractures?", ["No", "Yes"])
prior_fracture_encoded = 1 if prior_fracture == "Yes" else 0

# Creating DataFrame for logistic regression model input
user_df = pd.DataFrame({
    'age': [logistic_regression_age_scaled],
    'gender': [gender_encoded],
    'hormonal_changes': [hormonal_changes_encoded],
    'family_history': [family_history_encoded],
    'race': [race_encoded],
    'body_weight': [body_weight_encoded],
    'calcium': [calcium_intake_encoded],
    'vitamin_d': [vitamin_d_intake_encoded],
    'physical_activity': [physical_activity_encoded],
    'smoking': [smoking_encoded],
    'alcohol_consumption': [alcohol_consumption_encoded],
    'medical_condition': [medical_condition_encoded], 
    'medications': [medications_encoded],
    'prior_fracture': [prior_fracture_encoded]
})

# Load Model
curr_path = os.path.join(base_dir, "models", "logistic_regression_model.pkl")
model = joblib.load(open(curr_path, "rb"))

if st.button("Predict Osteoporosis Risk using Logistic Regression Model"):
    prediction = model.predict(user_df)
    risk = "positive" if prediction == 1 else "negative"
    st.write(f"### We predict {risk} risk of osteoporosis.")

# Creating DataFrame for support vector machine model input
user_df = pd.DataFrame({
    'age': [support_vector_machine_age_scaled],
    'gender': [gender_encoded],
    'hormonal_Changes': [hormonal_changes_encoded],
    'family_History': [family_history_encoded],
    'race_Ethnicity': [race_encoded],
    'body_Weight': [body_weight_encoded],
    'calcium_Intake': [calcium_intake_encoded],
    'vitamin_D_Intake': [vitamin_d_intake_encoded],
    'physical_Activity': [physical_activity_encoded],
    'smoking': [smoking_encoded],
    'alcohol_Consumption': [alcohol_consumption_encoded],
    'medical_Conditions': [medical_condition_encoded],
    'medications': [medications_encoded],
    'prior_Fractures': [prior_fracture_encoded],
})

curr_path = os.path.join(base_dir, "models", "support_vector_machine_model.pkl")
model = joblib.load(open(curr_path, "rb"))

if st.button("Predict Osteoporosis Risk using Support Vector Machine Model"):
    prediction = model.predict(user_df)
    risk = "positive" if prediction == 1 else "negative"
    st.write(f"### We predict {risk} risk of osteoporosis.")

# Creating DataFrame for support decision tree model input
user_df = pd.DataFrame({
    'age': [decision_tree_age_scaled],
    'gender': [gender_encoded],
    'hormonal_changes': [hormonal_changes_encoded],
    'family_history': [family_history_encoded],
    'race_ethnicity': [race_encoded],
    'body_weight': [body_weight_encoded],
    'calcium_intake': [calcium_intake_encoded],
    'vitamin_d_intake': [vitamin_d_intake_encoded],
    'physical_activity': [physical_activity_encoded],
    'smoking': [smoking_encoded],
    'alcohol_consumption': [alcohol_consumption_encoded],
    'medical_conditions': [medical_condition_encoded],
    'medications': [medications_encoded],
    'prior_fractures': [prior_fracture_encoded],
})

curr_path = os.path.join(base_dir, "models", "decision_tree_model.pkl")
model = joblib.load(open(curr_path, "rb"))

if st.button("Predict Osteoporosis Risk using Decision Tree Model"):
    prediction = model.predict(user_df)
    risk = "positive" if prediction == 1 else "negative"
    st.write(f"### We predict {risk} risk of osteoporosis.")