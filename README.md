# 🏏 CricketPulse – Real-Time T20 Score Predictor

CricketPulse is a machine learning-powered web application designed to predict T20 cricket match scores using real-time match data and advanced ML algorithms. It helps fans, analysts, and teams make better decisions during a game using dynamic and data-driven predictions.



## ⚠️ Problem Statement

Predicting scores in T20 cricket is challenging due to:

- Rapid game dynamics
- Sudden wicket losses
- Changing run rates
- Diverse pitch and ground conditions

Most existing tools fail to handle this complexity. CricketPulse addresses this gap with a robust ML-based prediction model.

---

## 🎯 Objectives

- Build a machine learning model to predict T20 match scores using live inputs like overs, runs, and wickets.
- Design a user-friendly web interface for input and output.
- Integrate real-time ML predictions with a functional web app using modern tech stacks.

---



## 🛠️ Tech Stack

### 🔹 Frontend
- HTML
- CSS
- JavaScript

### 🔹 Backend
- Django

### 🔹 Machine Learning
- Python
- Pandas
- XGBoost
- Pickle (for model serialization)

---

## 🔄 Workflow

1. **Data Acquisition**: Fetch YAML-format data from Cricksheet
2. **Conversion**: YAML → Pandas DataFrame
3. **Data Cleaning & Processing**
4. **EDA**: Explore and visualize data
5. **Train-Test Split**
6. **Feature Engineering**: OneHotEncoding, Scaling
7. **Model Training**: XGBoost
8. **Model Saving**: Store model using Pickle
9. **Integration**: Django backend loads model and serves predictions
10. **UI Interaction**: Frontend takes user input and shows predicted score

---

## 📊 Results

- Clean UI for users to enter match conditions (team, overs, runs, wickets, venue)
- Real-time score predictions
- Evaluation:
  - R² Score (Goodness of Fit)
  - Mean Absolute Error (MAE)

---



