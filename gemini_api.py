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
        print(f"Full Response: {response}")  # Print the full response object
        print(f"Response Type: {type(response)}")  # Print the type of the response object

        # Check the attributes of the response object
        if hasattr(response, '__dict__'):
            print(f"Response Attributes: {response.__dict__}")

        # Attempt to access 'generated_text' attribute
        if hasattr(response, 'generated_text'):
            return response.generated_text
        elif isinstance(response, dict) and 'generated_text' in response:
            return response['generated_text']
        else:
            return 'Unexpected response structure from the API'
    except Exception as e:
        return f'Error: {str(e)}'
