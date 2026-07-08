import streamlit as st

from pipeline.gtm_agent import generate_gtm

st.set_page_config(
    page_title="GTM Agent",
    page_icon="🎯",
    layout="wide"
)

st.title("🎯 GTM Agent")

st.subheader("Generate a Prospecting Brief using Omnigraph Knowledge")

product = st.text_input(
    "Product",
    value="Stockly"
)

if st.button(
    "Generate GTM Brief",
    use_container_width=True
):

    with st.spinner("Generating Prospecting Brief..."):

        brief = generate_gtm(product)

    st.success("Prospecting Brief Generated")

    st.markdown("---")

    st.markdown(brief)

    st.download_button(
        label="📄 Download Brief",
        data=brief,
        file_name="gtm_brief.md",
        mime="text/markdown"
    )