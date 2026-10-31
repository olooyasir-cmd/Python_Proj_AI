"""Meeting 6 student starter. See docs/LABS.md. This is intentionally unfinished.
Notebooks named below are in week1/notebooks/. They teach the Python here, not Streamlit
or pandas: for those use docs/LABS.md, Meeting 6 and coursekit/sales.py.
Stuck after trying? See solutions/week4/dashboard.py."""
import streamlit as st
from coursekit.ui import configuration, request
st.set_page_config(page_title='Sales Dashboard')
st.title('Sales Dashboard')
config = configuration()
st.info("Student starter: implement the checklist below during the guided lab.")
# TODO 1: Load sample/uploaded data with sales_input().
#   How: add sales_input to the coursekit.ui import above, then df = sales_input().
#   It draws the sample checkbox and the upload box for you.
#   Read: sales_input() in coursekit/ui.py.
st.write('1. Load sample/uploaded data with sales_input().')
# TODO 2: Validate before calculating; stop if no valid data.
#   How: sales_input() already validates with load_sales() and shows any error.
#   It returns None when there is no valid data, so: if df is None: st.stop()
#   Read: load_sales() in coursekit/sales.py, and explain each rejection.
#   Help: week1-deepdive-2-think-like-a-programmer.ipynb, section 3 (Decisions).
st.write('2. Validate before calculating; stop if no valid data.')
# TODO 3: Show verified metrics, grouped results and a chart.
#   How: from coursekit.sales import summarise. Add st.selectbox controls for dimension
#   (product, region) and metric (units, revenue), then call summarise(df, dimension, metric).
#   Show the totals with st.metric(). For the chart, import pandas as pd, then:
#   st.bar_chart(pd.DataFrame(summary['shown_groups']).set_index('name'))
#   Check: the sample has 8 rows, 885 units and 11,680 revenue; Accra revenue is 6,610.
#   Help: week1-deepdive-2-think-like-a-programmer.ipynb, section 5 (Dictionaries).
st.write('3. Show verified metrics, grouped results and a chart.')
# TODO 4: Generate an explanation only on button click; clear it when facts change.
#   How: from coursekit.sales import analysis_instructions. Under st.button('Explain'), call
#   request([{"role": "user", "content": 'Explain these facts.'}],
#           analysis_instructions(summary), config).
#   On success, save the answer and summary in session state. Show the facts you sent.
#   Clear: if the saved summary != the current summary, delete the saved explanation.
#   Help: week1-deepdive-2-think-like-a-programmer.ipynb, section 3 (Decisions, !=).
#   Check: docs/ACCEPTANCE.md, "Data apps".
st.write('4. Generate an explanation only on button click; clear it when facts change.')
