from google import genai
import streamlit as st

client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])

def ask(prompt):
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        return response.text
    except Exception as e:
        return f"API Error: {e}"
