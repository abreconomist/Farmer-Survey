
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Farmers' Survey", layout="wide")

st.title("📋 Farmers' Survey Questionnaire")
st.markdown("### Improving Agricultural Income through a Package of Climate Smart Practices")

# SECTION 1
st.header("Section 1: General Information")
with st.form("general_info"):
    col1, col2 = st.columns(2)
    name = col1.text_input("Name")
    father_name = col2.text_input("Father Name")
    contact = col1.text_input("Contact Number")
    age = col2.number_input("Age (years)", 10, 100)
    education = col1.text_input("Education (highest year or degree completed)")
    experience = col2.number_input("Farming Experience (years)", 0, 100)
    submitted1 = st.form_submit_button("Save Section 1")

# SECTION 2
st.header("Section 2: Farm Size and Boundaries")

st.markdown("### Land Ownership & Operation Table")
farm_data = pd.DataFrame({
    "Type": [
        "Own Operational", "Area Rented to", "Area Rented by",
        "Share crop to", "Share crop by", "Family Cultivating Land"
    ],
    "Area Acres": [""]*6,
    "Mauza Name": [""]*6,
    "Khewat No": [""]*6,
    "Marabah No.": [""]*6,
    "Khasra No": [""]*6
})

edited_farm_data = st.data_editor(farm_data, num_rows="dynamic")

farm_boundary = st.radio("Do you have clearly defined farm boundaries?", ["Yes", "No"])

# SECTION 3
st.header("Section 3: Communication and Networking")
smartphone = st.radio("Do you own a smartphone?", ["Yes", "No"])
whatsapp = st.radio("Do you have WhatsApp in your phone?", ["Yes", "No"])
if whatsapp == "Yes":
    uses_whatsapp = st.radio("Do you use WhatsApp for farming-related discussions?", ["Yes", "No"])

relatives_nearby = st.radio("Do you have close relatives farming within or nearby Mauza?", ["Yes", "No"])
if relatives_nearby == "Yes":
    st.markdown("### Relatives Farming Nearby")
    relatives_data = pd.DataFrame({
        "Name of Relative": [""],
        "Relationship": [""],
        "Mauza Name": [""],
        "Khewat No": [""],
        "Marabah No": [""],
        "Khasra No": [""]
    })
    st.data_editor(relatives_data, num_rows="dynamic")

caste = st.text_input("What is your caste/baradari?")
num_families = st.number_input("How many families with same caste/baradari?", min_value=0)

st.markdown("### Caste Families Details")
caste_families_data = pd.DataFrame({
    "Name of Relative": [""],
    "Relationship": [""],
    "Mauza Name": [""],
    "Khewat No": [""],
    "Marabah No": [""],
    "Khasra No": [""]
})
st.data_editor(caste_families_data, num_rows="dynamic")

bethak = st.radio("Do you spend free time with the other farmers of the area (Bethak or Dera)?", ["Yes", "No"])
if bethak == "Yes":
    location = st.text_input("If yes, where (Mauza/Khasra/Khewat/Marabah Number)")
    friend = st.text_input("Farmer Name/Caste you spend time with")

# SECTION 4
st.header("Section 4: Farming Information Sources")
sources = st.multiselect("What are your primary sources of farming information?", [
    "Agriculture Extension", "Other Farmers of this Area", "Other Farmers of Different Area",
    "Internet", "Facebook", "YouTube", "WhatsApp group", "SMS service", "Mobile Application", "Other"
])
if "Other" in sources:
    other_source = st.text_input("Specify other source")

# SECTION 5
st.header("Section 5: Water Source")
canal = st.slider("Canal (%)", 0, 100)
tubewell = st.slider("Tubewell (%)", 0, 100)
rainfed = st.slider("Rainfed (%)", 0, 100)
other_water = st.slider("Other (%)", 0, 100)

canal_type = st.radio("Canal type:", ["Perennial Canals", "Non-Perennial Canals"])
tubewell_energy = st.radio("Source of Tubewell energy", ["Diesel", "Electric", "Solar"])

# SECTION 6
st.header("Section 6: Yield (last 2 years)")
yield_data = pd.DataFrame({
    "Crop": [""],
    "Season": ["Rabi"],
    "Last Year - Area": [""],
    "Last Year - Yield (Mund/Acre)": [""],
    "Year Before - Area": [""],
    "Year Before - Yield (Mund/Acre)": [""]
})
st.data_editor(yield_data, num_rows="dynamic")

# SECTION 7
st.header("Section 7: Climate-Smart Agriculture (CSA) Technologies")

heard_tech = st.multiselect("Have you heard of the following technologies?", [
    "Precision Land Leveling", "Drip and Sprinkler Irrigation Systems",
    "Climate-Resilient Crop Varieties", "Conservation Agriculture", "Intercropping"
])

used_tech = st.multiselect("Have you used any of these technologies?", [
    "Precision Land Leveling", "Drip and Sprinkler Irrigation Systems",
    "Climate-Resilient Crop Varieties", "Conservation Agriculture", "Intercropping"
])

# Submit Button
st.markdown("## ✅ Submit Survey")
if st.button("Submit All Responses"):
    st.success("Survey submitted successfully! (Note: Save functionality not yet connected to backend)")
