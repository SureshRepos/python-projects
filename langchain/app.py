#Bring in deps
import os
from apiKey import apiKey

import streamlit as st

from langchain_community.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

os.environ['OPENAI_API_KEY'] = apiKey

#App framework
st.title('Demo GPT')

prompt = st.text_input('plug in your prompt here!')

#Prompt Templates
title_template = PromptTemplate(
      input_variables = ['topic'],
      template='Give me real world project ideas using Large Language Models  {topic}'
)

#llms 
llm = OpenAI(temperature=0.9)
title_chain = LLMChain(llm=llm, prompt=title_template, verbose=True)

# show AI response to the screen if there's a prompt
if prompt:
    response = title_chain.run(topic=prompt)
    st.write(response)