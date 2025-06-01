

import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")
BASE_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent"

def generate_answer(prompt: str) -> str:
    headers = {
        "Content-Type": "application/json"
    }
    params = {
        "key": API_KEY
    }
    data = {
        "contents": [
            {
                "parts": [{"text": prompt}]
            }
        ]
    }
    response = requests.post(BASE_URL, headers=headers, params=params, json=data)
    
    if response.status_code == 200:
        try:
            return response.json()['candidates'][0]['content']['parts'][0]['text']
        except:
            return "[Error parsing response]"
    else:
        return f"[Error {response.status_code}]: {response.text}"
