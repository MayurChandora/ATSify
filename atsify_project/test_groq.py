import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv(".env")
api_key = os.environ.get("GROQ_API_KEY")
print("API KEY starts with:", api_key[:10] if api_key else "None")

client = Groq(api_key=api_key)

try:
    response = client.chat.completions.create(
        messages=[{"role": "user", "content": "Hello"}],
        model="llama3-8b-8192",
    )
    print("Success:", response.choices[0].message.content)
except Exception as e:
    print("Error:", e)
