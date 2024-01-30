import pandas as pd
import time
import streamlit as st
from streamlit_extras.stylable_container import stylable_container
import pandas as pd
from datetime import datetime, timedelta, time as t
import plotly.graph_objects as go
from numerize import numerize 

st.set_page_config(
    page_title="Stats till date",
    page_icon="✅",
    layout="wide"
)

st.write("""
<style>
    [data-testid="stMetric"] {
        border-radius: 15px;
        padding: 5% 5% 5% 10%;
    }
</style>
""", unsafe_allow_html=True)

st.title("Ather Statistics (till date)")

if not "time" in st.session_state:
    st.session_state.time = (datetime.now() - datetime.combine(datetime.now(), t.min)).seconds

with st.container():
    columns = st.columns(4)
    with columns[0]:
        with stylable_container(key="reg", 
                                css_styles=["""
                                [data-testid="stMetric"] {
                                    background-color: #565656;
                                }
                                """]):
            st.metric("Registered Scooters", "192,762")
    with columns[1]:
        with stylable_container(key="longest", 
                                css_styles=["""
                                [data-testid="stMetric"] {
                                    background-color: black;
                                }
                                """]):
            st.metric("Longest trip on one charge", "150 km")
    with columns[2]:
        with stylable_container(key="longestPublic", 
                                css_styles="""
                                [data-testid="stMetric"] {
                                    background-color: black;
                                }
                                """):
            st.metric("Longest ride with public charging in a day", "127 km")
    with columns[3]:
        with stylable_container(key="Saving", 
                                css_styles="""
                                [data-testid="stMetric"] {
                                    background-color: green;
                                }
                                """):
            st.metric("Total Savings", "₹ 257.56 Cr")

with st.container():
    columns = st.columns(3)
    with columns[0]:
        with stylable_container(key="dist", 
                                css_styles=["""
                                [data-testid="stMetric"] {
                                    background-color: black;
                                }
                                """]):
            st.metric("Total Distance Ridden", numerize.numerize(1855071707) + " km")
    with columns[1]:
        
        with stylable_container(key="reverse", 
                                css_styles="""
                                [data-testid="stMetric"] {
                                    background-color: black;
                                    color: green;
                                }
                                """):
            st.metric("Total Distance in Reverse", numerize.numerize(11195927))
    with columns[2]:
        with stylable_container(key="fastChargers", 
                                css_styles=["""
                                [data-testid="stMetric"] {
                                    background-color: black;
                                    color: #fade2a;
                                }
                                ""","""
                                [data-testid="stMetricLabel"] {
                                    display: flex; 
                                    justify-content: flex-end
                                }
                                """]):
            st.metric("Fast chargers", "1,840")

with st.container():
    columns = st.columns([2, 1])
    with columns[0]:
        with stylable_container(key="CO2", 
                            css_styles="""
                            [data-testid="stMetric"] {
                                background-image: url("https://c4.wallpaperflare.com/wallpaper/50/820/839/leaves-nature-vector-wallpaper-preview.jpg");
                                background-size: cover;
                            }
                            """):
            st.metric("Kilograms of CO₂ Saved", numerize.numerize(56640074985))  
    with columns[1]:
        with stylable_container(key="chargingSession", 
                                css_styles="""
                                [data-testid="stMetric"] {
                                    background-color: black;
                                    color: red;
                                }
                                """):
            st.metric("Total Number of Charging Session", numerize.numerize(66172555)) 