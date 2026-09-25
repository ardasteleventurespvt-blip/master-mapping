%%writefile app.py
import streamlit as st
import pandas as pd

# Page title aur layout set karein
st.set_page_config(page_title="Master Mapping Data", layout="wide")

st.title("📍 Master Mapping Data")
st.write("Is page par alag-alag locations ki mapping sheet ka data available hai.")

# Sample Data (Yahan aap apna real data daal sakte hain ya Excel/CSV upload ka code laga sakte hain)
data = {
    "Location ID": ["LOC001", "LOC002", "LOC003", "LOC004"],
    "City/Location Name": ["Delhi", "Mumbai", "Bangalore", "Jaipur"],
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
    label="📥 Download Mapping Data (CSV)",
    data=csv,
    file_name='master_mapping_data.csv',
    mime='text/csv',
)