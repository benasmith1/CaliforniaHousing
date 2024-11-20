
#Import necessary libraries
import streamlit as st
import pickle
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd



file_input = st.file_uploader("Upload file of penguin predictors")
if file_input:
    user_df = pd.read_csv(file_input)
    st.session_state["user_data"] = user_df
