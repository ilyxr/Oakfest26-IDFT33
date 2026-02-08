import streamlit as st
import pandas as pd 

api_key="AIzaSyBfTeyoXqdKDTv-0S9auvehejBCMtrzaVQ" #ADD - ashleys code

import streamlit.components.v1 as components

api_key="AIzaSyBfTeyoXqdKDTv-0S9auvehejBCMtrzaVQ" #ADD - ashleys code

bg_url = "https://hitecher.com/storage/img/20190423/583ade3bcb4d91df0177.jpg"  
css = f"""
<style>
  .stApp {{
    background-image: url("{bg_url}");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
  }}
  .bg-overlay {{
    position: fixed; inset: 0; pointer-events: none; z-index: 0;
    background: rgba(0,5,75,0.25);
  }}
  .main > div {{ position: relative; z-index: 1; }}
</style>
<div class="bg-overlay"></div>
"""
st.markdown(css, unsafe_allow_html=True)

# what's padding i genuinely dk
st.write(" ") 
st.write(" ") 
st.write(" ") 
st.write(" ") 
st.write(" ") 
st.write(" ") 
st.write(" ") 
st.write(" ") 
st.write(" ") 
st.write(" ") 
st.write(" ") 
st.write(" ") 
st.write(" ") 
st.write(" ") 
st.write(" ") 
st.write(" ") 


st.markdown("<h1 style='text-align: center; color: white; font-family:monospace; padding: 67px'>t r i l u n a</h1>", unsafe_allow_html=True)

github_link = st.text_input(
    " ",
    placeholder = "enter link here",
    label_visibility = 'collapsed',
    key="placeholder",
)
if github_link: 
    with st.spinner("going through your hard work..."):
        # put the actual backend here 
        st.switch_page("resultsPage.py")
            
        
        
