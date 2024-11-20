

# Import Libraries
import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium # Plots folium map to the Streamlit app


st.image('pages/figures/californiamap.svg', use_column_width = True, 
         caption = "California Map")

if "user_data" in st.session_state:
    user_data = st.session_state["user_data"]
    st.write(user_data)