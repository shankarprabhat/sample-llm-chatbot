from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline

# model_name = "deepset/roberta-base-squad2"
model_name = "deepset/tinyroberta-squad2"

# a) Get predictions
nlp = pipeline('question-answering', model=model_name, tokenizer=model_name)
QA_input = {
    'question': 'What is LLM?',
    'context': 'LLM provides the capability to understand languages.'
}
res = nlp(QA_input)
print(res['answer'])
