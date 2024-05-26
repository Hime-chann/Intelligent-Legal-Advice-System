# app.py

import streamlit as st
from gemini_api import generate_text
from prompts import get_initial_prompt, get_country_prompt, get_age_prompt, get_query_prompt

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
                generated_text = generate_text(final_prompt)
                
                if "Error" in generated_text:
                    st.error(generated_text)
                else:
                    # Extract attorney type and where to go from the generated text
                    st.write(generated_text)
                    st.write(f"Suggested Attorney Type: {attorney_type}")
                    st.write(f"Suggested Authority Level: {authority_level}")
else:
    st.write("Please enter 'Yes' to proceed with legal advice.")
