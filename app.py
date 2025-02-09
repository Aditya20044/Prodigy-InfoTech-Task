import streamlit as st
import os

st.title("My Streamlit App")
st.write("Hello, this is a test deployment on Render!")

# Get the correct PORT from the environment variable
port = int(os.environ.get("PORT", 8501))  # Default is 8501 for local use

if __name__ == "__main__":
    st.run(port=port, host="0.0.0.0")
