import google.generativeai as genai
import os

# Setup your API key
api_key = "AIzaSyCSo2xaMpMmT10UhCRSWLiVZW3jlowiykw"
if not api_key:
    raise ValueError("API key not found. Please set the GOOGLE_API_KEY environment variable.")
else:
    print(f"API Key: {api_key}")  # Debug print to check API key

genai.configure(api_key=api_key)

def generate_text(prompt, max_tokens=300):
    try:
        response = genai.generate_text(
            prompt=prompt,
            max_output_tokens=max_tokens
        )
        print(f"Response Type: {type(response)}")  # Print the type of the response object
        print(f"Response Dir: {dir(response)}")    # Print all attributes and methods of the response object
        print(f"Response: {response}")  # Print the full response object
        
        # Check the attributes of the response object
        if hasattr(response, '__dict__'):
            print(f"Response Attributes: {response.__dict__}")

        # Extract the generated text from the response
        if response.candidates and len(response.candidates) > 0:
            generated_text = response.candidates[0]['output']
            return generated_text
        else:
            return 'No generated text found in the response'
    except Exception as e:
        return f'Error: {str(e)}'
