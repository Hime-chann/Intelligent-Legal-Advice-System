# app.py

import streamlit as st
from gemini_api import generate_text
from prompts import get_initial_prompt, get_country_prompt, get_age_prompt, get_attorney_type_prompt, get_authority_level_prompt, get_query_prompt

st.title("Intelligent Legal Advice System")

# Initial Prompt
initial_prompt = get_initial_prompt()
user_choice = st.text_input(initial_prompt)

if user_choice.lower() == 'yes':
    country_prompt = get_country_prompt()
    country_choice = st.text_input(country_prompt)
    
    if country_choice:
        age_prompt = get_age_prompt()
        age = st.text_input(age_prompt)
        
        if age:
            attorney_type_prompt = get_attorney_type_prompt()
            attorney_type = st.text_input(attorney_type_prompt)
            
            if attorney_type:
                authority_level_prompt = get_authority_level_prompt()
                authority_level = st.text_input(authority_level_prompt)
                
                if authority_level:
                    query_prompt = get_query_prompt()
                    legal_query = st.text_area(query_prompt)
                    
                    if legal_query:
                        final_prompt = f"Country: {country_choice}, Age: {age}, Attorney Type: {attorney_type}, Authority Level: {authority_level}, Query: {legal_query}"
                        st.write("Generating your legal advice...")
                        generated_text = generate_text(final_prompt)
                        st.write(generated_text)
else:
    st.write("Please enter 'Yes' to proceed with legal advice.")
