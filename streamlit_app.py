import streamlit as st

st.title("Streamlit Tutorial App")
st.write("This is my new app")

button1 = st.button("Click me")
if button1:
    st.write("This is some text")
