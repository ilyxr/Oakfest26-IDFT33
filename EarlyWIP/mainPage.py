import streamlit as st
import pandas as pd 
import streamlit.components.v1 as components


bg_url = "/EarlyWIP/pages/bg.png"  
css = f"""
<link href="https://fonts.googleapis.com/css2?family=SUSE+Mono:ital,wght@0,100..800;1,100..800&display=swap" rel="stylesheet">
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
    background: rgba(0,0,25,0);
  }}
  .main > div {{ position: relative; z-index: 1; }}
  
  .stTextInput input {{
    background-color: rgba(0, 0, 0, 0) !important;
    border: 0px solid rgba(0, 0, 0, 0) !important;
    outline: 0px solid rgba(0, 0, 0, 0) !important;
    padding: 12px 20px !important;
    color: rgba(255, 255, 255, 0.9) !important;
    text-align: center !important;
    box-sizing: border-box !important;
  }}

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

st.markdown("<h1 style='font-size: 4rem; text-align: center; color: white; font-family: Tourney, monospace; padding: 67px'>t r i l u n a</h1>", unsafe_allow_html=True)

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