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

# Dynamic Form
with st.form(key=f"mapping_form_{selected_partner}", clear_on_submit=True):
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
        
        # Company-specific Dynamic Fields
        company_fields = {}
        
        if selected_partner == "BAJAJ":
            company_fields["BFL ID / Bajaj Mapping Code"] = st.text_input("BFL ID / Bajaj Mapping Code *")
            
        elif selected_partner == "PAYTM":
            company_fields["Paytm MID"] = st.text_input("Paytm MID (Merchant ID) *")
            company_fields["Paytm TID"] = st.text_input("Paytm TID *")
            
        elif selected_partner == "HDFC":
            company_fields["HDFC Vendor Code"] = st.text_input("HDFC Vendor Code *")
            
        elif selected_partner == "HDB":
            company_fields["HDB Mapping Code"] = st.text_input("HDB Mapping Code *")
            
        elif selected_partner == "TVS":
            company_fields["TVS Mapping Code"] = st.text_input("TVS Mapping Code *")
            
        elif selected_partner == "ICICI":
            company_fields["ICICI Dealer ID / Mapping Code"] = st.text_input("ICICI Dealer ID / Mapping Code *")
            
        elif selected_partner == "IDFC":
            company_fields["IDFC Store ID"] = st.text_input("IDFC Store ID *")
            company_fields["Sales Point ID"] = st.text_input("Sales Point ID *")
            
        elif selected_partner == "PINELAB":
            company_fields["Pinelabs MID"] = st.text_input("Pinelabs MID *")
            company_fields["Pinelabs TID"] = st.text_input("Pinelabs TID *")

    submit_button = st.form_submit_button(label=f"Submit {selected_partner} Mapping Data")

# Form submission logic
if submit_button:
    # Check basic fields validation
    basic_fields_valid = all([apple_id, store_name, address, city, area, pincode, contact_person, contact_number, email_id])
    # Check company specific fields validation
    company_fields_valid = all(company_fields.values())
    
    if not (basic_fields_valid and company_fields_valid):
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
        }
        # Add dynamic company specific fields to record
        new_record.update(company_fields)
        
        st.session_state.mapping_records.append(new_record)
        st.success(f"✅ Mapping data for {selected_partner} successfully saved!")

# Display Data Table
st.write("---")
st.subheader("📊 Submitted Mapping Records")

if st.session_state.mapping_records:
    df_records = pd.DataFrame(st.session_state.mapping_records)
    
    # Filter by selected partner
    filtered_df = df_records[df_records["Partner"] == selected_partner]
    
    if not filtered_df.empty:
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
        st.info(f"No records found for {selected_partner}. Fill the form above to add entries.")
else:
    st.info("No records submitted yet.")
