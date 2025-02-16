from openai import OpenAI
from dotenv import load_dotenv
import streamlit as st
import os

from prompts import agent_role

load_dotenv()  

key = os.environ['OPENAI_API_KEY'] = st.secrets['OPENAI_API_KEY']

if not key:
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
else:
    client = OpenAI(api_key=key)



def ai_search(prompt):
    print("Thinking")
    stream = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": agent_role + prompt}],
        stream=True,
    )

    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            yield chunk.choices[0].delta.content 
        
            
            
    