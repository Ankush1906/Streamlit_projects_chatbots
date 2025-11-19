import streamlit as st
import requests
import json

API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"

def summarize_text(text):
    payload = {"inputs": text}
    response = requests.post(API_URL, json=payload)
    return response.json()[0]['summary_text']

st.title("Text Summarizer (API – No API Key Needed)")
st.write("Uses HuggingFace free public inference API.")

user_input = st.text_area("Enter text to summarize:", height=300)

if st.button("Summarize"):
    if user_input.strip():
        with st.spinner("Summarizing... Please wait..."):
            try:
                summary = summarize_text(user_input)
                st.subheader("Summary")
                st.write(summary)
            except:
                st.error("The free API is busy. Try again after a few seconds.")
    else:
        st.warning("Please enter some text.")
