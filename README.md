
# VerifAI - AI Fake News Analyzer

VerifAI is an AI-powered fake news detection and fact-checking web application that analyzes user-provided claims and generates a verdict with confidence score and reasoning.

The project uses Google's Gemini AI model to analyze information and classify it as **REAL, FAKE, MISLEADING, or UNVERIFIED**.

---

## 🚀 Features

- AI-powered claim analysis
- Fake news detection
- Verdict classification
- Confidence score generation
- AI reasoning explanation
- Clean and simple user interface
- Real-time analysis using Gemini API

---

## 🛠️ Tech Stack

### Frontend
- HTML
- CSS
- JavaScript

### Backend
- Python
- Flask
- Flask-CORS

### AI Model
- Google Gemini API

---

## 📂 Project Structure

    VerifAI/
    |
    |-- index.html
    |
    |-- backend/
    |   |-- app.py
    |   |-- requirements.txt
    |   |-- .env
    |
    |-- .gitignore


---

## ⚙️ Installation & Setup

### 1. Clone the repository

    git clone YOUR_REPOSITORY_URL

Move into the project:

    cd VerifAI


---

## Backend Setup

Go inside backend:

    cd backend

Install dependencies:

    pip install -r requirements.txt


---

## 🔑 API Key Setup

Create a file:

    backend/.env

Add your Gemini API key:

    GEMINI_API_KEY=your_api_key_here

Get your API key from:

Google AI Studio:
https://aistudio.google.com/app/apikey


---

## ▶️ Run the Backend

Start Flask server:

    python app.py

The backend will run on:

    http://127.0.0.1:5000


---

## 🌐 Run Frontend

Open:

    index.html

in your browser.

Enter a claim and click Check Now.

Example:

    The Earth is flat

The AI will return:

- Verdict
- Confidence score
- Reasoning


---

## 🔍 How It Works


    User Input
         |
         ↓
    Frontend (HTML/CSS/JS)
         |
         ↓
    Flask Backend
         |
         ↓
    Gemini AI API
         |
         ↓
    Fact Checking Response
         |
         ↓
    Result Display


---

## 📌 Example Output

    Verdict:
    FAKE

    Confidence:
    95%

    Reasoning:

    • Scientific evidence proves Earth is spherical
    • Satellite images confirm Earth's shape
    • Multiple experiments support this conclusion


---

## 🔒 Security

API keys are stored using environment variables.

The .env file is excluded from GitHub using:

    .gitignore


---

## 👨‍💻 Author

Pinapaka Shanmukhi


---

## ⭐ If you like this project

Give it a star on GitHub!
