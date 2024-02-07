import streamlit as st
import hashlib
import datetime

class Block:
    def __init__(self, index, previous_hash, timestamp, data, current_hash):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.current_hash = current_hash

def calculate_hash(index, previous_hash, timestamp, data):
    value = str(index) + str(previous_hash) + str(timestamp) + str(data)
    return hashlib.sha256(value.encode()).hexdigest()

def create_genesis_block():
    return Block(0, "0", datetime.datetime.now(), "Genesis Block", calculate_hash(0, "0", datetime.datetime.now(), "Genesis Block"))

def create_new_block(previous_block, data):
    index = previous_block.index + 1
    now = datetime.datetime.now()
    timestamp = now.strftime(" %d-%b-%Y - %I:%M %p")
    current_hash = calculate_hash(index, previous_block.current_hash, timestamp, data)
    return Block(index, previous_block.current_hash, timestamp, data, current_hash)

if 'password_chain' not in st.session_state:
    st.session_state.password_chain = [create_genesis_block()]

st.title(":blue[Blockchain Password] Manager")

st.sidebar.header("Password Manager")
action = st.sidebar.selectbox("Select Action", ["Add Password", "View Passwords"])

if action == "Add Password":
    new_password = st.text_input("Enter a new password:", type="password")
    if st.button("Add"):
        previous_block = st.session_state.password_chain[-1]
        new_block = create_new_block(previous_block, new_password)
        st.session_state.password_chain.append(new_block)
        st.success("Password added successfully!")

elif action == "View Passwords":
    st.header("Password List")
    for block in st.session_state.password_chain[1:]:
        # st.write(f"Index: {block.index}")
        # st.write(f"Timestamp: {block.timestamp}")
        # st.write(f"Data: {block.data}")
        # st.write(f"Current Hash: {block.current_hash}")
        # st.write("-" * 50)

        st.markdown(f'''
        <div style="color:#fff;border: 1px solid;border-radius:15px;padding:15px;margin:15px;">
            <div style="display:flex;justify-content:space-between;align-item:center;">
                <div><strong>Index : </strong>{block.index} </div>
                <div><strong>Timestamp : </strong>{block.timestamp} </div>
            </div>
            <strong>Data :</strong> {block.data}<br>
            <strong>Hash :</strong> {block.current_hash}
        </div>
        ''',
        unsafe_allow_html=True
        )

c31,c11,c12 = st.columns([3,1,5])
c11.image("logo.png", width=200)
