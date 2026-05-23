# Used car price Prediction & recommendation System
## Project Overview
This project is a machine learning powered Used Car Price Prediction and Recommendation System built using python, scikit-learn, and streamlit. The system predicts the price of a Used car based on several features and also recomends similar cars based on user preferences ad budget.

## Dataset Features
* Brand
* Model Year
* Engine Size
* Fuel Type
* Transmission
* Mileage
* Doors
* Owner Count
* Horsepower
* Price
  
## Feature Engineering
Additinal features created:
* Car Age
* Mileage Per Year
* HP Per Engine
* Age x Mileage
* Multi Owner
* Is New Car

  Catgorical features were encoded:
 * Brand_Ford
 * Brand_Honda
 * Brand_Hyundai
 * Bran Tesla
 * Fuel_type_Hybrid
 * Fuel_type_Petrol
 * Transmission_manual

   
## Exploratory Data Analysis (EDA) & Preprocessing
Completed:
* Exploratory Data Analysis (EDA)
* Missing value checks
* Duplicate checks
* Skewness analysis
* Outlier visualization
* Correlation Heatmap
* Feature scaling using StandardScaler

  Findings:
* Skewness values fir mileage and price were close to 0, indicationg near - symmetric distributions.
* No major outlier issues were observed.
* Correlation analysis helped identify important predictive features.
  
## Models Used
Several regression models were trained and compared:

* Linear Regressgion
* Ridge Regression
* Lasso Regression
* SVR
* Decision Tree
* Random Forest
* Gradient Boosting
* XGBoost

  Hyperparameter tuning was performed using GridSearchCV.

## Best Model Performance

Lasso Regression

Performance:
* Test R(square) = 0.945
* MAE = 1750
* RMSE = 2120

  why it was selected:
* Highest Test R(square)
* Lowest MAE
* Lowest RSME
* Good generalization performance
  
## Recommendtion System
A content - based recommendation system was built using:

* Consine Similarity
* Standardized numerical features

  Capabilities:
* Similar car recommendations
* Budget-based filtering
* Recommendation comments/output display

This system reconstructs encoded values back into readable labels such as:
* Brand
* Fuel Type
* Transmission
  
## Challengies Encoutered
1. Encoded Features
   Challenge:
 * Original categorical columns were encoded and lost readibility.
   
   Solution:
 * Created decoding functions to restore readable brand,fuel type, and transmission names.

2. Recommendation Dataset Structure
   Challenge:
 * The recommendation dataset structure did not initially match the recommendation function
   
   Solution:
 * Created a seperate recommend_df using propoerly engineered and encoded features.

3. Feature Leakage
   Challenge:
 * Price accidentally remained inside recommendation features.

   Solution:
 * Removed te target variable from recommendation calculations.

 4. Columns Errors
    Chalenge:
 * Errors occured while dropping columns already removed earlier.

   Solution:
 * Verified active dataframe structure before transformations.

 5. Deployment Prepration
    Challege:
 * Understanding which files/models should be saved.

   Solution: Saved:
 * model.pkl
 * columns.pkl
 * scaler.pkl
 * similarity.pkl
 * recommend_data.csv

## Wins & Achievements
* Successfully completed full ML workflow
* Built both prediction and recommendation systems.
* Applied feature engineering techniques.
* Performed model tuning with GridSearhCV.
* Achieved strong predictive performance.
* Build a portfolio-level end-to-end machine Learning application.

## Technologies Used
* Python
* Pandas
* Numpy
* Scikit-learn
* XGBoost
* Matplotlib
* Seaborn
* Joblib
* Streamlit
   
## Future Improvements

Possible future upgrades:
* Add real-time car listings API
* Add image-based recommendations
* Improve UI/UX in Streamlit
* Add user authentication and favorites system
