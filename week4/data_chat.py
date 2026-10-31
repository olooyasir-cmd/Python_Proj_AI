"""Meeting 7 student starter. See docs/LABS.md. This is intentionally unfinished.
Build week4/dashboard.py first: TODOs 1 and 2 reuse its code.
Notebooks named below are in week1/notebooks/. They teach the Python here, not Streamlit
or pandas: for those use docs/LABS.md, Meeting 7 and coursekit/sales.py.
Stuck after trying? See solutions/week4/data_chat.py."""
import streamlit as st
from coursekit.ui import configuration, request
st.set_page_config(page_title='Ask Your Sales Data')
st.title('Ask Your Sales Data')
config = configuration()
st.info("Student starter: implement the checklist below during the guided lab.")
# TODO 1: Read and validate the sales CSV.
#   How: same as week4/dashboard.py. Add sales_input to the import above, call it,
#   and use st.stop() if it returns None.
st.write('1. Read and validate the sales CSV.')
# TODO 2: Use summarise() and display the exact facts supplied to AI.
#   How: from coursekit.sales import summarise, then summary = summarise(df).
#   Show the whole dictionary with st.json(summary), so users can check the AI's claims.
#   Help: week1-deepdive-2-think-like-a-programmer.ipynb, section 5 (Dictionaries).
st.write('2. Use summarise() and display the exact facts supplied to AI.')
# TODO 3: Collect a bounded question in a form.
#   How: inside st.form, add st.text_input('Question', max_chars=1000) and a submit button.
#   "Bounded" means limited: reply() rejects anything over 1,000 characters.
#   Blank questions: test question.strip() and show guidance instead of calling AI.
#   Help: week1-deepdive-1-python-speaks.ipynb, section 4 (String methods).
st.write('3. Collect a bounded question in a form.')
# TODO 4: Explain unsupported questions; never execute model-generated code.
#   How: from coursekit.sales import analysis_instructions, then pass
#   analysis_instructions(summary) to request(). Those instructions tell the AI to
#   say so when the facts cannot answer. Also tell users on the page what it cannot know.
#   Safety: show replies as text only. Never pass them to exec() or eval().
#   Check: ask for the largest group, then about a date or cause that isn't in the data.
#   Live mode only: compare the answer with the facts, because the AI can still be wrong.
#   Check: docs/ACCEPTANCE.md, "Data apps".
st.write('4. Explain unsupported questions; never execute model-generated code.')
