import streamlit as st
import pandas as pd
import zipfile
import requests
import io

st.title("📂 Load CSV from ZIP (GitHub)")

# ✅ Replace with your actual GitHub file URL
zip_url = "/Users/adityakumar/Downloads/US_Accidents_March23.csv.zip"

# Download ZIP file from GitHub
response = requests.get(zip_url)
if response.status_code == 200:
    zip_file = io.BytesIO(response.content)  # Convert to file-like object
    
    # Extract ZIP file
    with zipfile.ZipFile(zip_file, "r") as z:
        csv_files = [f for f in z.namelist() if f.endswith(".csv")]
        
        if csv_files:
            with z.open(csv_files[0]) as f:
                df = pd.read_csv(f)
                st.write("### ✅ Loaded Data:")
                st.dataframe(df)
        else:
            st.error("⚠️ No CSV file found in the ZIP.")
else:
    st.error("⚠️ Failed to download ZIP file from GitHub.")
