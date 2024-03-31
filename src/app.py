from dotenv import load_dotenv
import streamlit as st
from langchain.schema import HumanMessage, AIMessage
from utils import logger, get_response, check_password

load_dotenv()
st.set_page_config(page_title="💬 Shan's AI Chat Assist")


if 'auth' not in st.session_state:
    st.session_state['auth'] = False

if not st.session_state['auth']:
    st.session_state['password'] = st.text_input("Enter your password:", type='password')

    if st.button('Continue') or st.session_state["password"] and st.session_state["password"].strip() != "":
        if check_password(st.session_state['password']):
            logger.info("User is authenticated")
            st.session_state['auth'] = True
            st.success('Password Correct! Press continue button to access the chatbot..')
        else:
            st.error('Password Incorrect. Please try again.')
else:
    st.title("Sean's AI Chat Assist")

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    for message in st.session_state.chat_history:
        if isinstance(message, HumanMessage):
            with st.chat_message("Human"):
                st.markdown(message.content)
        else:
            with st.chat_message("AI"):
                st.markdown(message.content)

    user_query = st.chat_input('Type Your Message..')
    if user_query and user_query.strip() != "":
        st.session_state.chat_history.append(HumanMessage(user_query))

        with st.chat_message("Human"):
            st.markdown(user_query)

        with st.chat_message("AI"):
            stream_response = get_response(user_query, st.session_state.chat_history)
            ai_response = st.write_stream(stream_response)

        st.session_state.chat_history.append(AIMessage(ai_response))
