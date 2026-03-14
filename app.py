import streamlit as st
from prompts import tutor, code, interview, summary
from chatbot import ask

st.set_page_config(page_title="Ananth Chatbot", layout="wide")

style = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://tse3.mm.bing.net/th/id/OIP.25ZXOH19zwo6OKPZh1sbJgHaEK?pid=Api&P=0&h=180");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}

[data-testid="stHeader"] {
    background: transparent;
}

.box {
    background: rgba(0, 0, 0, 0.7);
    padding: 20px;
    border-radius: 10px;
    color: white;
    margin-top: 20px;
    font-size: 18px;
    line-height: 1.6;
    white-space: pre-wrap;
}

.stSelectbox label, .stTextArea label, h1 {
    color: white !important;
}
</style>
"""

st.markdown(style, unsafe_allow_html=True)
st.title("Ananth Chatbot")

mode = st.selectbox(
    "Select Mode",
    ["Tutor", "Code Assistant", "Interview Coach", "Summarizer"]
)

question = st.text_area("Enter your question", height=150)

if st.button("Ask"):
    if not question.strip():
        st.warning("Please enter a question before submitting.")
    else:
        prompt_map = {
            "Tutor": tutor,
            "Code Assistant": code,
            "Interview Coach": interview,
            "Summarizer": summary,
        }

        with st.spinner("Thinking..."):
            try:
                prompt = prompt_map[mode](question)
                response = ask(prompt)
                st.markdown(f"<div class='box'>{response}</div>", unsafe_allow_html=True)
            except Exception as e:
                st.error(f"Something went wrong: {e}")