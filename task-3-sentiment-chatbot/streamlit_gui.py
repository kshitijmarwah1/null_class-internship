
import streamlit as st
from textblob import TextBlob

st.title("Sentiment-Aware Chatbot")

user_input = st.text_input("You:", "")

def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0:
        return "positive"
    elif polarity < 0:
        return "negative"
    else:
        return "neutral"

def generate_response(user_input):
    sentiment = analyze_sentiment(user_input)
    if sentiment == "positive":
        return "😊 I'm glad to hear that!"
    elif sentiment == "negative":
        return "😔 I'm sorry to hear that. Is there anything I can do to help?"
    else:
        return "🤔 Got it! Let me know if you'd like to talk more."

if user_input:
    st.write("Chatbot:", generate_response(user_input))
