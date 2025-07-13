import streamlit as st
import pandas as pd
import json
from helper_functions.utility import check_password  

# Check if the password is correct.  
if not check_password():  
    st.stop()

filepath = './data/courses-full.json'
with open(filepath, 'r') as file:
    json_string = file.read()
    dict_of_courses = json.loads(json_string)
    
df = pd.DataFrame(dict_of_courses).T.reset_index().drop(columns='index')

st.dataframe(df)
