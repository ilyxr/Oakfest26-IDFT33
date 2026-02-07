import streamlit as st
import pandas as pd 
import streamlit.components.v1 as components

st.markdown("""
<style>
.stTextInput input[aria-label="Transparent input"] {
    background-color: transparent;
    border: none;
    color: inherit;
}
</style>
""", unsafe_allow_html=True)
st.write(" ") 
st.write(" ") 
st.write(" ") 
st.write(" ") 
st.write(" ") 

st.markdown("<h1 style='text-align: center; color: white; font-family:monospace; padding: 160px'>t r i l u n a</h1>", unsafe_allow_html=True)
def page1(): 
    github_link = st.text_input(
        " ",
        placeholder = "enter a github link",
        label_visibility = 'collapsed',
        key="placeholder",
    )
        
        
def page2(): 
    st.write("Here are the results of the analysis: ")
    col1, col2 = st.columns(2) 
    
    with col1: 
        st.write(
            pd.DataFrame(
                {
                    "Problem": ["problem 1", "problem 2", "problem 3"],
                    "Description": ["explanation 1", "explanation 2", "explanation 3"],
                }
            ))
        
    with col2: 
        st.write("Overall Rating:")
        st.progress(80, text="4/5")
    
pg = st.navigation([
    st.Page(page1, title="Enter Link"),
    st.Page(page2, title="Results") 
], position="hidden")
pg.run()