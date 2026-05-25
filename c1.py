import streamlit as st
import pandas as pd
import numpy as np
import joblib
from sklearn.metrics.pairwise import cosine_similarity

#======================================================================================================================
# Page Layout
#======================================================================================================================

st.set_page_config(
    page_title=" Car Price Predition System.",
    layout="wide"
)

st.title("🚗 Used Car Price Prediction & Recommendation System")

#======================================================================================================================
# Load Files
#======================================================================================================================

model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")
similarity = joblib.load("similarity.pkl")

recommend_df= pd.read_csv("recommend_data.csv")
df = pd.read_csv("full_car_data.csv")

# columns = joblib.load("columns.pkl")

#======================================================================================================================
# SIDEBAR INPUTS
#======================================================================================================================

st.sidebar.header("Enter Car Details")

engine_size = st.sidebar.slider(
    "Engine Size",
    1.0,
    6.0,
    2.0
)

mileage = st.sidebar.slider(
    "Mileage",
    min_value=0,
    value=500000,
)

doors= st.sidebar.selectbox(
"Doors",
[2,3,4,5]
)

owner_count = st.sidebar.selectbox(
"Owner Count",
[1,2,3,4]
)

horsepower = st.sidebar.slider(
    "Horsepower",
    50,500,200
)

car_age = st.sidebar.slider(
"Car Age",
0,20,5
)

fuel_type = st.sidebar.selectbox(
"Fuel Type",
["Petrol","Hybrid", "Electric"] 
)

transmission = st.sidebar.selectbox(
"Transmission",
["Manual", "Automatic"] 
)

brand = st.sidebar.selectbox(
"Brand",
["Toyota","Ford" ,"Honda",  "Hyundai", "Tesla"]
)


#======================================================================================================================
# ENCODING
#======================================================================================================================

brand_ford = 1 if brand == "Ford" else 0
brand_honda = 1 if brand == "Honda" else 0
brand_hyundai = 1 if brand == "Hyundai" else 0
brand_tesla = 1 if brand == "Tesla" else 0

fuel_type_electric = 1 if fuel_type == "Electric" else 0
fuel_type_hybrid = 1 if fuel_type == "Hybrid" else 0
fuel_type_petrol = 1 if fuel_type == "Petrol" else 0

transmission_manual = 1 if transmission == "Manual" else 0

#======================================================================================================================
# FEATURE ENGINEERING
#======================================================================================================================

mileage_per_year = mileage / (car_age + 1)

hp_per_engine = horsepower / engine_size

age_x_mileage = car_age * mileage

multi_owner = 1 if owner_count > 1 else 0

is_new_car = 1 if car_age <= 2 else 0


#======================================================================================================================
# CREATE INPUT DATAFRAME
#======================================================================================================================

input_data = pd.DataFrame([{
"engine_size": engine_size,
"mileage": mileage,
"doors": doors,
"owner_count": owner_count,
"horsepower": horsepower,
"car_age": car_age,
"brand_ford": brand_ford,
"brand_honda": brand_honda,
"brand_hyundai": brand_hyundai,
"brand_tesla": brand_tesla,
"fuel_type_electric": fuel_type_electric,
"fuel_type_hybrid": fuel_type_hybrid,
"fuel_type_petrol": fuel_type_petrol,
"transmission_manual": transmission_manual,
"mileage_per_year": mileage_per_year,
"hp_per_engine": hp_per_engine,
"age_x_mileage": age_x_mileage,
"multi_owner": multi_owner,
"is_new_car": is_new_car
}])


#======================================================================================================================
# REORDER COLUMNS
#======================================================================================================================

# input_data = input_data[columns]

#======================================================================================================================
# PREDICTION
#======================================================================================================================

