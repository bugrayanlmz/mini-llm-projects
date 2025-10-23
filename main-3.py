from google import genai
import os
from dotenv import load_dotenv
import sys

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("Api key bulunamadı. Lütfen kontrol edin")
    exit()

client = genai.Client(api_key= api_key)

chat = client.chats.create(
    model= "gemini-2.5-flash"
)

while True:
    user_input= input("\nBir şeyler yazın:")

    if user_input.lower() in ["quit", "exit", "çık"]:
        print("Görüşürüz sg")
        break

    if not user_input.strip():
        continue

    try:
        response_stream = chat.send_message_stream(
            user_input
        )

        for chunk in response_stream:

            if chunk.text:
                print(chunk.text, end="", flush=True)


    
    except Exception as e:
        print(f"Hata {e}")