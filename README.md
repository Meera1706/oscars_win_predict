# 🎬 Oscars Prediction ML Project

An end-to-end **Machine Learning project** that predicts whether an Oscar nomination will win or not using historical data.

---

## 🚀 Project Overview

This project covers the complete ML lifecycle:

* Data Understanding & Cleaning
* Feature Engineering
* Model Training (Logistic, Random Forest, XGBoost)
* Model Evaluation (Precision, Recall, F1 Score)
* Model Selection
* Deployment using Streamlit

---

## 🎯 Problem Statement

Given features like:

* Year of film
* Award category

👉 Predict whether the nominee will **win an Oscar**.

This is a **binary classification problem**:

* 1 → Winner
* 0 → Not Winner

---

## 📊 Dataset

* Source: Oscars historical dataset
* Rows: ~11,000
* Features:

  * `year_film`
  * `canon_category`
  * `winner` (target)

---

## ⚙️ Models Used

| Model                        | Description          |
| ---------------------------- | -------------------- |
| Logistic Regression          | Baseline model       |
| Random Forest                | Ensemble model       |
| XGBoost                      | Boosting model       |
| Balanced Logistic Regression | Final selected model |

---

## 🏆 Final Model

👉 **Balanced Logistic Regression**

### Why?

* Handles class imbalance
* Improves recall (detects more winners)
* Best F1 Score among all models

---

## 📈 Evaluation Metrics

* Accuracy
* Precision
* Recall
* F1 Score

⚠️ Special focus on:

* **Recall** (important for detecting winners)
* **F1 Score** (balance between precision & recall)

---

## 🖥️ Streamlit App Features

* 📊 EDA Page
* 📈 Model Comparison
* 🔮 Prediction System
* 🧠 Explainability (basic)

---

## 📁 Project Structure

```
ml-oscars-project/
│
├── app.py
├── requirements.txt
│
├── model/
│   ├── model.pkl
│   ├── scaler.pkl
│   └── columns.pkl
│
├── pages/
│   ├── 1_EDA.py
│   ├── 2_Model_Comparison.py
│   ├── 3_Prediction.py
│   └── 4_Explainability.py
│
└── data/
    └── dataset.csv
```

---

## ▶️ How to Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

## 🌐 Live App

👉 Add your Streamlit link here after deployment

---

## 🧠 Key Learnings

* Handling imbalanced datasets
* Model evaluation beyond accuracy
* Feature selection and encoding
* Deploying ML models using Streamlit

---

## 📌 Future Improvements

* Add full SHAP visualizations
* Improve prediction UI
* Add more features (actor, film metadata)
* Hyperparameter tuning

---

## 👨‍💻 Author

Prarthna Patel

---

## ⭐ If you like this project

Give it a star on GitHub!
