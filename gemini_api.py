import google.generativeai as genai
import os

# Setup your API key
api_key = os.getenv('GOOGLE_API_KEY')
if not api_key:
    raise ValueError("API key not found. Please set the GOOGLE_API_KEY environment variable.")
else:
    print(f"API Key: {api_key}")  # Debug print to check API key

genai.configure(api_key=api_key)

def generate_text(prompt, max_tokens=150):
    try:
        response = genai.generate_text(
            prompt=prompt,
            max_output_tokens=max_tokens
        )
        print(f"Response: {response}")  # Debug print to check the response
        if hasattr(response, 'generated_text'):
            return response.generated_text
        else:
            return 'Unexpected response structure from the API'
    except Exception as e:
        return f'Error: {str(e)}'
