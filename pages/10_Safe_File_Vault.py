# File safe vault
import streamlit as st 
import hashlib

st.title(":blue[File safe] vault")

uploaded_file = st.file_uploader("Choose a file")

if st.button("Submit"):
    if uploaded_file is not None:
        st.markdown(
            f"""
                <style>
                    .container {{
                        width: 100%;
                        height: 100%;
                        display: flex;
                        flex-direction: column;
                        padding: 1rem;
                        box-sizing: border-box;
                        border-radius: 0.5rem;
                        border: 1px solid ;
                        margin-bottom: 1rem;
                    }}

                </style>
                <div class="container">
                    <div class="row">
                        <b>File Name:</b> {uploaded_file.name}
                    </div>
                    <div class="row">
                        <b>File Type:</b> {uploaded_file.type}
                    </div>
                    <div class="row">
                        <b>File Size:</b> {uploaded_file.size}
                    </div>
                    <div class="row">
                        <b>Hash Value:</b> {hashlib.sha256(uploaded_file.name.encode()).hexdigest()}
                    </div>
                    
                </div>
            """,
            unsafe_allow_html=True,
        )
        st.success("Saved File")
    else:
        st.warning("No File Selected")


c31,c11,c12 = st.columns([3,1,5])
c11.image("logo.png", width=200)
