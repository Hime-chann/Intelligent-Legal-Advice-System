# gemini_api.py

import google.generativeai as genai
import os

# Setup your API key
api_key = os.getenv('AIzaSyCSo2xaMpMmT10UhCRSWLiVZW3jlowiykw')


genai.configure(api_key=api_key)

def generate_text(prompt, max_tokens=150):
    try:
        response = genai.generate_text(
            prompt=prompt,
            max_output_tokens=max_tokens
        )
        return response['generated_text']
    except Exception as e:
        return f'Error: {str(e)}'
