# 🌍 Nationality Detection System (ML)

An AI-powered web application that analyzes a person's image to predict **nationality, emotion, age, and dress color** using Machine Learning and Computer Vision techniques.

---

## 🚀 Project Overview

This project is built as part of an internship task to demonstrate the use of **Machine Learning models in real-world applications**.

The system takes an input image and performs:

* Face analysis using Deep Learning
* Emotion recognition
* Age prediction
* Nationality classification (based on race)
* Dress color detection using image processing

---

## 🎯 Features

* 📤 Upload Image Interface (Streamlit UI)
* 🌎 Nationality Detection
* 😊 Emotion Detection
* 🎂 Age Prediction
* 🎨 Dress Color Detection
* ⚙️ Conditional Output Logic:

  * **Indian** → Age + Dress Color + Emotion
  * **USA** → Age + Emotion
  * **African** → Dress Color + Emotion
  * **Other** → Basic Output

---

## 🧠 Machine Learning Concept

This project is an **ML-based application** using **pre-trained deep learning models**:

* DeepFace for:

  * Age prediction
  * Emotion detection
  * Race detection
* Custom logic for nationality mapping
* OpenCV for image processing and color detection

> ⚠️ Note: The model is not trained from scratch. Pre-trained models are used and integrated into a real-world application.

---

## 🛠️ Technologies Used

* Python 🐍
* Streamlit 🌐
* OpenCV 👁️
* DeepFace 🤖
* NumPy 🔢

---

## 📂 Project Structure

```
nationality_detection/
│
├── app.py                  # Main Streamlit Application
├── requirements.txt       # Dependencies
├── utils/
│   └── color_utils.py     # Dress Color Detection Logic
├── model/                 # (Optional future models)
├── sample/                # Sample images
├── result/                # Output results
```

---

## ▶️ How to Run the Project

### 1️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 2️⃣ Run the Application

```bash
python -m streamlit run app.py
```

### 3️⃣ Open in Browser

```
http://localhost:8501
```

---

## 📊 Example Output

* 🌎 Nationality: Indian
* 😊 Emotion: Happy
* 🎂 Age: 28
* 🎨 Dress Color: Blue

---

## 💡 Key Highlights

* Real-time AI-based predictions
* Clean and interactive UI
* Uses Deep Learning without training from scratch
* Combines ML + Logic-based decision making

---

## 📌 Future Improvements

* Real nationality dataset training
* Improve dress color accuracy
* Add confidence scores
* Deploy on cloud (Streamlit Cloud / AWS)

---

## 👨‍💻 Author

**Raghuveer3339**

---

## ⭐ Conclusion

This project demonstrates how **Machine Learning models can be integrated into practical applications** with a user-friendly interface, making AI accessible and interactive.

---
