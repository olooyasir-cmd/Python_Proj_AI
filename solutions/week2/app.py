"""Solution for Meeting 3. Try week2/app.py yourself first.
Run: python -m streamlit run solutions/week2/app.py"""
import streamlit as st
from coursekit.market import PRICES, quote, receipt
from coursekit.ui import configuration, request
st.set_page_config(page_title='Market Assistant')
st.title('Market Assistant')
config = configuration()

# TODO 1: a form waits for the submit button, so typing causes no AI calls.
with st.form('order'):
    product = st.selectbox('Product', list(PRICES))
    quantity = st.number_input('Quantity', min_value=1, max_value=100, value=1, step=1)
    question = st.text_input('Question about your order', max_chars=1000)
    submitted = st.form_submit_button('Get quote')

if submitted:
    # A new order replaces the old results, including any old AI answer.
    st.session_state.pop('receipt', None)
    st.session_state.pop('answer', None)
    try:
        # TODO 2: Python calculates the exact amount.
        text = receipt(quote(product, quantity))
    except ValueError as exc:
        st.error(str(exc))
    else:
        # TODO 4: session state keeps the results when Streamlit reruns this file.
        st.session_state.receipt = text
        # TODO 3: the only AI call, after submission and with a real question.
        if question.strip():
            instructions = ('You are a friendly market assistant. Explain this exact quote and '
                            f'do not change its amount or claim anything is in stock: {text}')
            answer = request([{"role": "user", "content": question}], instructions, config)
            if answer:
                st.session_state.answer = answer
        else:
            st.info('Add a question if you would like the assistant to explain your quote.')

# TODO 4: display outside the submit block so results survive later reruns.
if 'receipt' in st.session_state:
    st.success(st.session_state.receipt)
if 'answer' in st.session_state:
    st.write(st.session_state.answer)
