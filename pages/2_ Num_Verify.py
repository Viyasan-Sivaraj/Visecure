import streamlit as sl
import pickle
import requests
import tldextract
from bs4 import BeautifulSoup
import tldextract
import socket
import whois
from datetime import datetime
from googlesearch import search
import pandas as pd
import bz2file as bz2
import re

sl.set_page_config(page_title='Mobile Spam Detection', page_icon = "hacker.png")

data = bz2.BZ2File('model2.pbz2', 'rb')
pipe = pickle.load(data)

style = """
<style>
.stButton > button{
    all : unset;
    padding: 5px 40px;
    border : 1px solid;
    border-radius: 17px 0 17px 0;
    transition: 0.5s ease-in-out;
    color: #a0a0a0;
}

.stButton > button:hover{
    all : unset;
    padding: 5px 40px;
    border : 1px solid;
    border-radius: 0px 17px 0px 17px;
    transition: 0.5s ease-in-out;
}
.stButton > button:focus:not(:active){
    all : unset;
    padding: 5px 40px;
    border : 1px solid;
    border-radius: 10px 10px 10px 10px;
    transition: 0.5s ease-in-out;
}
.stButton > button:focus{
    all : unset;
    padding: 5px 40px;
    border : 1px solid;
    border-radius: 10px 10px 10px 10px;
    transition: 0.5s ease-in-out;
}
.streamlit-expanderHeader:hover{
    color: rgb(96, 180, 255);
}
.css-1fcdlhc .streamlit-expanderHeader:hover svg{
    fill:rgb(96, 180, 255);
}
.st-ck:hover,.st-ck:focus{
    border: rgb(96, 180, 255);
}
<style>
"""

sl.markdown(f"{style}",unsafe_allow_html=True)


title = 'Visecure'


sl.markdown("""
<style>
/* Apply styles to the "section-basic" class */
.section-basic {
    padding: 20px;
}

.h1-subline {
    font-size: 18px;
    color: #ff9933;
}

.well {
    border: 1px solid ;
    border-radius: 15px;
    padding: 15px;
}

.container{
    padding: 20px;
    border-radius: 15px;
    border: 1px solid;
}

/* Apply styles to the "zusammenfassung-serioesitaet" class */
.zusammenfassung-serioesitaet {
    background-color: #4caf50; /* Green background color */
    color: #fff; /* White text color */
}

/* Add any additional styles you want for other elements with their respective classes */

</style>
""", unsafe_allow_html=True)

sl.markdown(f"<h1 style='text-align: center;color:rgb(50,121,123);'>{title}</h1>", unsafe_allow_html=True)

def num(number):
    url = f"https://spamcalls.net/en/search?q={number}"
    r = requests.get(url)
    if r.status_code == 200:
        return r.text
    else:
        return "Error"


def main():
    sl.title("Number Verification")
    sl.markdown("""
    <div id="rating">
    </div>
    """,unsafe_allow_html=True)
    number = sl.text_input("Enter the mobile number")
    if sl.button("Verify"):
        report = num(number)
        if report == "Error":
            sl.error("Error occured")
        else:
            pattern = r'<div class="main main-raised">(.+?)</div>'

            # Use re.search to find the first match
            match = re.search(pattern, report, re.DOTALL)

            # Extract the matched content
            if match:
                extracted_content = match.group(1)
                sl.header(":blue[Report]")
                modified_content = re.sub(r'<a href="#ratings">', '', extracted_content)
                output_string = re.sub(r'<i[^>]*>.*?</i>', '', modified_content)
                sl.markdown(f"{output_string}", unsafe_allow_html=True)
                if "Medium" in extracted_content:
                    sl.markdown("""
                    <style>                  
                    .well {
                        border: 1px solid ;
                        border-radius: 15px;
                        padding: 15px;
                        background-color: #ff9933;
                    }
                    </style>
                    """, unsafe_allow_html=True)
                if "High" in extracted_content:
                    sl.markdown("""
                    <style>
                    .well {
                        border: 1px solid ;
                        border-radius: 15px;
                        padding: 15px;
                        background-color: rgba(255,0,0,0.7);
                    }
                    </style>
                    """, unsafe_allow_html=True)
                if "Low" in extracted_content:
                    sl.markdown("""
                    <style>
                    .well {
                        border: 1px solid ;
                        border-radius: 15px;
                        padding: 15px;
                        background-color: rgba(76,175,80,0.7);
                    }

                    </style>
                    """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()

with sl.expander("About"):
    c3,c1,c2 = sl.columns([3,1,5])
    c1.image("logo.png", width=200)
    sl.write("###")
    sl.header(":blue[Description :]")
    sl.write("""
  Team Name - Startup Pro - [ Team Head - Viyasan S ( CEO ) ]
1. S. Viyasan - Project Manager and Lead Developer: responsible for leading the project and managing the team's workflow, setting timelines and goals, and overseeing the development of the Visecure Application\n
2. V. Swathi - Data Scientist and Machine Learning Expert: responsible for designing and implementing the machine learning algorithms that will be used to detect phishing pages, as well as analyzing data and making recommendations for improving the system.\n
3. O. Vishnubalan - Front-end Developer and UI/UX Designer: responsible for designing and implementing the user interface for the phishing page detection system, making it intuitive and user-friendly.\n
4. R. Abilash Kumar - Back-end Developer and Blockchain Expert: responsible for designing and implementing the back-end infrastructure for the system, including the database and server-side functionality.\n
    """)
    sl.write("###")
    sl.write("###")
    
c31,c11,c12 = sl.columns([3,1,5])
c11.image("logo.png", width=200)
