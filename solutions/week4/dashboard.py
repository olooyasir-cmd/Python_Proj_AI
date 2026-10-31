"""Solution for Meeting 6. Try week4/dashboard.py yourself first.
Run: python -m streamlit run solutions/week4/dashboard.py"""
import pandas as pd
import streamlit as st
from coursekit.sales import analysis_instructions, summarise
from coursekit.ui import configuration, request, sales_input
st.set_page_config(page_title='Sales Dashboard')
st.title('Sales Dashboard')
config = configuration()

# TODO 1: sales_input() draws the sample checkbox and upload box, then validates the data.
df = sales_input()

# TODO 2: None means no valid data, and sales_input() has already explained why.
if df is None:
    st.stop()

# TODO 3: Python calculates every number shown here.
dimension = st.selectbox('Group by', ['product', 'region'])
metric = st.selectbox('Measure', ['revenue', 'units'])
summary = summarise(df, dimension, metric)

rows, units, revenue = st.columns(3)
rows.metric('Rows', summary['rows'])
units.metric('Units', f"{summary['total_units']:,.0f}")
revenue.metric('Revenue', f"{summary['total_revenue']:,.2f}")
st.bar_chart(pd.DataFrame(summary['shown_groups']).set_index('name'))

# TODO 4: an explanation only stays while it matches the facts on screen.
if st.session_state.get('explained_facts') != summary:
    st.session_state.pop('explanation', None)
    st.session_state.pop('explained_facts', None)

with st.expander('Facts sent to the AI when you click Explain'):
    st.json(summary)

if st.button('Explain'):
    messages = [{"role": "user", "content": 'Explain these sales facts.'}]
    answer = request(messages, analysis_instructions(summary), config)
    if answer:
        st.session_state.explanation = answer
        st.session_state.explained_facts = summary

if 'explanation' in st.session_state:
    st.write(st.session_state.explanation)
