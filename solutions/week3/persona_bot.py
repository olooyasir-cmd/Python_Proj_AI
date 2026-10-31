"""Solution for Meeting 5. Try week3/persona_bot.py yourself first.
Run: python -m streamlit run solutions/week3/persona_bot.py"""
import streamlit as st
from coursekit.ui import configuration, request
st.set_page_config(page_title='Persona Studio')
st.title('Persona Studio')
config = configuration()

PERSONAS = {
    'Patient tutor': 'a patient tutor who explains ideas step by step',
    'Career coach': 'a practical career coach who gives clear next steps',
    'Market trader': 'a friendly Accra market trader who uses everyday examples',
}

# TODO 1: the sidebar controls.
with st.sidebar:
    persona = st.selectbox('Persona', list(PERSONAS))
    tone = st.selectbox('Tone', ['warm', 'direct', 'playful'])
    detail = st.selectbox('Answer detail', ['brief', 'moderate', 'thorough'])

# TODO 2: every prompt is just a string, so an f-string can build it.
instructions = f'You are {PERSONAS[persona]}. Use a {tone} tone and give {detail} answers.'
st.caption(instructions)

# TODO 3: a change of choices starts fresh, so old replies cannot conflict with them.
choices = (persona, tone, detail)
if st.session_state.get('choices') != choices:
    st.session_state.choices = choices
    st.session_state.messages = []

# TODO 4: the same chat loop as week3/chatbot.py, using the built instructions.
for msg in st.session_state.messages:
    with st.chat_message(msg['role']):
        st.write(msg['content'])

if question := st.chat_input('Ask a question'):
    new_message = {"role": "user", "content": question}
    answer = request(st.session_state.messages + [new_message], instructions, config)
    if answer:
        st.session_state.messages.append(new_message)
        st.session_state.messages.append({"role": "assistant", "content": answer})
        # One exchange is two messages, so ten messages is five exchanges.
        st.session_state.messages = st.session_state.messages[-10:]
        st.rerun()
