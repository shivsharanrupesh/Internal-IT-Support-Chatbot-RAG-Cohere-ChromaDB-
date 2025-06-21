"""
Streamlit Chat Frontend for Internal IT Support Chatbot

- Connects to FastAPI backend at /ask.
- Each user/session is tracked by a UUID.
- Shows persistent chat history within the session.
"""

import streamlit as st
import requests
import uuid

st.set_page_config(page_title="IT Support Chatbot", page_icon="💬")
st.title("💬 Internal IT Support Chatbot")
st.markdown("""
Get instant, authoritative answers to your IT and network questions.
This chatbot uses your company's official PDF documentation as its knowledge base.
""")

# Generate or load a session ID (for conversation context)
if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())
# Persistent chat history for user session
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("Your IT question:", key="input")

if st.button("Ask") and user_input:
    payload = {
        "question": user_input,
        "session_id": st.session_state.session_id,
    }
    try:
        # Send question to backend API
        response = requests.post("http://localhost:8000/ask", json=payload, timeout=60)
        response.raise_for_status()
        data = response.json()
        # Add question and answer to chat history
        st.session_state.chat_history.append(("You", user_input))
        st.session_state.chat_history.append(("Bot", data["answer"]))
        # Display full chat history (most recent at bottom)
        for sender, message in st.session_state.chat_history:
            st.markdown(f"**{sender}:** {message}")
        # Show source document references if available
        if data.get("sources"):
            st.markdown("*Sources:*")
            for src in data["sources"]:
                st.markdown(f"- {src}")
    except Exception as e:
        st.error(f"Error contacting backend: {e}")

# Show chat history even if no new input
if not user_input:
    for sender, message in st.session_state.chat_history:
        st.markdown(f"**{sender}:** {message}")

st.markdown("---")
st.caption("Internal use only. For urgent or complex IT issues, contact the IT Service Desk.")
