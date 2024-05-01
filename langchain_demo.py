import constants
from langchain_community.llms import OpenAI
import streamlit as st

st.title('Langchain Demo With OPENAI API')
input_text = st.text_input("Search the topic u want")

# OPENAI LLMS
llm = OpenAI(api_key=constants.openai_key, temperature=0.8)

if input_text:
    st.write(llm(input_text))
