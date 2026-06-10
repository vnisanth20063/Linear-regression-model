import streamlit as st
import pandas as pd
from pickle import load
st.title("Let's Predict")


selected_model=st.sidebar.selectbox("Select a model",options= ["Linear Regression"])


if selected_model=="Linear Regression":
   var= st.sidebar.selectbox("Choose prediction",options=["House price prediction","Salary prediction"])
   if var == "House price prediction":
      longitude=st.number_input("Enter Latitude")
      latitude=st.number_input("Enter Longitude")
      housing_median_age=st.number_input("Enter Age of house")
      t_rooms=st.number_input("Enter Total rooms")
      population=st.number_input("Enter Population")
      median_income=st.number_input("Enter Income")
      popula_tion=st.number_input("Enter count of house in a area")
      house_data=pd.DataFrame({"longitude":[longitude],
                    "latitude":[latitude],                          
                    "housing_median_age":[housing_median_age],
                    "t_rooms":[t_rooms],
                    "population":[population]
                    ,"median_income":[median_income],
                    "popula_tion":[popula_tion]})
      btn=st.button("Predict")
      with open("House prediction ml.pkl", "rb") as file:
         h_model=load(file)
      if btn:
         prediction=model.predict(house_data)
         st.success(prediction)
   elif var =="Salary prediction":
      Years_of_Experience=st.number_input("Enter your experience")
      b= st.button("Predict")
      salry=pd.DataFrame({"Years of Experience":[Years_of_Experience]})
      with open("Salary prediction ml.pkl", "rb") as f:
       loaded_model=load(f)
      if b:
       prdct=loaded_model.predict(salry)
       st.success(prdct)

       