
import streamlit as st
import json

# Questionnaire data (parsed JSON embedded directly)
questionnaire_data = {
    "Sections": [
        {
            "title": "Section 1: General Information (This must be the farmer’s information)",
            "questions": [
                "Name:",
                "Father Name:",
                "Contact Number:",
                "Age: ____ (years)",
                "Education (highest year or degree completed):",
                "Farming Experience: _______ (Years)"
            ]
        },
        {
            "title": "Section 2: Farm Size and Boundaries.",
            "questions": [
                "Do you have clearly defined farm boundaries? (Yes / No)"
            ]
        },
        {
            "title": "Section 3: Communication and Networking",
            "questions": [
                "Do you own a smartphone? (Yes / No)",
                "Do you have WhatsApp in your phone? (Yes / No)",
                "If yes, do you use WhatsApp for farming-related discussions? (Yes / No)",
                "Do you have close relatives farming within or nearby Mauza? (Yes / No)",
                "What is your caste/ baradari:",
                "How many families having the same caste/baradari in the area:",
                "Do you spend free time with the other farmers of the area (Bethak or Dera)? (Yes / No)",
                "If yes, where (Mauza/Khasra/ Khewat/ Marabah Number):",
                "Farmer Name/Caste whom you spend time with:"
            ]
        },
        {
            "title": "Section 4: Farming Information Sources",
            "questions": [
                "What are your primary sources of farming information?"
            ]
        },
        {
            "title": "Section 5: Water Source",
            "questions": [
                "Primary source of irrigation water (in percentage): Canal",
                "Primary source of irrigation water (in percentage): Tubewell",
                "Primary source of irrigation water (in percentage): Rainfed",
                "Primary source of irrigation water (in percentage): Other",
                "Canal type: Perennial / Non-Perennial",
                "Source of Tubewell energy: Diesel / Electric / Solar"
            ]
        },
        {
            "title": "Section 6: Yield",
            "questions": [
                "What is your average yield per acre for your crop (last 2 years)?"
            ]
        },
        {
            "title": "Section 7: Knowledge and Adoption of CSA Technologies",
            "questions": [
                "Have you heard of CSA technologies? (Select all that apply)",
                "Have you used any CSA technologies? (Select all that apply)"
            ]
        }
    ]
}

st.title("Farmers' Survey Questionnaire")

responses = {}

for section in questionnaire_data["Sections"]:
    st.header(section["title"])
    for q in section["questions"]:
        response = st.text_input(q)
        responses[q] = response

if st.button("Submit"):
    with open("responses.json", "w", encoding="utf-8") as f:
        json.dump(responses, f, ensure_ascii=False, indent=4)
    st.success("Responses saved successfully!")
