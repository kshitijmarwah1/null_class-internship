import streamlit as st
from multi_modal_chatbot import chat_with_text, chat_with_image

st.title("🧠 Multi-Modal Chatbot (Gemini AI)")

option = st.radio("Choose Input Type", ["Text", "Image"])

if option == "Text":
    prompt = st.text_input("Enter your question:")
    if st.button("Send"):
        if prompt:
            with st.spinner("Thinking..."):
                response = chat_with_text(prompt)
                st.success(response)
        else:
            st.warning("Please enter a prompt!")

else:
    uploaded_file = st.file_uploader("Upload an Image", type=["png", "jpg", "jpeg"])
    prompt = st.text_input("Optional prompt for image:")
    if st.button("Send Image"):
        if uploaded_file:
            with st.spinner("Analyzing..."):
                with open("temp.jpg", "wb") as f:
                    f.write(uploaded_file.read())
                response = chat_with_image("temp.jpg", prompt or "Describe this image.")
                st.success(response)
        else:
            st.warning("Please upload an image!")
