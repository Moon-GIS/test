import ee
import streamlit as st

service_account = st.secrets["google_earth_engine"]["client_email"]
credentials = ee.ServiceAccountCredentials(service_account, st.secrets["google_earth_engine"])
ee.Initialize(credentials)
