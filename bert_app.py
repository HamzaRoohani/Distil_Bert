import streamlit as st
import requests

model_id = "distilbert-base-uncased-finetuned-sst-2-english"
token = "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"
API_URL = "https://api-inference.huggingface.co/models/distilbert/distilbert-base-uncased-finetuned-sst-2-english"

headers = {"Authorization": f"Bearer {token}"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()

st.title("Sentiment analysis")

text_input = st.text_input("Enter any text to predict sentiment analysis:")

if st.button("Analyze"):
	if text_input:
		data = {"inputs": text_input}
		response = query(data)
		
        # Display the output
		if 'error' not in response:
			st.write(response)
		else:
			st.write("Error in API request")
	else:
		st.write("Please enter some text to analyze!")