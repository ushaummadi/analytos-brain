import streamlit as st
from pipeline.hybrid_search import ask

st.title("🧪 MCP Tester")

role = st.selectbox(
    "Agent",
    ["content-agent", "gtm-agent"]
)

question = st.text_input("Question")

if st.button("Run"):

    # Restricted keywords
    restricted = [
        "email",
        "gmail",
        "internal",
        "thread",
        "conversation"
    ]

    # Content Agent restriction
    if role == "content-agent" and any(
        word in question.lower() for word in restricted
    ):
        st.error("""
❌ Access Denied

The **content-agent** role is not authorized to access:

• Internal Emails
• Email Threads
• Gmail Content
• Internal Communications

This request is blocked by the simulated Cedar access policy.
""")
        st.stop()

    # Otherwise execute normally
    answer, context = ask(question)

    st.success(answer)

    with st.expander("Context"):
        st.code(context)
