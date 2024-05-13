import streamlit as st
import pandas as pd
import time
import numpy as np
from io import StringIO

if 'df' not in st.session_state:
    st.session_state.df = pd.DataFrame()

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as bytes:
    # bytes_data = uploaded_file.getvalue()
    # st.write(bytes_data)

    # # To convert to a string based IO:
    # stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    # st.write(stringio)

    # # To read file as string:
    # string_data = stringio.read()
    # st.write(string_data)

    # Can be used wherever a "file-like" object is accepted:
    dataframe = pd.read_csv(uploaded_file)
    st.session_state.df = st.experimental_data_editor(dataframe, num_rows="dynamic")

 

# button = st.button("plot")
# if button:
chart = st.line_chart(st.session_state.df)
