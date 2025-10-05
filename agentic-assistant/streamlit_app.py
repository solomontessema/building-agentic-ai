import streamlit as st
from agents.base_agent import agent

st.set_page_config(page_title="Agentic Assistant", layout="wide")
st.title("🤖 Agentic Assistant Dashboard")

# Input box
user_query = st.text_input("Enter your question:")

# Run the agent if input is given
if user_query:
    with st.spinner("Thinking..."):
        response = agent.run(user_query)
        st.markdown("**Response:**")
        st.write(response)
