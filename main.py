from dotenv import load_dotenv
import streamlit as st
from langchain_openai import ChatOpenAI
import os

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_KEY")
chat_model = ChatOpenAI(api_key=OPENAI_API_KEY, model_name="gpt-3.5-turbo")
st.title('AI 작사가')

content = st.text_input('작사할 주제를 제시해주세요.')
if st.button('작사 요청하기'):
    result = chat_model.invoke(content + "에 대한 노래의 작사를 해 줘")
    st.write(result.content)
