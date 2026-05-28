# 🎵 EchoTune - Music Recommender System

EchoTune is an AI-powered music recommendation web application built using **Python**, **Streamlit**, and **Machine Learning**.
It recommends similar songs based on content similarity using TF-IDF vectorization and cosine similarity.

## 🚀 Live Demo

🌐 Live Application: https://echotune-music-recommender.onrender.com/

---

# ✨ Features

* 🎧 Smart music recommendations
* 🔍 Search songs instantly
* 🤖 ML-based recommendation engine
* ⚡ Fast and interactive UI with Streamlit
* ☁️ Deployed on Render

---

# 🛠️ Tech Stack

## Frontend

* Streamlit

## Backend

* Python

## Machine Learning

* Scikit-learn
* TF-IDF Vectorizer
* Cosine Similarity

## Libraries Used

* Pandas
* NumPy
* Joblib

---

# 📂 Project Structure

```bash
EchoTune-Music-Recommender/
│
├── app.py
├── requirements.txt
├── Music_Recommendation_System.ipynb
│
├── models/
│   ├── music_df.pkl
│   ├── similarity.pkl
│   └── tfidf.pkl
│
└── README.md
```

---

# ⚙️ Installation

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/mr-gaurav-kumar/EchoTune-Music-Recommender.git
```

## 2️⃣ Navigate to Project Folder

```bash
cd EchoTune-Music-Recommender
```

## 3️⃣ Create Virtual Environment

```bash
python -m venv venv
```

## 4️⃣ Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

## 5️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

## 6️⃣ Run Application

```bash
streamlit run app.py
```

---

# 🧠 How It Works

1. Music data is preprocessed
2. TF-IDF vectorization converts text into numerical vectors
3. Cosine similarity calculates similarity scores
4. The system recommends songs with highest similarity

---

# 📸 Preview
<img width="1897" height="872" alt="image" src="https://github.com/user-attachments/assets/0c08ffb4-6ec4-4ca6-8fa7-9169a340b444" />

<!-- <img width="100%" alt="EchoTune Preview" src="https://via.placeholder.com/1200x600.png?text=EchoTune+Music+Recommender"/> -->

---

# 🌍 Deployment

This application is deployed on Render.

Deployment command:

```bash
python -m streamlit run app.py --server.port $PORT --server.address 0.0.0.0
```

---

# 📌 Future Improvements

* Spotify API integration
* Album cover previews
* User authentication
* Personalized recommendations
* Audio preview support

---

# 👨‍💻 Author

**Gaurav Kumar**

* GitHub: https://github.com/mr-gaurav-kumar

---

# ⭐ Support

If you liked this project:

* Star the repository
* Share the project
* Give feedback

---
