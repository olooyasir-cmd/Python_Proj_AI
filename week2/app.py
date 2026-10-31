"""Meeting 3 student starter. See docs/LABS.md. This is intentionally unfinished.
Notebooks named below are in week1/notebooks/. They teach the Python here, not Streamlit:
for st.* commands use docs/LABS.md, Meeting 3.
Stuck after trying? See solutions/week2/app.py."""
import streamlit as st
from coursekit.ui import configuration, request
st.set_page_config(page_title='Market Assistant')
st.title('Market Assistant')
config = configuration()
st.info("Student starter: implement the checklist below during the guided lab.")
# TODO 1: Create a form with product, quantity and question inputs.
#   How: inside "with st.form('order'):" add st.selectbox, st.number_input, st.text_input
#   and st.form_submit_button. Save the button's result: submitted = ...
#   Products: from coursekit.market import PRICES, then list(PRICES) gives the options.
#   Quantity: st.number_input('Quantity', min_value=1, max_value=100, value=1, step=1).
#   Keep those whole numbers: quote() rejects a decimal such as 1.0.
#   Help: week1-deepdive-1-python-speaks.ipynb, section 7 (input -> transform -> output).
st.write('1. Create a form with product, quantity and question inputs.')
# TODO 2: Use quote() and display receipt().
#   How: from coursekit.market import quote, receipt. Under "if submitted:" call quote(),
#   pass its dictionary to receipt(), and show the text with st.success().
#   quote() raises ValueError on bad input: use try/except ValueError and show st.error().
#   Read: coursekit/market.py. Check: 3 yams gives GHS 24.00.
#   Help: week1-deepdive-2-think-like-a-programmer.ipynb, section 5 (Dictionaries).
st.write('2. Use quote() and display receipt().')
# TODO 3: Call request() only after submission and non-empty question.
#   How: test question.strip(), then call request(messages, instructions, config).
#   messages is [{"role": "user", "content": ...}], and request() returns None on failure.
#   Include the receipt text in instructions so the AI explains Python's exact amount.
#   Why: Streamlit reruns this file on every interaction, so a call outside this
#   check could spend API credit by surprise.
#   Help: week1-deepdive-1-python-speaks.ipynb, sections 3 and 4 (f-strings, String methods).
#   Help: week1-deepdive-2-think-like-a-programmer.ipynb, section 3 (Decisions).
st.write('3. Call request() only after submission and non-empty question.')
# TODO 4: Save the result in session state.
#   How: inside the submit block, st.session_state.result = your text.
#   Display it outside that block, with an if 'result' in st.session_state check.
#   Check: submit once, change a widget, and the result is still there with no new AI call.
#   Help: week1-deepdive-2-think-like-a-programmer.ipynb, section 6 (the "in" check).
st.write('4. Save the result in session state.')
