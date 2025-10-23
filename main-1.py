from google import genai
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("HATA: .env dosyasında GEMINI_API_KEY bulunamadı!")
    exit()

client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model= "gemini-2.5-flash",
    contents= "Fenerbahçe en son süperlig de hangi takım ile maç yaptı? şu anki tarih 21 ekim 2025"
)

print(response.text)

