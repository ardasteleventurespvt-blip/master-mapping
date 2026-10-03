import streamlit as st
import pandas as pd

# Page title aur layout set karein
st.set_page_config(page_title="Affordability Mapping - Ardas Tele Ventures", layout="wide")

# Company Header & Branding
st.markdown("<h3 style='text-align: center; color: #1E3A8A;'>Ardas Tele Ventures Pvt. Ltd.</h3>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center;'>Affordability Mapping Form</h1>", unsafe_allow_html=True)
st.write("---")

# Session state initialization for data storage
if "mapping_records" not in st.session_state:
    st.session_state.mapping_records = []

# Mapping options
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

st.subheader(f"📝 Fill Affordability Mapping Form for: {selected_partner}")

# Rajasthan Cities List
rajasthan_cities = [
    "Ajmer", "Alwar", "Anupgarh", "Balotra", "Banswara", "Baran", "Barmer", "Beawar",
    "Bharatpur", "Bhilwara", "Bikaner", "Bundi", "Chittorgarh", "Churu", "Dausa",
    "Deeg", "Didwana-Kuchaman", "Dholpur", "Dungarpur", "Ganganagar", "Gangapur City",
    "Hanumangarh", "Jaipur", "Jaipur Rural", "Jaisalmer", "Jalore", "Jhalawar",
    "Jhunjhunu", "Jodhpur", "Jodhpur Rural", "Karauli", "Kekri", "Kota", "Kotputli-Behror",
    "Khairthal-Tijara", "Nagaur", "Neem Ka Thana", "Pali", "Phalodi", "Pratapgarh",
    "Rajsamand", "Salumbar", "Sanchore", "Sawai Madhopur", "Shahpura", "Sikar", "Sirohi",
    "Tonk", "Udaipur", "Other"
]

# Form definition
with st.form(key="mapping_form", clear_on_submit=True):
    col1, col2 = st.columns(2)
    
    with col1:
        apple_id = st.text_input("Apple ID *")
        store_name = st.text_input("Store Name *")
        address = st.text_area("Address *")
        
        selected_city = st.selectbox("City (Rajasthan) *", rajasthan_cities)
        
        # Other City Input if "Other" selected
        if selected_city == "Other":
            custom_city = st.text_input("Enter City Name *")
            city = custom_city
        else:
            city = selected_city

        area = st.text_input("Area *")

    with col2:
        pincode = st.text_input("Pincode *")
        contact_person = st.text_input("Contact Person *")
        contact_number = st.text_input("Contact Number *")
        email_id = st.text_input("Email ID *")
        
        # Company specific ID field
        if selected_partner == "BAJAJ":
            mapping_code = st.text_input("BFL ID / Bajaj Mapping Code *")
        else:
            mapping_code = st.text_input(f"{selected_partner} Mapping Code / ID *")

    submit_button = st.form_submit_button(label="Submit Mapping Data")

# Form submission logic
if submit_button:
    if not (apple_id and store_name and address and city and area and pincode and contact_person and contact_number and email_id and mapping_code):
        st.error("⚠️ Please fill all required mandatory fields (*).")
    else:
        new_record = {
            "Partner": selected_partner,
            "Apple ID": apple_id,
            "Store Name": store_name,
            "Address": address,
            "City": city,
            "Area": area,
            "Pincode": pincode,
            "Contact Person": contact_person,
            "Contact Number": contact_number,
            "Email ID": email_id,
            "Mapping Code/ID": mapping_code
        }
        st.session_state.mapping_records.append(new_record)
        st.success(f"✅ Mapping data for {selected_partner} successfully saved!")

# Display Data Table
st.write("---")
st.subheader("📊 Submitted Mapping Records")

if st.session_state.mapping_records:
    df_records = pd.DataFrame(st.session_state.mapping_records)
    
    # Filter by selected partner
    filtered_df = df_records[df_records["Partner"] == selected_partner]
    
    st.dataframe(filtered_df, use_container_width=True)
    
    # CSV Download Button
    csv = filtered_df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label=f"📥 Download {selected_partner} Mapping Data (CSV)",
        data=csv,
        file_name=f'{selected_partner.lower()}_affordability_mapping.csv',
        mime='text/csv',
    )
else:
    st.info("No records submitted yet. Fill out the form above to add data.")
