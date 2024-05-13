import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk
import time


chart_data = pd.DataFrame(
   np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
   columns=['lat', 'lon'])

iss_data = pd.read_json("http://api.open-notify.org/iss-now.json")

print(iss_data.columns)
print(iss_data["iss_position"])
iss_df = pd.DataFrame({"longitude":[iss_data["iss_position"]["longitude"]],
                        "latitude":[iss_data["iss_position"]["latitude"]]})

if 'iss_df' not in st.session_state:
    st.session_state.iss_df = iss_df

button = st.button('update')
if button:
    iss_data = pd.read_json("http://api.open-notify.org/iss-now.json")
    st.session_state.iss_df = pd.concat([st.session_state.iss_df, pd.DataFrame({"longitude":[iss_data["iss_position"]["longitude"]],
                            "latitude":[iss_data["iss_position"]["latitude"]]})], ignore_index = True)


st.write("longitude", st.session_state.iss_df["longitude"].values[-1])    

chart = st.pydeck_chart(pdk.Deck(
    map_style=None,
    initial_view_state=pdk.ViewState(
        latitude=iss_data["iss_position"]["latitude"],
        longitude=iss_data["iss_position"]["longitude"],
        zoom=2,
        pitch=0,
    ),
    layers=[
        # pdk.Layer(
        #    'HexagonLayer',
        #    data=chart_data,
        #    get_position='[lon, lat]',
        #    radius=200,
        #    elevation_scale=4,
        #    elevation_range=[0, 1000],
        #    pickable=True,
        #    extruded=True,
        # ),
        pdk.Layer(
            'ScatterplotLayer',
            data=st.session_state.iss_df,
            get_position="[longitude, latitude]",
            get_color='[200, 30, 0, 160]',
            get_radius=100000,
        ),
    ],
))

@st.cache_data
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv(index=False).encode('utf-8')

csv = convert_df(st.session_state.iss_df)

st.download_button(
    label="Download data as CSV",
    data=csv,
    file_name='large_df.csv',
    mime='text/csv',
)


# for i in range(10):
#     time.sleep(0.1)

#     iss_data = pd.read_json("http://api.open-notify.org/iss-now.json")
#     st.session_state.iss_df = pd.concat([st.session_state.iss_df, pd.DataFrame({"longitude":[iss_data["iss_position"]["longitude"]],
#                             "latitude":[iss_data["iss_position"]["latitude"]]})], ignore_index = True)
    

# st.session_state.iss_df
