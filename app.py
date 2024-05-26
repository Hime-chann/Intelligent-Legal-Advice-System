import streamlit as st
from gemini_api import generate_text
from prompts import get_initial_prompt, get_country_prompt, get_age_prompt, get_query_prompt

def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Legal Advice", "README"])

    if page == "Legal Advice":
        legal_advice_page()
    elif page == "README":
        readme_page()

def legal_advice_page():
    st.title("Intelligent Legal Advice System")

    # Initial Prompt
    initial_prompt = get_initial_prompt()
    user_choice = st.text_input(initial_prompt)

    if user_choice.lower() == 'yes':
        country_prompt, countries = get_country_prompt()
        country_choice = st.selectbox(country_prompt, countries)
        
        if country_choice:
            age_prompt = get_age_prompt()
            age = st.text_input(age_prompt)
            
            if age:
                query_prompt = get_query_prompt()
                legal_query = st.text_area(query_prompt)
                
                if legal_query:
                    final_prompt = f"Country: {country_choice}, Age: {age}, Query: {legal_query}"
                    st.write("Generating your legal advice...")
                    response = generate_text(final_prompt)
                    
                    if isinstance(response, str) and response.startswith("Error"):
                        st.error(response)
                    else:
                        # Display the full API response
                        st.write("API Response:")
                        st.write(response)
                        
                        # Extract information based on actual response structure
                        attorney_type = "Not specified"
                        authority_level = "Not specified"

                        # Example of parsing a string response
                        if isinstance(response, str):
                            # Extract attorney type if mentioned in the response
                            if "attorney" in response.lower():
                                attorney_type = "Lawyer"
                            
                            # Extract authority level if mentioned in the response
                            if "authority" in response.lower():
                                authority_level = "Varies"
                        elif isinstance(response, dict) and 'generated_text' in response:
                            generated_text = response['generated_text']
                            # Extract attorney type if mentioned in the generated text
                            if "attorney" in generated_text.lower():
                                attorney_type = "Lawyer"
                            
                            # Extract authority level if mentioned in the generated text
                            if "authority" in generated_text.lower():
                                authority_level = "Varies"

                        st.write(f"Suggested Attorney Type: {attorney_type}")
                        st.write(f"Suggested Authority Level: {authority_level}")
    else:
        st.write("Please enter 'Yes' to proceed with legal advice.")

def readme_page():
    st.title("README.md")
    with open("README.md", "r") as file:
        readme_content = file.read()
    st.markdown(readme_content)

if __name__ == "__main__":
    main()
