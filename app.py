import streamlit as st
import pandas as pd
import requests

st.title("OCR Invoice Monitoring")

if st.button("Fetch"):
    st.info("Calling Staple OCR API...")
