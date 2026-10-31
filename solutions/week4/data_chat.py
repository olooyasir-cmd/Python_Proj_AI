"""Solution for Meeting 7. Try week4/data_chat.py yourself first.
Run: python -m streamlit run solutions/week4/data_chat.py"""
import streamlit as st
from coursekit.sales import analysis_instructions, summarise
from coursekit.ui import configuration, request, sales_input
st.set_page_config(page_title='Ask Your Sales Data')
st.title('Ask Your Sales Data')
config = configuration()

# TODO 1: the same validated loading as the dashboard.
df = sales_input()
if df is None:
    st.stop()

# TODO 2: show the exact facts, so users can check the AI's claims against them.
summary = summarise(df)
st.subheader('Facts supplied to the AI')
st.json(summary)

# An answer only stays while it matches the facts on screen.
if st.session_state.get('answered_facts') != summary:
    st.session_state.pop('answer', None)
    st.session_state.pop('answered_facts', None)

# TODO 3: a form sends one question at a time, with a length limit.
with st.form('question_form'):
    question = st.text_input('Question about these facts', max_chars=1000)
    submitted = st.form_submit_button('Ask')

# TODO 4: tell users the limits, and let the instructions cover unsupported questions.
st.caption('This app only knows the facts above. It has no dates, causes or profit figures.')

if submitted:
    st.session_state.pop('answer', None)
    if question.strip():
        messages = [{"role": "user", "content": question}]
        answer = request(messages, analysis_instructions(summary), config)
        if answer:
            st.session_state.answer = answer
            st.session_state.answered_facts = summary
    else:
        st.warning('Enter a question first.')

# TODO 4: the reply is only ever displayed as text, never run as code.
if 'answer' in st.session_state:
    st.write(st.session_state.answer)
