# ❤️ Heart Disease Prediction System

This project is a **Machine Learning web application** that predicts the risk of heart disease using patient health information.

The model is trained using medical data and deployed as an interactive **Streamlit web app** where users can enter patient details and instantly get a prediction.

---

# 🌐 Live Demo

Try the application here:

https://heart-disease-predictor-prathamesh.streamlit.app

---

# 📌 Project Overview

Heart disease is one of the leading causes of death worldwide.
This project demonstrates how **machine learning can help predict the risk of heart disease** based on medical attributes like age, cholesterol level, blood pressure, and heart rate.

The system allows users to enter patient information and get a prediction about whether the person is likely to have heart disease.

---

# 🧠 Machine Learning Model

The following ML models were explored:

* Logistic Regression
* Random Forest Classifier

After evaluation, **Random Forest** was used as the final model because it gave better accuracy.

Model evaluation metrics used:

* Accuracy
* Precision
* Recall
* F1 Score
* ROC-AUC Score

---

# ⚙️ Technologies Used

* Python
* Scikit-learn
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Streamlit
* SHAP (Explainable AI)

---

# 📊 Features of the Application

✔ Machine learning prediction model
✔ Interactive web interface
✔ User input for patient health data
✔ Real-time prediction result
✔ Probability of heart disease risk
✔ Feature importance visualization
✔ Explainable AI using SHAP
✔ Deployed as a live web application

---

# 🖥️ Application Interface

Example of the web interface:

(Add screenshots here)

You can add screenshots like:

* Main dashboard
* Input form
* Prediction result

---

# 📂 Project Structure

heart-disease-ml

│

├── app.py               # Streamlit web application

├── heart_model.pkl      # Trained machine learning model

├── model.ipynb          # Jupyter notebook for training the model

├── dataset/heart.csv    # Dataset used for training

├── requirements.txt     # Python dependencies

└── README.md            # Project documentation

---

# 🚀 How to Run This Project Locally

### 1️⃣ Clone the repository

git clone https://github.com/prathameshchaudhari2004/heart-disease-ml.git

### 2️⃣ Go to the project folder

cd heart-disease-ml

### 3️⃣ Install required libraries

pip install -r requirements.txt

### 4️⃣ Run the Streamlit application

streamlit run app.py

### 5️⃣ Open the browser

The app will run at:

http://localhost:8501

---

# 📈 Dataset

The dataset used for this project is the **UCI Heart Disease Dataset**.

It contains medical attributes such as:

* Age
* Sex
* Chest pain type
* Blood pressure
* Cholesterol level
* Heart rate
* Exercise induced angina
* ST depression

These features help the machine learning model determine the probability of heart disease.

---

# 👨‍💻 Author

**Prathamesh Chaudhari**

B.Tech Information Technology Student
Interested in Machine Learning, Data Science, and AI-based solutions.

GitHub:
https://github.com/prathameshchaudhari2004

---

# ⭐ If you like this project

Please consider giving this repository a **star ⭐** on GitHub.
