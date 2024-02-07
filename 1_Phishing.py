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

sl.set_page_config(page_title='Phishing Page Detection', page_icon = "hacker.png")

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

</style>
"""


sl.markdown(f"{style}",unsafe_allow_html=True)


title = 'Phishing Detection <span style="color:rgb(50,121,123)">(Visecure)</span>'

sl.markdown(f"<h1 style='text-align: center;'>{title}</h1>", unsafe_allow_html=True)

url = sl.text_input(" Enter Your Url :")

if  "https://" not in url:
    url = "https://" + url

if url != "":

    if sl.button('Scan'):
        # Send a GET request to the URL and get its HTML content
        try:
            response = requests.get(url)
            html = response.content
            result = 1

            # Use BeautifulSoup to parse the HTML content and extract features
            
        except:
            result = 0
        
        if result==1:
            soup = BeautifulSoup(html, 'html.parser')
            # Length of URL
            length_url = len(url)

            # Length of hostname
            hostname = tldextract.extract(url).domain
            length_hostname = len(hostname)

            # IP address (if available)
            try:
                ip = socket.gethostbyname(hostname)
            except socket.gaierror:
                ip = 0

            # Number of dots in the URL
            nb_dots = url.count('.')

            # Number of question marks in the URL
            nb_qm = url.count('?')

            # Number of equal signs in the URL
            nb_eq = url.count('=')

            # Number of slashes in the URL
            nb_slash = url.count('/')

            # Number of "www" in the URL
            nb_www = url.count('www')

            # Ratio of digits in the URL
            ratio_digits_url = sum(c.isdigit() for c in url) / len(url)

            # Ratio of digits in the hostname
            ratio_digits_host = sum(c.isdigit() for c in hostname) / len(hostname)

            # TLD in subdomain (1 if yes, 0 if no)
            tld_in_subdomain = int(tldextract.extract(url).subdomain.count('.') > 0)

            # Prefix or suffix in the hostname (1 if yes, 0 if no)
            prefix_suffix = int(bool(hostname.startswith('www.') or hostname.endswith('.com')))

            # Shortest word in the hostname
            shortest_word_host = min(len(word) for word in hostname.split('.'))
            
            # Longest words in the URL, raw HTML, and path
            try:
                longest_words_raw = max(len(word) for word in soup.get_text().split())
                longest_word_path = max(len(word) for word in url.split('/'))
            except:
                longest_words_raw = 0
                longest_word_path = 0
                
            # Phishing hints (1 if present, 0 if not)
            phish_hints_list = ['login', 'signin', 'verify', 'banking', 'password', 'security', 'update', 'support']
            phish_hints = 0
            for i in phish_hints_list:
                if i in url:
                    phish_hints = i
                    break
            # Number of hyperlinks on the page
            try:
                nb_hyperlinks = len(soup.find_all('a'))
            except:
                nb_hyperlinks = 0
            # Ratio of internal hyperlinks (pointing to the same domain)
            domain = tldextract.extract(url).registered_domain
            
            try:
                internal_links = [link.get('href') for link in soup.find_all('a') if tldextract.extract(link.get('href')).registered_domain == domain]
            except:
                internal_links = '0'
            if nb_hyperlinks!=0:
                ratio_intHyperlinks = len(internal_links) / nb_hyperlinks
            else:
                ratio_intHyperlinks = 0
            # Empty title tag (1 if yes, 0 if no)
            try:
                empty_title = int(bool(soup.title.string))
            except:
                empty_title=0
            
            try:    
                # Domain name in the title tag (1 if yes, 0 if no)
                domain_in_title = int(bool(domain in soup.title.string))
            except:
                domain_in_title = 0
            # Domain age (if available)
            try:
                whois = whois.whois(url)
                if 'creation_date' in whois:
                    domain_age = (datetime.now().date() - whois['creation_date'].date()).days
                else:
                    domain_age = 0
            except:
                domain_age=0

            # Google index status (1 if indexed, 0 if not)
            try :
                google_index = int('google.com' in requests.get(f"https://www.google.com/search?q={url}").text)
            except :
                google_index = 0
            # Page rank (if available)
            try:
                page_rank = google_pagerank(url)
            except:
                page_rank = 0
            
            
            input_df = pd.DataFrame(
                {
                'length_url' : [length_url],
                'length_hostname' : [length_hostname], 
                'ip':[ip], 
                'nb_dots':[nb_dots], 
                'nb_qm':[nb_qm], 
                'nb_eq':[nb_eq],
                'nb_slash':[nb_slash], 
                'nb_www':[nb_www], 
                'ratio_digits_url':[ratio_digits_url], 
                'ratio_digits_host':[ratio_digits_host],
                'tld_in_subdomain':[tld_in_subdomain], 
                'prefix_suffix':[prefix_suffix], 
                'shortest_word_host':[shortest_word_host],
                'longest_words_raw':[longest_words_raw],
                'longest_word_path':[longest_word_path], 
                'phish_hints':[phish_hints],
                'nb_hyperlinks':[nb_hyperlinks], 
                'ratio_intHyperlinks':[ratio_intHyperlinks], 
                'empty_title':[empty_title],
                'domain_in_title':[domain_in_title], 
                'domain_age':[domain_age], 
                'google_index':[google_index], 
                'page_rank':[page_rank]
            }
            )
            
            result = pipe.predict(input_df)
            
            print(input_df)
        print("\n\n\n",result)
        if result==1:
            sl.success("The website look's clean", icon="✅")
        else:
            sl.error("  The website look's suspicious", icon="🚨")
            

with sl.expander("About"):
    c3,c1,c2 = sl.columns([3,1,5])
    c1.image("logo.png", width=200)
    sl.write("###")
    sl.header(":blue[Description :]")
    sl.write("""
    Team Name - Startup Pro - [ Team Head - Viyasan S ( CEO ) ]
1. S. Viyasan - Project Manager and Lead Developer: responsible for leading the project and managing the team's workflow, setting timelines and goals, and overseeing the development of the Visecure Application.\n
2. V. Swathi - Data Scientist and Machine Learning Expert: responsible for designing and implementing the machine learning algorithms that will be used to detect phishing pages, as well as analyzing data and making recommendations for improving the system.\n
3. O. Vishnubalan - Front-end Developer and UI/UX Designer: responsible for designing and implementing the user interface for the phishing page detection system, making it intuitive and user-friendly.\n
4. R. Abilash Kumar - Back-end Developer and Blockchain Expert: responsible for designing and implementing the back-end infrastructure for the system, including the database and server-side functionality.\n
    """)
    sl.write("###")
    sl.write("###")
    
c31,c11,c12 = sl.columns([3,1,5])
c11.image("logo.png", width=200)
