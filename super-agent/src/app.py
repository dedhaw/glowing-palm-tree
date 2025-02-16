import streamlit as st
from agent import ai_search
from virtual_browser import search, exec_search


st.title("Virtual Browser")
st.write("This is a virtual browser")

input_query = st.text_input("Website URL or Search Query", "")

def stream_ai_response(query):
    stream = ai_search(query)
    response_container = st.empty()
    full_response = ""

    for chunk in stream:
        full_response += chunk
        response_container.markdown(full_response)

    return full_response

if input_query:
    response = stream_ai_response(input_query)
    if response:
        exec_search(response)