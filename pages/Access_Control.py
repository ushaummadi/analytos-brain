import streamlit as st
from policy import check_access

st.title("🔐 Cedar Policy Demo")

role = st.selectbox(
    "Role",
    [
        "content-agent",
        "gtm-agent"
    ]
)

resource = st.selectbox(
    "Resource",
    [
        "Product",
        "Feature",
        "ProofPoint",
        "Persona",
        "ICPSegment",
        "EmailThread"
    ]
)

if st.button("Check Access"):

    if check_access(role, resource):

        st.success("✅ Allowed")

    else:

        st.error("❌ Access Denied")