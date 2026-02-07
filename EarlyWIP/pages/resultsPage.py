# results page 
import streamlit as st 
import pandas as pd 

# padding? nah 
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
st.write(" ") 
st.write(" ") 
st.write(" ") 

bg_url = "https://instagram.fblr20-2.fna.fbcdn.net/v/t1.15752-9/624576839_1959843261553319_717761765649431422_n.png?_nc_cat=104&_nc_cb=04374bf5-24e287ff&ccb=7-5&_nc_sid=fc17b8&efg=eyJxZV9ncm91cHMiOlsiaWdkX2Jlc3RfZWZmb3J0X2ltYWdlOnRlc3QiXX0%3D&_nc_ohc=qmWISgwWNh4Q7kNvwFVQ6N_&_nc_oc=AdlNWneZykDImYYMnykQpWpodj_cKyLE0f4G-sJqSWFdLuedungpqw9rxJlPoMIJ6nk&_nc_zt=23&_nc_ht=instagram.fblr20-2.fna&oh=03_Q7cD4gGNjK_fVDEG0Jdx5E70B9K0AM1VsQ3pEYN5uwBab8pRAA&oe=69AEB84E"  
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
    background: rgba(0,5,25,0.75);
  }}
  .main > div {{ position: relative; z-index: 1; }}
</style>
<div class="bg-overlay"></div>
"""
st.markdown(css, unsafe_allow_html=True)

st.subheader("Results")

df = pd.DataFrame(
    {
        "Problem": ["problem 1", "problem 2", "problem 3"],
        "Description": ["explanation 1", "explanation 2", "explanation 3"],
        "Priority": [5, 3, 1],
    }
)

st.dataframe(
    df,
    column_config={
        "Problem": st.column_config.Column(width="small"),
        "Description": st.column_config.Column(width="large"),
        "Priority": st.column_config.Column(width="small"),
    },
    use_container_width=True,
    hide_index=True,
)


st.write("Overall Rating:")
st.progress(67, text="67/100")