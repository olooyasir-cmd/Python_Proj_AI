"""Meeting 4 student starter. See docs/LABS.md. This is intentionally unfinished.
Notebooks named below are in week1/notebooks/. They teach the Python here, not Streamlit:
for st.* commands use docs/LABS.md, Meeting 4.
Stuck after trying? See solutions/week3/chatbot.py."""
import streamlit as st
from coursekit.ui import configuration, request
st.set_page_config(page_title='Study Buddy')
st.title('Study Buddy')
config = configuration()
st.info("Student starter: implement the checklist below during the guided lab.")
# TODO 1: Initialise messages once with an if-not-in guard.
#   How: if 'messages' not in st.session_state: st.session_state.messages = []
#   Why: Streamlit reruns this file on every interaction, so a plain list would reset.
#   Try the counter exercise in docs/LABS.md, Meeting 4 first to see this happen.
#   Help: week1-deepdive-2-think-like-a-programmer.ipynb, section 1 (Lists)
#   and section 6 (the "in" check).
st.write('1. Initialise messages once with an if-not-in guard.')
# TODO 2: Replay saved user/assistant messages as chat bubbles.
#   How: loop over st.session_state.messages. For each one, use
#   "with st.chat_message(msg['role']):" and st.write(msg['content']) inside it.
#   Help: week1-deepdive-2-think-like-a-programmer.ipynb, section 5 (the conversation loop).
#   Practice: week1-assignment.ipynb, Challenge 8 (looping over a chat).
st.write('2. Replay saved user/assistant messages as chat bubbles.')
# TODO 3: Capture a question and call request() with the latest history.
#   How: if question := st.chat_input('Ask a question'):
#   Build a new message, then pass st.session_state.messages + [new_message] to request().
#   Don't append yet: a failed call must not leave half a turn in the history.
#   Careful: the notebooks show a "system" message, but reply() rejects that role.
#   Pass the bot's job as the instructions string instead.
#   Read: reply() in coursekit/ai.py to see the rules each message must follow.
st.write('3. Capture a question and call request() with the latest history.')
# TODO 4: Save successful turns and add a New conversation button.
#   How: request() returns None on failure. Only when you get text back, append the user
#   message and {"role": "assistant", "content": answer}. Then call st.rerun() to show them.
#   Button: set st.session_state.messages = [] and call st.rerun(). Don't use
#   st.session_state.clear(), because it would also reset the 20-request limit counter.
#   Help: week1-deepdive-2-think-like-a-programmer.ipynb, section 1 (.append()).
#   Check: docs/ACCEPTANCE.md, "Chat/persona". Demo mode shows the count growing, but only
#   live mode can show a real follow-up answer.
st.write('4. Save successful turns and add a New conversation button.')
