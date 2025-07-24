import os
import google.generativeai as genai
from PIL import Image
from dotenv import load_dotenv


load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def chat_with_text(prompt: str):
    model = genai.GenerativeModel("gemini-pro")
    chat = model.start_chat()
    response = chat.send_message(prompt)
    return response.text

def chat_with_image(image_path: str, prompt: str = "Describe this image"):
    model = genai.GenerativeModel("gemini-pro-vision")
    image = Image.open(image_path)
    response = model.generate_content([prompt, image])
    return response.text

if __name__ == "__main__":
    print("🧠 Text Response:")
    print(chat_with_text("Explain black holes in simple terms."))

    print("\n🖼️ Image Response:")
    print(chat_with_image("sample_inputs/sample_image.jpg", "What do you see?"))
