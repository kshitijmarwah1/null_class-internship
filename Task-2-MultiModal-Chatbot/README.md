# Task 2: Multi-Modal Chatbot using Gemini AI

## Overview
This chatbot can:
- Handle **text input** and generate responses using Gemini Pro.
- Handle **image input** using Gemini Vision (describe or answer based on image).

## Files
- `multi_modal_chatbot.py`: Core logic for Gemini API.
- `streamlit_gui.py`: Streamlit GUI for interaction.
- `task2_demo.ipynb`: Notebook version.
- `requirements.txt`: Dependencies.
- `.env`: Stores API key. 
- `sample_inputs/sample_image.jpg`: Sample image for testing.

## Setup
1.  Install requirements:
    ```bash
    pip install -r requirements.txt
    ```
2.  Add your API key to a `.env` file. **Never commit this file to your repository.**
    ```
    GOOGLE_API_KEY="YOUR_API_KEY_HERE"
    ```

## Launch Streamlit UI
```bash
streamlit run streamlit_gui.py