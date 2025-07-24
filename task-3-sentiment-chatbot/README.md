
# Task 3: Sentiment-Aware Chatbot

## Description
This chatbot uses sentiment analysis to detect the emotional tone of the user's input and responds accordingly. It supports:
- Text sentiment detection (positive, negative, neutral)
- Friendly replies based on emotion
- Streamlit GUI

## Files
- `task3_sentiment_chatbot.ipynb`: Jupyter notebook with sentiment chatbot logic
- `streamlit_gui.py`: GUI implementation with Streamlit
- `requirements.txt`: Dependencies
- `README.md`: Project overview

## Accuracy Claim
The model is based on `TextBlob` which provides ~70-75% sentiment classification accuracy on basic English statements.

## Run Instructions

```bash
pip install -r requirements.txt
streamlit run streamlit_gui.py
```

## Notes
No training was required since this task uses a rule-based sentiment engine (TextBlob).
