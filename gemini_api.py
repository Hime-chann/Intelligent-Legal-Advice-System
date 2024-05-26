# gemini_api.py

import requests

API_KEY = 'AIzaSyC_B3AKd4OWZjh-iIYEjdJ9t0xBKAvhqqg'
API_URL = 'https://aistudio.google.com/app/apikey'  # Hypothetical endpoint

def generate_text(prompt, max_tokens=150):
    headers = {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json'
    }
    data = {
        'prompt': prompt,
        'max_tokens': max_tokens
    }
    response = requests.post(API_URL, headers=headers, json=data)
    if response.status_code == 200:
        return response.json().get('text', '')
    else:
        return 'Error: Unable to fetch response from API'
