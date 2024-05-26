import google.generativeai as genai

# Directly set your API key here
api_key = "AIzaSyCSo2xaMpMmT10UhCRSWLiVZW3jlowiykw"
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
        print(f"Response: {response}")  # Debug print to check the response structure

        # Assuming the response object is a dictionary-like structure
        # Adjust the attribute names based on actual API response
        if 'generated_text' in response:
            return response['generated_text']
        elif hasattr(response, 'generated_text'):
            return response.generated_text
        else:
            return 'Unexpected response structure from the API'
    except Exception as e:
        return f'Error: {str(e)}'
