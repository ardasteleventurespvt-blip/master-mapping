import streamlit as st
import pandas as pd

# Page title aur layout set karein
st.set_page_config(page_title="Affordability Mapping - Ardas Tele Ventures", layout="wide")

# Company Header & Branding
st.markdown("<h3 style='text-align: center; color: #1E3A8A;'>Ardas Tele Ventures Pvt. Ltd.</h3>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center;'>Affordability Mapping</h1>", unsafe_allow_html=True)
st.write("---")

# Mapping option select karne ke liye list
options = [
    "BAJAJ",
    "PAYTM",
    "HDFC",
    "HDB",
    "TVS",
    "ICICI",
    "IDFC",
    "PINELAB"
]

# Dropdown selection (Selectbox)
selected_partner = st.selectbox(
    "📌 Select Partner / Entity for Affordability Mapping:",
    options,
    index=0
)

st.subheader(f"📊 Selected Mapping: {selected_partner}")

# Sample Data (Aap isko apne actual database / CSV se replace kar sakte hain)
data = {
    "Location ID": ["LOC001", "LOC002", "LOC003", "LOC004"],
    "City/Location Name": ["Delhi", "Mumbai", "Bangalore", "Jaipur"],
    "Partner Name": [selected_partner] * 4,
    "Mapping Person/Team": ["Ramesh Kumar", "Suresh Sharma", "Priya Singh", "Amit Patel"],
    "Status": ["Active", "Active", "Pending", "Active"]
}

df = pd.DataFrame(data)

# Search bar location filter karne ke liye
search = st.text_input("🔍 Location ya Name se search karein:")

if search:
    filtered_df = df[df.apply(lambda row: row.astype(str).str.contains(search, case=False).any(), axis=1)]
    st.dataframe(filtered_df, use_container_width=True)
else:
    st.dataframe(df, use_container_width=True)

# File download button (Excel ya CSV download ke liye)
csv = df.to_csv(index=False).encode('utf-8')
st.download_button(
    label=f"📥 Download {selected_partner} Mapping Data (CSV)",
    data=csv,
    file_name=f'{selected_partner.lower()}_affordability_mapping.csv',
    mime='text/csv',
)
