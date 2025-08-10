import streamlit as st

st.title("Test Google Earth Engine Secrets")
st.write("GCP Project ID:", st.secrets["google_earth_engine"]["project_id"])
