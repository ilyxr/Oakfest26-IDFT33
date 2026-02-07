
# results page 
import streamlit as st 
import pandas as pd 

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