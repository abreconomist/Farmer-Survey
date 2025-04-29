
import streamlit as st
import json

# Load the questionnaire data
with open("parsed_questionnaire.json", "r", encoding="utf-8") as f:
    data = json.load(f)

st.title("Farmers' Survey Questionnaire")

responses = {}

for section in data["Sections"]:
    st.header(section["title"])
    for q in section["questions"]:
        response = st.text_input(q)
        responses[q] = response

# Save responses
if st.button("Submit"):
    with open("responses.json", "w", encoding="utf-8") as f:
        json.dump(responses, f, ensure_ascii=False, indent=4)
    st.success("Responses saved successfully!")
