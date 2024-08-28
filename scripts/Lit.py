import streamlit as st
import pandas as pd
from Parser import populate_df

df = populate_df()


st.title("tableaux des items")

st.dataframe(df)