from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai
from dotenv import load_dotenv
import os
import json


app = Flask(__name__)
CORS(app)


load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise Exception("GEMINI_API_KEY not found")


genai.configure(
    api_key=api_key
)


model = genai.GenerativeModel("gemini-2.5-flash")


@app.route("/")
def home():
    return "VerifAI Backend Running"


@app.route("/check", methods=["POST"])
def check():

    try:

        data = request.json
        claim = data["content"]


        prompt = f"""

You are a professional fact checker.

Analyze this claim:

{claim}


IMPORTANT:
- Return ONLY JSON
- No markdown
- No explanation outside JSON
- reasoning MUST be an array of short bullet points
- Each reasoning point must be a separate string


Return exactly this format:

{{
"verdict":"REAL",
"confidence":90,
"claim_summary":"short summary",
"reasoning":[
"First reason",
"Second reason",
"Third reason"
],
"sources":[]
}}

"""


        response = model.generate_content(prompt)


        text = response.text.strip()


        # remove markdown if Gemini adds it
        text = text.replace("```json", "")
        text = text.replace("```", "")


        result = json.loads(text)


        return jsonify(result)


    except Exception as e:

        print("ERROR:", e)

        return jsonify({
            "error": str(e)
        }), 500



app.run(
    host="127.0.0.1",
    port=5000
)
