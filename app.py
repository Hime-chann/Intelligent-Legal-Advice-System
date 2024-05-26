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
                        # Display the generated text
                        st.write(response)
                        
                        # Dummy extraction logic (You might need to parse the generated text properly)
                        # Assuming the response text includes lines like "Attorney Type: XYZ" and "Authority Level: ABC"
                        attorney_type = "Not specified"
                        authority_level = "Not specified"

                        if "Attorney Type:" in response:
                            attorney_type = response.split("Attorney Type:")[1].split("\n")[0].strip()

                        if "Authority Level:" in response:
                            authority_level = response.split("Authority Level:")[1].split("\n")[0].strip()

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
