"""Meeting 5 student starter. See docs/LABS.md. This is intentionally unfinished.
Build week3/chatbot.py first: TODO 4 reuses its chat loop.
Notebooks named below are in week1/notebooks/. They teach the Python here, not Streamlit:
for st.* commands use docs/LABS.md, Meeting 5.
Stuck after trying? See solutions/week3/persona_bot.py."""
import streamlit as st
from coursekit.ui import configuration, request
st.set_page_config(page_title='Persona Studio')
st.title('Persona Studio')
config = configuration()
st.info("Student starter: implement the checklist below during the guided lab.")
# TODO 1: Create persona and tone controls.
#   How: make a dictionary, persona name -> description. In the sidebar, add st.selectbox
#   controls for persona, tone and answer detail ("with st.sidebar:").
#   list(your_dictionary) gives the persona options.
#   Help: week1-deepdive-2-think-like-a-programmer.ipynb, section 5 (Dictionaries).
st.write('1. Create persona and tone controls.')
# TODO 2: Build instructions from those choices.
#   How: combine the choices into one f-string, then show it with st.caption() or st.code().
#   Use answer detail here. The course doesn't use a temperature slider.
#   Help: week1-deepdive-1-python-speaks.ipynb, section 3 (f-strings).
st.write('2. Build instructions from those choices.')
# TODO 3: Start a new conversation when controls change.
#   How: put the current choices in a tuple, such as choices = (persona, tone, detail).
#   If st.session_state.get('choices') != choices, save the new choices and empty messages.
#   Why: old replies could conflict with the new persona.
#   Help: week1-deepdive-2-think-like-a-programmer.ipynb, section 3 (Decisions, !=).
st.write('3. Start a new conversation when controls change.')
# TODO 4: Reuse the chat loop and keep only five exchanges.
#   How: copy TODOs 2-4 from week3/chatbot.py and pass your instructions to request().
#   One exchange is two messages, so after saving a turn keep the last ten:
#   st.session_state.messages = st.session_state.messages[-10:]
#   [-10:] is new. It extends the [-1] indexing from Deep Dive 2, section 1 (Lists).
#   Check: docs/ACCEPTANCE.md, "Chat/persona". Then deploy with week5/DEPLOY.md.
st.write('4. Reuse the chat loop and keep only five exchanges.')
