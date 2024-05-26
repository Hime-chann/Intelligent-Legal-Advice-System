# prompts.py

def get_initial_prompt():
    return "Welcome! Would you like to get legal advice? (yes/no)"

def get_country_prompt():
    countries = [
        "USA", "Canada", "UK", "Australia", "Germany", "Philippines",
        "India", "China", "Japan", "France", "Brazil", "South Africa",
        "Russia", "Mexico", "Italy", "Spain", "Netherlands", "Sweden"
    ]
    return "Please select your country for legal advice:", countries

def get_age_prompt():
    return "Please enter your age."

def get_query_prompt():
    return "Please describe your legal query in detail."
