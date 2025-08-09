import streamlit as st

st.title("Cat vs Dog Classifier")
st.text("Built by Gamas Chang")

uploaded_file = st.file_uploader("Gamas upload an image...", type=["jpg", "png", "jpeg"])
if uploaded_file is not None:
    st.image(uploaded_file, use_container_width=True)
