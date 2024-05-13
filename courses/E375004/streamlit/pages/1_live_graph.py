import streamlit as st
import numpy as np
import pandas as pd
import time

st.set_page_config(
    page_title="Graph",
    page_icon=":chart_with_upwards_trend:",
    layout="wide",
    initial_sidebar_state="expanded",

)

progress_bar = st.sidebar.progress(0)
status_text = st.sidebar.empty()
# data = pd.DataFrame(np.array([0]))
data = pd.DataFrame([0.0], columns=["data"])
print(type(data))
print(data.size)
print(data)

chart = st.line_chart(data)

for i in range(1, 30):
    data = pd.DataFrame(data.values + np.random.randn(1),columns=["data"])
    print(type(data))
    print(data.size)
    print(data)
    status_text.text("%i%% Complete" % i)
    chart.add_rows(data)
    progress_bar.progress(i)
    last_rows = data
    time.sleep(0.5)

progress_bar.empty()

# Streamlit widgets automatically run the script from top to bottom. Since
# this button is not connected to any other logic, it just causes a plain
# rerun.
st.button("Re-run")