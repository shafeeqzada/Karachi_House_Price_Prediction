# Karachi House Price Prediction

A machine learning project that predicts house prices in Karachi based on location, size, bedrooms, and bathrooms. The model is deployed as a Streamlit web app.

**Live Demo:** [https://karachi-housepriceprediction.streamlit.app/]

## Dataset
- Source: Kaggle (Karachi House Prices 2023), `Cleaned_Data.csv`
- Rows: 16,849
- Features: Area (location), NoOfBedrooms, NoOfBathrooms, AreaSqYards
- Target: Price

## Project Steps
1. Data cleaning (rare areas grouped into "Rare Area" / "other")
2. Exploratory data analysis (price distribution, area-wise prices, feature importance)
3. Encoded the Area column using `get_dummies`
4. Trained and compared multiple models
5. Saved the best model (Random Forest) and deployed it with Streamlit

## Model Results

| Model | Test R² |
|---|---|
| Linear Regression | 0.799 |
| Decision Tree (depth 10) | 0.822 |
| Polynomial Regression (degree 2) | 0.833 |
| **Random Forest** | **0.849** |

- Best model: Random Forest (Test MAE approx. 8.0M PKR)
- Most important feature: AreaSqYards

## Tech Stack
Python, pandas, scikit-learn, matplotlib, joblib, Streamlit

## Project Structure
```
├── app.py               # Streamlit app
├── house_model.pkl      # Trained Random Forest model
├── columns.pkl          # List of model input columns
├── requirements.txt     # Dependencies
├── notebook.ipynb       # Cleaning, EDA, and model training
└── README.md
```

## How to Run Locally
```
pip install -r requirements.txt
streamlit run app.py
```

## Limitations
- The model performs best on areas and value ranges seen during training.
- Prices are based on 2023 data and may differ from the current market.

## Author
[Shafiq Zada]
