import streamlit as st
import pandas as pd
import joblib

house_model = joblib.load("house_model.pkl")
columns = joblib.load("columns.pkl")

area_names = {}
for c in columns:
    if c.startswith("Area_"):
        show_name = c.replace("Area_", "", 1).strip()
        area_names[show_name] = c

st.title("Karachi House Price Prediction")      

area = st.selectbox("Area / Location", sorted(area_names.keys()))
size = st.number_input("Size (sq yards)", min_value = 20 , value = 120)
bedrooms = st.number_input("Bedrooms", min_value= 1 , value= 3 )
bathrooms = st.number_input("Bathrooms", min_value = 1, value = 2)

if st.button("predict"):
    row = {}
    for c in columns:
        row[c] = 0

    row["AreaSqYards"]  = size
    row["NoOfBedrooms"] = bedrooms
    row["NoOfBathrooms"] = bathrooms 
    row[area_names[area]] = 1

    data = pd.DataFrame([row], columns = columns)
    price = house_model.predict(data)[0]
    st.success("Estimated Price Rs." + format(int(price), ","))