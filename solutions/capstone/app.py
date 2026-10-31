"""Example solution for Meeting 8: a small study planner. Try capstone/app.py yourself first.
Your capstone must solve your own problem: renaming this example is not an independent project.
TODOs 1 and 4 are mostly group work: planning in capstone/README.md, then tests and deployment.
Run: python -m streamlit run solutions/capstone/app.py"""
import streamlit as st
from coursekit.ui import configuration, request
st.set_page_config(page_title='Study Planner')
st.title('Study Planner')
config = configuration()


def build_plan(topics_text, days, hours_per_day):
    # TODO 2: exact Python logic, kept apart from the display so it is easy to check.
    topics = [topic.strip() for topic in topics_text.split(',') if topic.strip()]
    if not topics:
        raise ValueError('Enter at least one topic, separated by commas.')
    if len(topics) > days:
        raise ValueError('Choose one topic per day at most: add days or remove topics.')
    hours_per_topic = days * hours_per_day / len(topics)
    return {'topics': topics, 'total_hours': days * hours_per_day,
            'hours_per_topic': round(hours_per_topic, 1)}


# TODO 2: input -> validation -> useful output, all without AI.
with st.form('plan_form'):
    topics_text = st.text_input('Topics, separated by commas', max_chars=500)
    days = st.number_input('Days until the exam', min_value=1, max_value=60, value=7, step=1)
    hours_per_day = st.number_input('Study hours per day', min_value=1, max_value=8, value=2, step=1)
    submitted = st.form_submit_button('Build plan')

if submitted:
    st.session_state.pop('plan', None)
    st.session_state.pop('advice', None)
    try:
        st.session_state.plan = build_plan(topics_text, days, hours_per_day)
    except ValueError as exc:
        st.error(str(exc))

if 'plan' in st.session_state:
    plan = st.session_state.plan
    st.metric('Total study hours', plan['total_hours'])
    st.write(f"About {plan['hours_per_topic']} hours for each topic:")
    for topic in plan['topics']:
        st.write(f'- {topic}')

    # TODO 3: AI only adds tips. It runs on a click, and request() handles missing configuration.
    if st.button('Get study tips'):
        instructions = ('You are a study coach. Give short tips for this plan and do not change '
                        f"its hours: {plan['topics']}, {plan['hours_per_topic']} hours per topic.")
        advice = request([{"role": "user", "content": 'Give me tips for this plan.'}],
                         instructions, config)
        if advice:
            st.session_state.advice = advice

if 'advice' in st.session_state:
    st.write(st.session_state.advice)
