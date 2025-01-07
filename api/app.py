# Flask application for the chatbot
from flask import Flask, request, jsonify
from transformers import pipeline
from flask_cors import CORS
import os

os.environ["TRANSFORMERS_CACHE"] = "/tmp"

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
# CORS(app, resources={r"/chat": {"origins": "http://localhost:3000"}}) # Enable CORS for /chat route

# Load the LLM model (adjust as needed)
# chatbot = pipeline("conversational", model="gpt-2")
big_model = "deepset/roberta-base-squad2"
small_model = "deepset/tinyroberta-squad2"
chatbot = pipeline("question-answering", model=small_model)

@app.route("/chat", methods=["POST"])
def chat():
    print('Request:', request.json)
    user_input = request.json.get("message")
    
    QA_input = {
    "question": user_input,
    "context": "LLM provides the capability to understand languages."
    }
    response = chatbot(QA_input)
    return jsonify({"response": response['answer']})

if __name__ == "__main__":
    app.run(debug=True)
