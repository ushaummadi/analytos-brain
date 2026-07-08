import streamlit as st

from pipeline.hybrid_search import ask
from policy import check_access

st.title("🧪 MCP Tester")

role = st.selectbox(
    "Agent",
    [
        "content-agent",
        "gtm-agent"
    ]
)

question = st.text_input("Question")

if st.button("Ask"):

    # Block EmailThread access
    if "email" in question.lower():

        if not check_access(role, "EmailThread"):

            st.error("❌ Access Denied")
            st.stop()

    answer, context = ask(question)

    st.success(answer)

    with st.expander("Context"):
        st.code(context)