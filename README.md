# 🎬 Movie Sentiment Analysis (Flask + Logistic Regression)

A simple web app that predicts whether a movie review is **Positive** or **Negative**.  
Built with **Python, scikit-learn, Flask**, and a **Logistic Regression** model.
---
##  Tools & Tech

Python 3.10+

Flask (web framework)

scikit-learn (Logistic Regression + TF-IDF)

Pickle (for saving the model)
---
---

## 🚀 Features
- Logistic Regression model trained on IMDB-style reviews  
- REST API endpoint (`/api/predict`) for predictions  
- Web interface (HTML + Bootstrap) for easy use  
- Input a review → get prediction in real-time  

---

## 📂 Project Structure
MovieSent/
├─ app.py # Flask backend
├─ models/
│ └─ logreg_model.pkl # trained Logistic Regression model
├─ frontend/
│ └─ index.html # simple web interface
├─ requirements.txt # dependencies


---

## 🛠️ Installation & Setup

1. Clone this repo:
   ```bash
   git clone https://github.com/your-username/MovieSent.git
   cd MovieSent
   
## Create & activate a virtual environment:

python -m venv tf-env
tf-env\Scripts\activate     # Windows
source tf-env/bin/activate  # Mac/Linu

## install dependencies:

pip install -r requirements.txt


## Run the Flask app:

flask run --port 5000

## 🌐 Usage

Open in your browser: http://127.0.0.1:5000

Enter a movie review in the text box

Click Predict → see result (Positive / Negative)

## 📡 REST API Example

Endpoint:
POST /api/predict

## Future Improvements

Add LSTM (Deep Learning) model for comparison

Deploy on Hugging Face Spaces / Render / Heroku

Add user authentication & review history
