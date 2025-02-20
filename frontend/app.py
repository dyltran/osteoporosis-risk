import streamlit as st

st.title("Welcome to our Osteoporosis Risk Predictor")

#FOR SUPPORT VECTOR CLASSIFIER: factors that have a postive feature importance: age, prior factures, gender, hormonal changes, body weight, race ethnicity, alcohol consumption, physical activity, vitamin D intake, calcium intake

name = st.text_input("Enter your name!")
if name:
    print(f"Hello, {name}. Please provide the information below.")

age = st.slider("Choose your age.", 0, 150, 1)
    if number:
        st.write(f"You are {age} years old.")

st.write("Do you have prior fractures?")
if st.button("No"):
    prior_Fractures = "No"
if st.button("Yes"):
    prior_Fractures = "Yes"

st.write("What is your gender?")
if st.button("Female"):
    gender = "Female"
if st.button("Male"):
    gender = "Male"

st.write("Describe your homonal changes.")
if st.button("Normal"):
    hormonal_Changes = "Normal"
if st.button("Postmenopausal"):
    hormonal_Changes = "Postmenopausal"

st.write("Describe your body weight.")
if st.button("Normal"):
    body_Weight = "Normal"
if st.button("Underweight"):
    body_Weight = "Underweight"

st.write("Describe your race/ethnicity.")
if st.button("African American"):
    race_Ethnicity = "African American"
if st.button("Asian"):
    race_Ethnicity = "Asian"
if st.button("Caucasian"):
    race_Ethnicity = "Caucasian"

st.write("Describe your alcohol consumption")
    alcohol_consumption = "Light"
if st.button("Moderate"):
    alcohol_consumption = "Moderate"
if st.button("NaN"):
    alcohol_consumption = "NaN"

st.write("Describe your physical activity")
if st.button("Active"):
    physical_Activity = "Active"
if st.button("Sedentary"):
    physical_Activity = "Sedentary"

st.write("Describe your vitamin D intake")
if st.button("Insufficient"):
    vitamin_D_Intake = "Insufficient"
if st.button("Sufficient"):
    alcohol_consumption = "Sufficient"

st.write("Describe your calcium intake")
if st.button("Adequate"):
    calcium_Intake = "Adequate"
if st.button("Low"):
    calcium_Intake = "Low"








