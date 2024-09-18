import transformers
import torch
import requests


model_id = "distilbert-base-uncased-finetuned-sst-2-english"
token = "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"
API_URL = "https://api-inference.huggingface.co/models/distilbert/distilbert-base-uncased-finetuned-sst-2-english"

headers = {"Authorization": f"Bearer {token}"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()

text_input = input("Enter any text: ")

payload = {"inputs": text_input}

response = query(payload)

print(f"Sentiment analysis result: {response}")