import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv

from utils import load_pdf, split_documents, build_vectorstore, retrieve_context
from prompts import PRO_PROMPT, CON_PROMPT, MODERATOR_PROMPT

load_dotenv()

# Configure Gemini
genai.configure(api_key="AIzaSyDlWGoBEeDF9pWKvRZ_00zcYOlq61usKPU")

def gemini_call(prompt, model="gemini-1.5-flash"):
    response = genai.GenerativeModel(model).generate_content(prompt)
    return response.text

st.title("🤖 DebateBot – RAG + Gemini")

uploaded_file = st.file_uploader("Upload a policy report (PDF)", type=["pdf"])
topic = st.text_input("Enter debate topic (e.g., 'AI in Education')")

if uploaded_file and topic:
    text = load_pdf(uploaded_file)
    chunks = split_documents(text)
    vs = build_vectorstore(chunks)

    st.success("PDF processed! Ready for debate.")

    if st.button("Start Debate"):
        context = retrieve_context(topic, vs)

        pro = gemini_call(PRO_PROMPT.format(topic=topic, context=context))
        con = gemini_call(CON_PROMPT.format(topic=topic, context=context))
        summary = gemini_call(MODERATOR_PROMPT.format(pro=pro, con=con))

        st.subheader("🟢 Pro Side")
        st.write(pro)

        st.subheader("🔴 Con Side")
        st.write(con)

        st.subheader("⚖️ Moderator’s Summary")
        st.write(summary)
