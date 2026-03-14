import streamlit as st
from prompts import tutor, code, interview, summary
from chatbot import ask

st.set_page_config(page_title="Ananth Chatbot", layout="wide")

style = """
<style>

[data-testid="stAppViewContainer"]{
background-image:url("https://tse3.mm.bing.net/th/id/OIP.25ZXOH19zwo6OKPZh1sbJgHaEK?pid=Api&P=0&h=180");
background-size:cover;
background-position:center;
background-attachment:fixed;
}

[data-testid="stHeader"]{
background:transparent;
}

h1{
color:white;
}

label{
color:white !important;
}

textarea{
background:rgba(0,0,0,0.6) !important;
color:white !important;
border-radius:10px !important;
}

.stSelectbox div[data-baseweb="select"]{
background:rgba(0,0,0,0.6);
color:white;
border-radius:10px;
}

.stButton button{
background:rgba(0,0,0,0.7);
color:white;
border-radius:8px;
}

.box{
background:rgba(0,0,0,0.65);
padding:25px;
border-radius:12px;
color:white;
margin-top:20px;
font-size:18px;
white-space:pre-wrap;
}

</style>
"""

st.markdown(style, unsafe_allow_html=True)

st.title("Ananth Chatbot")

mode = st.selectbox(
"Select Mode",
["Tutor","Code Assistant","Interview Coach","Summarizer"]
)

question = st.text_area("Enter your question", height=180)

if st.button("Ask"):

    if not question.strip():
        st.warning("Enter a question")

    else:

        prompt_map = {
        "Tutor": tutor,
        "Code Assistant": code,
        "Interview Coach": interview,
        "Summarizer": summary
        }

        with st.spinner("Thinking..."):
            prompt = prompt_map[mode](question)
            response = ask(prompt)

        st.markdown(f"<div class='box'>{response}</div>", unsafe_allow_html=True)
