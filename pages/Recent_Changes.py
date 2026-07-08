import streamlit as st
from database import get_approvals

st.title("🕒 Recent Changes")

approvals = get_approvals()

if approvals:

    for branch, user, date in approvals:

        st.success(f"""
✅ **{branch}**

Approved By: **{user}**

{date}
""")

else:

    st.info("No approvals found.")