
import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Farmers' Survey Questionnaire", layout="wide")
st.title("Farmers' Survey Questionnaire")
st.write("**Improving Agricultural Income through a Package of Climate Smart Practices**")
st.markdown("---")

responses = {}

# Section 1: General Information
st.header("Section 1: General Information")
responses["Name"] = st.text_input("Name")
responses["Father Name"] = st.text_input("Father Name")
responses["Contact Number"] = st.text_input("Contact Number")
responses["Age"] = st.number_input("Age", 10, 100, step=1)
responses["Education"] = st.text_input("Education (highest year or degree completed)")
responses["Farming Experience"] = st.number_input("Farming Experience (years)", 0, 100, step=1)

# Section 2: Farm Size and Boundaries
st.header("Section 2: Farm Size and Boundaries")
farm_data = st.data_editor(pd.DataFrame({
    "Type": ["Own Operational", "Area Rented to", "Area Rented by", "Share crop to", "Share crop by", "Family Cultivating Land"],
    "Area (Acres)": [0]*6,
    "Location (Mauza Name/Khewat No./Marabah No./ Khasra No)": [""]*6,
    "Ownership": [""]*6
}), num_rows="dynamic", use_container_width=True)
responses["Farm Data"] = farm_data.to_dict()

responses["Total Cultivated Area"] = st.number_input("Total Cultivated Area (ii+iv+vi+vii)", 0.0)
responses["Clearly defined farm boundaries"] = st.radio("Do you have clearly defined farm boundaries?", ["Yes", "No"])

# Section 3: Communication and Networking
st.header("Section 3: Communication and Networking")
responses["Own Smartphone"] = st.radio("Do you own a smartphone?", ["Yes", "No"])
responses["WhatsApp on Phone"] = st.radio("Do you have WhatsApp in your phone?", ["Yes", "No"])
responses["Use WhatsApp for Farming"] = st.radio("If yes, do you use WhatsApp for farming-related discussions?", ["Yes", "No"])
responses["Relatives Farming Nearby"] = st.radio("Do you have close relatives (brothers, cousins) farming within or nearby Mauza?", ["Yes", "No"])

if responses["Relatives Farming Nearby"] == "Yes":
    st.markdown("**Details of Relatives**")
    relative_data = st.data_editor(pd.DataFrame({
        "Name of Relative": [""],
        "Relationship": [""],
        "Mauza/ Khasra/Marabah/ Khewat": [""]
    }), num_rows="dynamic", use_container_width=True)
    responses["Relatives Info"] = relative_data.to_dict()

responses["Caste/Baradari"] = st.text_input("What is your caste/ baradari?")
responses["Families in Area (same caste/baradari)"] = st.number_input("How many families with same caste/baradari in the area?", 0)
responses["Visit Frequency"] = st.data_editor(pd.DataFrame({
    "Name of Relative": [""],
    "Relationship": [""],
    "Mauza/ Khasra/ Khewat/Marabah Number": [""],
    "Frequency of visit": [""]
}), num_rows="dynamic", use_container_width=True)

responses["Spend time with farmers (Bethak/Dera)"] = st.radio("Do you spend free time with the other farmers of the area?", ["Yes", "No"])
if responses["Spend time with farmers (Bethak/Dera)"] == "Yes":
    responses["Bethak Location"] = st.text_input("Where? (Mauza/Khasra/ Khewat/ Marabah Number)")
    responses["Farmer Name/Caste"] = st.text_input("Farmer Name/Caste whom you spend time with")

# Section 4: Farming Information Sources
st.header("Section 4: Farming Information Sources")
info_sources = st.multiselect("What are your primary sources of farming information? (Select all that apply)", [
    "Agriculture Extension", "Other Farmers of this Area", "Other Farmers of Different Area", "Internet", 
    "Facebook", "YouTube", "WhatsApp group", "SMS service", "Mobile Application", "Other"
])
responses["Farming Info Sources"] = info_sources
if "Other" in info_sources:
    responses["Other Info Source"] = st.text_input("Other source (specify)")

# Section 5: Water Source
st.header("Section 5: Water Source")
responses["Irrigation Water Source (%)"] = {
    "Canal": st.slider("Canal (%)", 0, 100),
    "Tubewell": st.slider("Tubewell (%)", 0, 100),
    "Rainfed": st.slider("Rainfed (%)", 0, 100),
    "Other": st.slider("Other (%)", 0, 100)
}
responses["Canal Type"] = st.radio("Canal type", ["Perennial Canals", "Non-Perennial Canals"])
responses["Tubewell Energy Source"] = st.multiselect("Source of Tubewell energy", ["Diesel", "Electric", "Solar"])

# Section 6: Yield
st.header("Section 6: Yield")
yield_data = st.data_editor(pd.DataFrame({
    "Crop": [""],
    "Season": ["Rabi", "Kharif"],
    "Last Year Area (Acres)": [0.0, 0.0],
    "Last Year Avg Yield (Mund/Acre)": [0.0, 0.0],
    "Year Before Area (Acres)": [0.0, 0.0],
    "Year Before Avg Yield (Mund/Acre)": [0.0, 0.0]
}), num_rows="dynamic", use_container_width=True)
responses["Yield Data"] = yield_data.to_dict()

# Section 7: Knowledge and Adoption of CSA Technologies
st.header("Section 7: Knowledge and Adoption of CSA Technologies")
techs = ["Precision Land Leveling", "Drip and Sprinkler Irrigation Systems", "Climate-Resilient Crop Varieties", 
         "Conservation Agriculture (Zero Tillage and Cover Cropping)", "Intercropping"]
responses["CSA Technologies Heard"] = st.multiselect("Have you heard of the following CSA technologies?", techs)
responses["CSA Technologies Used"] = st.multiselect("Have you used any of these on your farm?", techs)

# Submit
if st.button("Submit Survey"):
    df = pd.DataFrame([responses])
    df.to_csv("farmer_responses.csv", mode="a", index=False, header=False)
    st.success("Thank you! Your response has been recorded.")
