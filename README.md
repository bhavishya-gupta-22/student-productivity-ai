# 🎓 Student Productivity AI

**Course Project:** Fundamentals of AI and ML (BYOP)
**Developer:** Bhavishya Gupta
**Registration Number:** 25BCE10588
**Deadline:** March 31, 2026

---

## 📌 Project Overview

**Student Productivity AI** is a data-driven web application designed to help students analyze, predict, and optimize their daily routines.

Unlike a simple calculator, this tool uses a **Machine Learning regression model** trained on student behavioral data to generate a **Productivity Score (out of 100%)**.

The goal is to bridge the gap between **“working hard”** and **“working smart”** by identifying key habits — such as sleep, stress, and screen time — that act as bottlenecks to academic success.

---

## 🚀 Live Demo

🔗 [Click Here to View the App](https://student-efficiency-ai.streamlit.app/)

---

## 🧠 Features

* **🤖 AI Productivity Prediction**
  Uses 14 input parameters (study hours, sleep, stress, coffee intake, etc.) to predict efficiency.

* **📊 Data-Driven "What-If" Scenarios**
  Simulates how changing one habit (e.g., +1 hour of sleep) impacts productivity.

* **⚠️ Smart Validation System**
  Prevents impossible inputs using a "Time Paradox" engine (ensures total time ≤ 24 hours).

* **💡 Personalized AI Insights**
  Provides targeted feedback only when weak areas (e.g., high stress, low sleep) are detected.

* **📈 Persistence & Trend Tracking**
  Saves predictions to a CSV file and visualizes progress over time using line charts.

---

## 🛠️ Tech Stack

* **Language:** Python 3.x
* **Framework:** Streamlit
* **Data Analysis:** Pandas, NumPy
* **Visualization:** Plotly Express
* **Machine Learning:** Scikit-Learn (Linear Regression / Random Forest)

---

## 📂 Project Structure

```
student-productivity-ai/
├── app.py                      # Main Streamlit application & UI logic
├── requirements.txt            # Dependencies for deployment
├── productivity_history.csv    # Local database for tracking trends
├── README.md                   # Project documentation
└── src/
    ├── predict.py              # ML inference & logic
    └── model.pkl               # Trained ML model
```

---

## ⚙️ Installation & Local Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/student-productivity-ai.git
cd student-productivity-ai
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Application

```bash
streamlit run app.py
```

---

## 📈 ML Model Details

The model is trained on student behavioral data with the following key features:

### 📚 Academic Factors

* Attendance %
* Assignments Completed
* Study Hours

### 🧘 Health Factors

* Sleep Hours
* Exercise Minutes
* Coffee Intake

### 📱 Distractions

* Social Media Usage
* YouTube Time
* Gaming Time

### 🧠 Mental State

* Stress Level (1–5)
* Focus Score (1–100)

### 🔍 What-If Analysis Logic

The system performs sensitivity analysis by:

* Holding 13 variables constant
* Changing 1 variable (e.g., sleep)
* Re-running the model
* Measuring the impact on productivity score

---

## 📝 Reflection

This project explores the intersection of **behavioral science** and **machine learning**.

One of the biggest challenges was avoiding generic AI advice. To solve this, a concept of **Selective Intelligence** was implemented — the system only provides suggestions when data indicates a statistically significant weakness.

This makes the AI feel **purposeful, contextual, and intelligent**, rather than scripted.

---

## ⭐ Future Improvements

* Add user authentication system
* Deploy cloud database (Firebase / Supabase)
* Improve model accuracy with larger datasets
* Add mobile responsiveness

---

## 🙌 Acknowledgements

Built as part of the **Fundamentals of AI and ML** course project.

---

## 📸 App Preview

![Screenshot](screenshots/Screenshot (35).png)
![Screenshot](screenshots/Screenshot (36).png)
![Screenshot](screenshots/Screenshot (37).png)
![Screenshot](screenshots/Screenshot (38).png)
![Screenshot](screenshots/Screenshot (39).png)

---

## 📬 Contact

**Bhavishya Gupta**
+91 8707399551


