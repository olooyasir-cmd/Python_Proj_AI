"""Meeting 8 student starter. See docs/LABS.md. This is intentionally unfinished.
Notebooks named below are in week1/notebooks/.
Stuck after trying? See the example in solutions/capstone/app.py, but build your own idea."""
import streamlit as st
from coursekit.ui import configuration, request
st.set_page_config(page_title='My Capstone App')
st.title('My Capstone App')
config = configuration()
st.info("Student starter: implement the checklist below during the guided lab.")
# TODO 1: Write the problem and user in capstone/README.md.
#   How: fill in the project details and the planning table, and agree on one core feature.
#   Do this as a group before writing app code. Pick an assistant or data analyst project.
st.write('1. Write the problem and user in capstone/README.md.')
# TODO 2: Build input -> validation -> useful output first.
#   How: no AI yet. Reuse your closest guided app as a base:
#   assistant: week2/app.py or week3/chatbot.py. Data analyst: week4/dashboard.py.
#   Help: week1-deepdive-1-python-speaks.ipynb, section 7 (input -> transform -> output).
#   Help: week1-deepdive-2-think-like-a-programmer.ipynb, sections 3 and 6.
st.write('2. Build input -> validation -> useful output first.')
# TODO 3: Add AI only where it helps; handle missing configuration.
#   How: let Python do anything that must be exact. Call request() only after a user action.
#   request() shows missing-key errors and returns None, so check for None before saving.
#   Test it: run live mode without a key and expect a readable error (see SETUP.md, section 4).
st.write('3. Add AI only where it helps; handle missing configuration.')
# TODO 4: Test, deploy, and document each member's contribution.
#   Test: python -m pytest -q, then docs/ACCEPTANCE.md on a teammate's machine.
#   Deploy: week5/DEPLOY.md. Document: complete the submission list in capstone/README.md.
#   Team: each member codes a feature on a branch and reviews a teammate's pull request.
st.write("4. Test, deploy, and document each member's contribution.")
