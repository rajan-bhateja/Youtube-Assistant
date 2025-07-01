import streamlit as st

st.set_page_config(page_title="Youtube Assistant", layout="wide")
st.title("Youtube Assistant")
st.caption("Powered by Langchain, Streamlit, ...")

col1, col2 = st.columns(2)

with col1:
    with st.form(key='my_form'):
        youtube_url = st.text_input("Enter YouTube video URL:")
        user_query = st.text_input("Enter your query:")
        submit_button = st.form_submit_button(label='Submit')

        if submit_button is not None:
            st.write("URL:", youtube_url)
            st.write("Query:", user_query)

        else:
            st.warning("You didn't submit anything")

with col2:
    st.header("Assistant's Response:")
    with st.spinner("Working on it...", width="content"):
        pass