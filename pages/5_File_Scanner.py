import streamlit as st 

st.title(":blue[File] Scanner")

detection = False

malicious = ["rd c:\system32", "del c:\\", "rd c:\\"]

fs = st.file_uploader("Upload a file")

if st.button("Scan"):
    if fs is not None:
        if fs.name.endswith(".bat"):
            batch = fs.getvalue().decode("utf-8")
            codes = batch.split("\n")
            for line in codes:
                for maliciouscode in malicious:
                    if maliciouscode.lower() == line.lower():
                        detection = True
                if detection == True:
                    st.error("Virus detected!")
                else:
                    st.success("No virus detected!")
        else:
            st.success("No virus detected!")
    else:
        st.error("Please upload a file!")

c31,c11,c12 = st.columns([3,1,5])
c11.image("logo.png", width=200)
