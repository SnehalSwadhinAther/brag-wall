import streamlit as st
from streamlit_extras.stylable_container import stylable_container
import pandas as pd
import math

millnames = ['',' k',' Mn',' Bn',' Tn']

def millify(n):
    n = float(n)
    millidx = max(0,min(len(millnames)-1,
                        math.floor(0 if n == 0 else math.log10(abs(n))/3)))
    x = str(round(n / 10**(3 * millidx), 2))
    return (x[:-2] if x[-2:] == ".0" else x) + millnames[millidx]

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

st.title("Ather Stats - Lifetime")

with st.container():
    columns = st.columns(3)
    with columns[0]:
        with stylable_container(key="reg", 
                                css_styles=["""
                                [data-testid="stMetric"] {
                                    background-color: #565656;
                                }
                                """]):
            st.metric("Total Registered Scooters", "1,94,441")
    with columns[1]:
        with stylable_container(key="longest", 
                                css_styles=["""
                                [data-testid="stMetric"] {
                                    background-color: black;
                                }
                                """]):
            st.metric("Longest trip on one charge", "150 km")
    with columns[2]:
        with stylable_container(key="Saving", 
                                css_styles="""
                                [data-testid="stMetric"] {
                                    background-color: green;
                                }
                                """):
            st.metric("Total Savings", "₹ 265.85 Cr")

with st.container():
    columns = st.columns(3)
    with columns[0]:
        with stylable_container(key="dist", 
                                css_styles=["""
                                [data-testid="stMetric"] {
                                    background-color: black;
                                }
                                """]):
            st.metric("Total Distance Covered", millify(1869134161) + " km")
    with columns[1]:
        
        with stylable_container(key="reverse", 
                                css_styles="""
                                [data-testid="stMetric"] {
                                    background-color: black;
                                    color: green;
                                }
                                """):
            st.metric("Park Assistance / Reverse Distance", millify(11368573) + " km")
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
            st.metric("Fast Charging Stations", "2000+")

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
            st.metric("Total CO₂ Emissions Saved", millify(57662570726) + " kg")  
    with columns[1]:
        with stylable_container(key="chargingSession", 
                                css_styles="""
                                [data-testid="stMetric"] {
                                    background-color: black;
                                    color: red;
                                }
                                """):
            st.metric("Total Charging Sessions", millify(67261182)) 