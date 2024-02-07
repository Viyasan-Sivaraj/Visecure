import streamlit as st

def is_good_upi_id(upi_id):
    # Check if the UPI ID has consecutive repeated alphabetic characters like "aaaa"
    for i in range(len(upi_id) - 3):
        if upi_id[i:i+4].isalpha() and upi_id[i:i+4] == upi_id[i]*4:
            return False
    
    # Check if the UPI ID contains excessive digits or characters
    if sum(c.isdigit() for c in upi_id) >= len(upi_id) / 2:
        return False
    
    # Check for excessive consecutive repeating characters (like "abbbbb")
    max_consecutive_repeats = 3
    for i in range(len(upi_id) - max_consecutive_repeats):
        if upi_id[i:i+max_consecutive_repeats].isalpha() and upi_id[i:i+max_consecutive_repeats] == upi_id[i] * max_consecutive_repeats:
            return False
    
    # Check for patterns that might indicate a fake/malicious UPI ID
    suspicious_patterns = ["123", "abc", "admin", "test", "username"]
    if any(pattern in upi_id.lower() for pattern in suspicious_patterns):
        return False
    
    # You can add more criteria here if needed
    return True


def upi_id_scanner():
    st.title(":blue[UPI ID] Scanner")

    upi_id = st.text_input("Enter UPI ID:")
    if st.button("Scan"):
        if is_good_upi_id(upi_id):
            st.success("Good UPI ID")
        else:
            st.error("Potentially Fake/Malicious UPI ID")

import re

def is_valid_bitcoin_address(address):
    # Bitcoin addresses start with '1', '3', or 'bc1'
    if re.match(r'^[13][a-km-zA-HJ-NP-Z1-9]{25,34}$', address):
        return True
    return False

def is_valid_ethereum_address(address):
    # Ethereum addresses are 40 characters in length and start with '0x'
    if re.match(r'^0x[a-fA-F0-9]{40}$', address):
        return True
    return False

def crypto_address_scanner():
    st.title("Crypto Address Scanner")

    crypto_address = st.text_input("Enter Crypto Address:")
    if st.button("Scan"):
        valid_crypto = False

        # Check for common cryptocurrency address formats
        if is_valid_bitcoin_address(crypto_address):
            st.success("Valid Bitcoin Address")
            valid_crypto = True

        if is_valid_ethereum_address(crypto_address):
            st.success("Valid Ethereum Address")
            valid_crypto = True

        if not valid_crypto:
            st.error("Invalid Crypto Address")

# Add more cryptocurrency-specific checks if needed
# You can follow a similar pattern for other cryptocurrency addresses

def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["UPI ID Scanner", "Crypto Address Scanner"])

    if page == "UPI ID Scanner":
        upi_id_scanner()
    elif page == "Crypto Address Scanner":
        crypto_address_scanner()



def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["UPI ID Scanner", "Crypto Address Scanner"])

    if page == "UPI ID Scanner":
        upi_id_scanner()
    elif page == "Crypto Address Scanner":
        crypto_address_scanner()

if __name__ == "__main__":
    main()

c31,c11,c12 = st.columns([3,1,5])
c11.image("logo.png", width=200)
