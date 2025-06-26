# app.py
import streamlit as st
from backend.parser import read_code_file, detect_language
from backend.explain import generate_summary
from backend.utils import highlight_keywords

st.set_page_config(page_title="SyntaxSage", layout="wide")
st.title("SyntaxSage")

uploaded_file = st.file_uploader("Upload a code file", type=["py", "java", "cob", "txt"])
code_input = st.text_area("Or paste your code here", height=200)
context = st.text_input("Optional: Add context (e.g., banking system)")

if uploaded_file or code_input:
    code = read_code_file(uploaded_file) if uploaded_file else code_input
    lang = detect_language(code)

    st.markdown(f"Detected Language: **{lang.upper()}**")
    
    with st.spinner("Generating explanation..."):
        explanation = generate_summary(code, lang)
        highlighted = highlight_keywords(explanation, ["function", "loop", "return", "if", "validate", "calculate"])

    st.subheader("🧠 Explanation")
    st.markdown(highlighted)
    
    st.download_button("📥 Download Explanation", explanation, file_name="explanation.txt")
