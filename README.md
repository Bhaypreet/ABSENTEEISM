# Absenteeism Prediction using Logistic Regression, Random Forest, and XGBoost

This project predicts employee absenteeism using three different machine learning models:  
**Logistic Regression**, **Random Forest**, and **XGBoost**. It includes end-to-end data  
preprocessing, model building, evaluation, and a **Streamlit app** for interactive predictions.

---

## 🚀 Project Overview

### 🎯 Objective
To build a predictive system that identifies whether an employee will be absent based on various personal and work-related factors.

### 🧠 Models Implemented
- ✅ Logistic Regression (baseline)
- ✅ Random Forest Classifier
- ✅ XGBoost Classifier

### 🛠 Tools Used
- Python, pandas, scikit-learn, xgboost
- Streamlit (for model deployment)

---

## 📊 Dataset Features

The dataset includes the following preprocessed features:

| Feature                        | Description                             |
|-------------------------------|-----------------------------------------|
| `reason_G0` to `reason_G3`    | Reason for absence (one-hot encoded)    |
| `Day of the week`             | Day on which employee is absent         |
| `month_value`                 | Month of absence                        |
| `Transportation Expense`      | Daily transportation cost               |
| `Distance to Work`            | Distance from home to office            |
| `Age`                         | Age of the employee                     |
| `Daily Work Load Average`     | Average work hours                      |
| `Body Mass Index`             | BMI value of employee                   |
| `Education`                   | 0 = High School or less, 1 = Higher Ed  |
| `Children`, `Pets`            | Family-related attributes               |

The target variable is **binary**:  
- `1`: Employee is likely to be absent  
- `0`: Employee is not likely to be absent

---

## 📈 Model Training & Evaluation

| Model              | Accuracy | Precision | Recall | F1-Score |
|-------------------|----------|-----------|--------|----------|
| Logistic Regression | ✅ Baseline model |
| Random Forest       | ✅ Used for better interpretability |
| XGBoost             | ✅ Final model for highest accuracy |

> Evaluation includes confusion matrix and classification report.

---

## 💻 Streamlit App

An interactive Streamlit app is provided to allow HR teams or analysts to make predictions by inputting employee attributes.

### 🔧 To Run Locally

1. **Clone this repository**  
   ```bash
   git clone https://github.com/yourusername/absenteeism-prediction.git
   cd absenteeism-prediction
