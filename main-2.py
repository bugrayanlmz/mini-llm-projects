from google import genai
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("HATA: .env dosyasında GEMINI_API_KEY bulunamadı!")
    exit()

client = genai.Client(api_key= api_key)

chat = client.chats.create(
    model= "gemini-2.5-flash",
)

print("Hangi konuda yardımcı olmamı istersin?")

while True:
    user_input = input("Write something:")

    if user_input.lower() in ['quit', 'exit', 'çık', 'q']:
        print("\n Hoşça kal!")
        break

    if not user_input.strip():
        print("Bir şeyler girin")
        continue

    try:

        response = chat.send_message(user_input)

        print(f"Gemini: {response.text}")

    except Exception as e:
        print(f"Hata oluştu {e}")




