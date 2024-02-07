import streamlit as st 
from streamlit_option_menu import option_menu as opt  
st.set_page_config(page_title="About",page_icon="icon/mainmenu.png",layout='wide')

sty = """
            <style>
                .css-1629p8f.e16nr0p31{
                    text-align:center;
                }
            </style>
        """
st.markdown(f"{sty}",unsafe_allow_html=True)

with st.sidebar:
    selected = opt(
        menu_title='About',
        menu_icon='body-text',
        options=['Project','Team']
    )

if selected == 'Project':
    c1,c2,c3 = st.columns([4,1,5])
    c2.image("logo.png",width=250)
    st.write("""
## Product Perspective:
 Visecure is a comprehensive mobile application designed to empower users with cutting-edge security and privacy features, ensuring their digital well-being in an increasingly connected world. 
 It combines state-of-the-art technologies and a user-friendly interface to provide a one-stop solution for all their security needs.
## Product Features:

 * Malware Analysis: Scans both files and file-less malware to protect your device.\n
 * AI-Enabled Phishing Detection: Uses advanced AI algorithms to detect phishing attempts.\n
 * Spam Alert System: Crowd-sources inputs to verify the source of incoming calls, SMS, and emails.\n
 * Obscenity Blocker: Filters out inappropriate content from messages and websites.\n
 * Blockchain-Based Password Manager: Safely stores and manages passwords.\n
 * Real-time Fraud Indicator Flagging: Identifies and verifies calls, SMS, UPI IDs, and URLs in real-time.\n
 * Cybercrime Reporting: Allows users to report cybercrimes easily.\n

## User Classes and Characteristics:

 * General Users: Individuals concerned about their online security and privacy.\n
 * Business Users: Professionals and companies looking to secure their digital assets.\n
 * Parents: Concerned about their children's online safety.\n
 * Law Enforcement: Access to cybercrime reports and partnerships with local police.\n 
 * Cryptocurrency Enthusiasts: Use blockchain-based features for secure transactions.\n 
 * Frequent Travelers: Require VPN and secure communication abroad.\n 

## Special Features:
 * Blockchain Integration: Utilizes blockchain for added security and trust.
 * Crowdsourcing for Threat Detection: Harnesses the power of the community to identify threats.
 * Cybercrime Reporting & Emergency SOS Button: Provides a lifeline during critical situations & Allows users to report crimes easily..
 * Partnerships: Collaborates with government agencies and law enforcement.
 
""")

if selected == 'Team':
    sty = """
            <style>
                .css-1629p8f.e16nr0p31{
                    text-align:left;
                }
            </style>
        """
    st.markdown(f"{sty}",unsafe_allow_html=True)
    c11,c22 = st.columns([4,1])
    c11.title("Team Details")
    c22.image("startup.jpg",width=150)
    st.header("Team Description :")
    st.write("""
          
          Vision:

At Visecure, we envision a digital world where individuals and businesses can thrive without fear, where privacy and security are not luxuries but fundamental rights. Our vision is to lead the charge in revolutionizing digital security, creating a safer, more secure, and interconnected global community.

 Mission:

Our mission at Visecure is to empower every digital citizen with the tools and knowledge to protect their online identity and assets. We are on a relentless quest to build and advance innovative security solutions that are accessible, user-friendly, and effective. Our aim is to make the digital landscape a secure and inclusive space for all.
""")

    st.subheader("Team members : ")
    st.write("""
         * [Viyasan S - ( Team Leader )](https://www.linkedin.com/in/viyasan-sivaraj-12b14b1a4/)
         * [Swathi V - ( AI/ML Engineer)](https://www.linkedin.com/in/swathi-v-696329230/)
         * [Vishnu Balan O - ( UI/UX Designer)](https://www.linkedin.com/in/vishnu-into-ux-66014424b/)
         * [Abilash Kumar R - ( Blockchain Expert)](https://www.linkedin.com/in/abilash-kumar-r-3196a0268/)
    """)
