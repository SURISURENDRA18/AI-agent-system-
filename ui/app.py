

import streamlit as st
import requests

st.set_page_config(page_title="AI Agent System", layout="wide")

st.title("🤖 Multi-Agent AI System")

query = st.text_input("Enter your query")


if st.button("Run"):
    if not query.strip():
        st.warning("Please enter a query")
    else:
        try:
            res = requests.post(
                "http://127.0.0.1:8000/run",
                json={"query": query},  
                timeout=60
            )

            data = res.json()

            st.subheader(" Research")
            st.write(data.get("research", "No data"))

            st.subheader(" Analysis")
            st.write(data.get("analysis", "No data"))

            st.subheader(" Draft")
            st.write(data.get("draft", "No data"))

            st.subheader(" Final Output")
            st.success(data.get("final", "No output"))

        except Exception as e:
            st.error(f"Error: {e}")
    