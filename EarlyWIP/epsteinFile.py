import streamlit as st
import pandas as pd 

st.title("name of the project (i forgor)")

def page1(): 
    st.write("Please enter your Github File's link")
    github_link = st.text_input("Github File Link: ", key="github_link") 
    if st.button("Submit", key="submit_button"):
        st.write("You entered: ", github_link)
        # the function would be called right HERE 
        # st.spinner() 
        # st.success("Analysis complete!") 
        # st.button("Go to Results", key="go_to_results_button")
        # if st.button("Go to Results", key="go_to_results_button"):
        #   st.switch_page("Page2")
        
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