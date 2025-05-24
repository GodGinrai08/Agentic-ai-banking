import streamlit as st
import requests
import json

st.title("💸 Banking Transaction Insights")

uploaded_file = st.file_uploader("Upload your transaction file (JSON)", type="json")

if uploaded_file:
    with open("temp_transactions.json", "wb") as f:
        f.write(uploaded_file.read())

    st.success("File uploaded successfully!")

    if st.button("Analyze"):
        with st.spinner("Analyzing..."):
            response = requests.post(
                "http://localhost:8000/analyze",  # Your FastAPI endpoint
                json={"path": "temp_transactions.json"}
            )
            if response.status_code == 200:
                result = response.json()
                st.subheader("📊 Summary")
                st.json(result["summary"])
            else:
                st.error(f"Error: {response.json()['detail']}")
