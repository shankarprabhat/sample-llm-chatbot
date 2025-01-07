# Flask application for the chatbot
from flask import Flask, request, jsonify
from transformers import pipeline
from flask_cors import CORS
import os

os.environ["TRANSFORMERS_CACHE"] = "/tmp"

print("Is /tmp writable?", os.access("/tmp", os.W_OK))

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
# CORS(app, resources={r"/chat": {"origins": "http://localhost:3000"}}) # Enable CORS for /chat route

# Load the LLM model (adjust as needed)
# chatbot = pipeline("conversational", model="gpt-2")
# big_model = "deepset/roberta-base-squad2"
# small_model = "deepset/tinyroberta-squad2"
# chatbot = pipeline("question-answering", model=small_model)

@app.route("/chat", methods=["POST"])
def chat():
    # print('Request:', request.json)
    # user_input = request.json.get("message")
    
    # QA_input = {
    # "question": user_input,
    # "context": "LLM provides the capability to understand languages."
    # }
    # response = chatbot(QA_input)
    # return jsonify({"response": response['answer']})

    import requests
    # from pprint import pprint

    TOKEN = "Bearer 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"

    API_URL = 'https://api-inference.huggingface.co/models/deepset/roberta-base-squad2'
    headers = {"Authorization": TOKEN}

    print('Request:', request.json)
    user_input = request.json.get("message")
    print("Transformers cache directory:", os.environ.get("TRANSFORMERS_CACHE"))

    # The Entertheaccesskeyhere is just a placeholder, which can be changed according to the user's access key
    def query(payload):
        response = requests.post(API_URL, headers=headers, json=payload)
        response.raise_for_status()  # Raise exception for HTTP errors
        return response.json()

    params = {'max_length': 200, 'top_k': 10, 'temperature': 2.5}
    output = query({'inputs': {"question": user_input,"context": "My name is Suvojit and I am a Senior Data Scientist"},'parameters': params})
    # pprint('output',output)
    return jsonify({"response": output[0]['answer']})

if __name__ == "__main__":
    app.run(debug=True)
