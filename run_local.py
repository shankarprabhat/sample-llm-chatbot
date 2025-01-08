# from transformers import AutoModelForQuestionAnswering, AutoTokenizer
# from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline
# from transformers import pipeline
import requests
from pprint import pprint


call_pipeline = False
# model_name = "deepset/roberta-base-squad2"

if call_pipeline is True:
    model_name = "deepset/tinyroberta-squad2"

    # a) Get predictions
    # nlp = pipeline('question-answering', model=model_name, tokenizer=model_name)
    # QA_input = {
    #     'question': 'What is LLM?',
    #     'context': 'LLM provides the capability to understand languages.'
    # }
    # res = nlp(QA_input)
    # print(res['answer'])

call_inference_api = True

if call_inference_api is True:

    TOKEN = "Bearer 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"

    API_URL = 'https://api-inference.huggingface.co/models/deepset/roberta-base-squad2'
    headers = {"Authorization": TOKEN}

    # The Entertheaccesskeyhere is just a placeholder, which can be changed according to the user's access key
    def query(payload):
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.json()

    params = {'max_length': 200, 'top_k': 10, 'temperature': 2.5}
    output = query({'inputs': {"question": "What's my profession?","context": "My name is Suvojit and I am a Senior Data Scientist"},'parameters': params})
    # pprint(output)
    print(output[0]['answer'])
