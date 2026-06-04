from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

client = genai.Client(api_key=api_key)

models = client.models.list()

print("\n🔥 Available Gemini Models:\n")

for m in models:
    print(m.name)