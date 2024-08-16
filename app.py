

import streamlit as st
import os

os.environ["MISTRAL_API_KEY"] = 'kgYDKvLmZ6tPlU2CyFFY2S642npGBHEM'

from langchain_mistralai import ChatMistralAI
from langchain import LLMChain,PromptTemplate
st.title("prototype")
model = ChatMistralAI(model="codestral-latest")
prompt=st.text_input("enter the text")
template = ''' 
          CONTEXT: {scenario}
          STORY: 
  '''

prompttemp = PromptTemplate (template = template, input_variables = ['scenario'])

if prompt:
    req=LLMChain(llm=model,prompt=prompttemp)
    response=req.invoke(prompt)
    st.write(response)
