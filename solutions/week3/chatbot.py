"""Solution for Meeting 4. Try week3/chatbot.py yourself first.
Run: python -m streamlit run solutions/week3/chatbot.py"""
import streamlit as st
from coursekit.ui import configuration, request
st.set_page_config(page_title='Study Buddy')
st.title('Study Buddy')
config = configuration()
INSTRUCTIONS = 'You are a patient study buddy. Explain ideas simply and use short examples.'

# TODO 1: the guard stops each rerun from wiping the conversation.
if 'messages' not in st.session_state:
    st.session_state.messages = []

# TODO 4: clear the conversation only, so the request limit counter keeps counting.
if st.sidebar.button('New conversation'):
    st.session_state.messages = []
    st.rerun()

# TODO 2: Streamlit redraws the page each run, so replay the saved messages.
for msg in st.session_state.messages:
    with st.chat_message(msg['role']):
        st.write(msg['content'])

# TODO 3: send the history plus the new question, without saving anything yet.
if question := st.chat_input('Ask a question'):
    new_message = {"role": "user", "content": question}
    answer = request(st.session_state.messages + [new_message], INSTRUCTIONS, config)
    # TODO 4: save both sides only on success, and keep the latest five exchanges.
    if answer:
        st.session_state.messages.append(new_message)
        st.session_state.messages.append({"role": "assistant", "content": answer})
        st.session_state.messages = st.session_state.messages[-10:]
        st.rerun()
