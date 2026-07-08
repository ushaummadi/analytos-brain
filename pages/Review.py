import streamlit as st

from review import (
    get_branch_diff,
    merge_branch,
    delete_branch
)

from database import save_approval

# -------------------------------------------------
# Session State
# -------------------------------------------------

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "username" not in st.session_state:
    st.session_state.username = ""

# -------------------------------------------------
# Login Check
# -------------------------------------------------

if not st.session_state.logged_in:

    st.error("🔒 Please login first from the main application.")

    st.stop()

# -------------------------------------------------
# Page
# -------------------------------------------------

st.set_page_config(
    page_title="Human Review",
    page_icon="✅",
    layout="wide"
)

st.title("🧑 Human-in-the-Loop Review")

st.write(
    "Review the changes on an ingestion branch before merging them into **main**."
)

# -------------------------------------------------
# Branch Input
# -------------------------------------------------

branch = st.text_input(
    "Branch Name",
    value="ingest-stockly"
)

# -------------------------------------------------
# Show Diff
# -------------------------------------------------

if st.button(
    "📄 Show Diff",
    key="show_diff_btn",
    use_container_width=True
):

    diff = get_branch_diff(branch)

    st.subheader("Branch Diff")

    if diff.strip():

        st.code(diff)

    else:

        st.info("No changes found.")

# -------------------------------------------------
# Review Actions
# -------------------------------------------------

st.divider()

col1, col2 = st.columns(2)

# ---------------- Approve ----------------

with col1:

    if st.button(
        "✅ Approve & Merge",
        key="approve_btn",
        use_container_width=True
    ):

        output = merge_branch(branch)

        save_approval(
            branch=branch,
            approved_by=st.session_state.username
        )

        st.success("Branch merged successfully.")

        st.code(output)

        st.rerun()

# ---------------- Reject ----------------

with col2:

    if st.button(
        "❌ Reject",
        key="reject_btn",
        use_container_width=True
    ):

        output = delete_branch(branch)

        st.warning("Branch rejected and deleted.")

        st.code(output)

        st.rerun()

# -------------------------------------------------
# Reviewer Information
# -------------------------------------------------

st.divider()

st.info(
    f"👤 Reviewer: **{st.session_state.username}**"
)