## Conversational Q&A Chatbot

from langchain.schema import HumanMessage, SystemMessage, AIMessage
from langchain_community.chat_models import ChatOpenAI
from dotenv import load_dotenv

import streamlit as st

# Global keywords
state_keyword = 'history_messages'
chat = ChatOpenAI(temperature=0.5)


# Function to load OpenAI model and get responses
def get_chatmodel_response(question):
    st.session_state[state_keyword].append(HumanMessage(content=question))
    answer = chat(st.session_state[state_keyword])
    st.session_state[state_keyword].append(AIMessage(content=answer.content))
    return answer.content


def setup_streamlit_ui():
    st.set_page_config(page_title="Conversational Q&A Chatbot")
    st.header("Hey, Let's Chat")
    if state_keyword not in st.session_state:
        st.session_state[state_keyword] = [SystemMessage(content="Yor are a comedian AI Assistant")]
    input_text = st.text_input("Input: ", key="input")
    response = get_chatmodel_response(input_text)
    submit = st.button("Ask the question")
    ## If ask button is clicked
    if submit:
        st.subheader("The Response is")
        st.write(response)

load_dotenv()
setup_streamlit_ui()