if st.button("Predict Price"):

    #scaled Input
    scaled_input = scaler.transform(input_data)

    #Predict price
    prediction = model.predict(scaled_input)

    # save prediction
    st.session_state.predicted_price = prediction[0]

     
    # Display result 
    st.success(
      f"Estimated Car Price: ${
   st.session_state.predicted_price:,.2f}"
    )


#======================================================================================================================
#                                              SIMILAR CAR RECCOMENDATION
#======================================================================================================================    

if  st.button("🔍 Find Similar Cars"):

    # Check if prediction exists
    if 'predicted_price' not in st.session_state:
      st.warning("Please predict the price first.")
        
    else:
      predicted_price = st.session_state.predicted_price    

      st.subheader("🔍 Similar Cars Recommendation")

    # Copy dataframe
      similar_cars = df.copy()

    # Filter similar prices
    similar_cars = similar_cars[
        (similar_cars['price'] >= predicted_price - 15000) &  
        (similar_cars['price'] <= predicted_price + 15000)
    ]

    # find closest price
    similar_cars['price_difference'] = abs(
        similar_cars['price']-predicted_price
    )
    
    # Sorted by closest price
    similar_cars = similar_cars.sort_values(by ='price_difference'
     )

    # Top 5 cars
    similar_cars = similar_cars.head(5)
      

    for i,row in similar_cars.iterrows():
         
#======================================================================================================================
# BRAND DECODER
#======================================================================================================================
      if row['brand_ford'] == 1:
          decoded_brand ="Ford"   
    
      elif row['brand_honda'] == 1:
          decoded_brand = "Honda"
    
      elif row['brand_hyundai'] == 1:
          decoded_brand = "Hyundai"
    
      elif row['brand_tesla'] == 1:
          decoded_brand = "Tesla"
    
      else:
          decoded_brand = "Toyota"         
      
          st.write("Brand:", decoded_brand)
          st.write(f"Price: ${row['price']:,.2f}")
          st.write(f"Mileage:", row['mileage'])
          st.write(f"Horsepower:", row['horsepower'])
          st.write("---")

    
#======================================================================================================================
# FUEL DECODER
#======================================================================================================================
    
    if row['fuel_type_electric'] == 1:
        decoded_fuel = "Electric"
    
    elif row['fuel_type_hybrid'] == 1:
        decoded_fuel = "Hybrid"
    
    else:
        decoded_fuel =  "Petrol"


#======================================================================================================================
# TRANSMISSION DECODER
#======================================================================================================================


    if row['transmission_manual'] == 1:
        decoded_transmission = "Manual"
    
    else:
        decoded_transmission = "Automatic"      
    
#======================================================================================================================
#                         ================== BUDGET RECOMMENDATION =================
#======================================================================================================================
st.subheader("🔍 Budget Cars Recommendation")

budget = st.number_input("Enter your budget", min_value=0, value=20000, step=1000, max_value=int(df['price'].max()))

if st.button("Find Budget Cars"):

  budget_cars= df[df['price'] <= budget]         

  if budget_cars.empty:
    st.warning("No cars available within the specified budget.")

  else:
    budget_cars = budget_cars.head(5)    

    for i, row in budget_cars.iterrows():
         
         
#======================================================================================================================
#  BRAND DECODER
#======================================================================================================================

       if row['brand_ford'] == 1:
        decoded_brand ="Ford"
    
       elif row['brand_honda'] == 1:
        decoded_brand = "Honda"
    
       elif row['brand_hyundai'] == 1:
        decoded_brand = "Hyundai"
    
       elif row['brand_tesla'] == 1:
        decoded_brand = "Tesla"
    
       else:
         decoded_brand = "Toyota"

#======================================================================================================================
#                                                 DISPLAY RESULT
#======================================================================================================================

        
         st.write(f"### {decoded_brand}")
         st.write(f"Price: ${row['price']:,.2f}")
         st.write(f"Mileage: {row['mileage']}")
         st.write(f"Horsepower: {row['horsepower']}")
         st.write("---")
        

