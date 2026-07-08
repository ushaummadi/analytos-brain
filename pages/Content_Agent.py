import streamlit as st
from pipeline.content_agent import generate_blog

st.title("📝 Content Agent")

topic = st.text_input(
    "Blog Topic",
    "Inventory Optimization"
)

if st.button("Generate Blog"):

    with st.spinner("Generating..."):

        blog = generate_blog(topic)

    st.markdown(blog)