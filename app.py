import pandas as pd
import time
import streamlit as st
from streamlit_extras.stylable_container import stylable_container
import pandas as pd
from datetime import datetime, timedelta, time as t
import plotly.graph_objects as go
from numerize import numerize 

@st.cache_data
def get_dist_today():
    return pd.read_csv("dist_ridden.csv")

@st.cache_data
def get_dist_today():
    return pd.read_csv("dist_ridden.csv")

st.set_page_config(
    page_title="Live Data for Today",
    page_icon="✅",
    layout="wide"
)

dist_ridden = get_dist_today()

st.write("""
<style>
    [data-testid="stMetric"] {
        border-radius: 15px;
        padding: 5% 5% 5% 10%;
    }
</style>
""", unsafe_allow_html=True)

st.title("Ather Statistics")

if not "time" in st.session_state:
    st.session_state.time = (datetime.now() - datetime.combine(datetime.now(), t.min)).seconds

with st.container():
    columns = st.columns(4)
    with columns[0]:
        with stylable_container(key="reg", 
                                css_styles=["""
                                [data-testid="stMetric"] {
                                    background-color: #565656;
                                    position: relative;
                                    z-index: 1;
                                }
                                """]):
            st.metric("Registered Scooters", "192,762")
    with columns[1]:
        with stylable_container(key="longest", 
                                css_styles=["""
                                [data-testid="stMetric"] {
                                    background-color: black;
                                    position: relative;
                                    z-index: 1;
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
            st.metric("Longest ride with public charging in a day", "456,797 km")
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
        if dist_ridden['total_distance'][st.session_state.time] < 1803650:
            gauge_color = '#1B8720'
        elif dist_ridden['total_distance'][st.session_state.time] < 3607300:
            gauge_color = '#FF9400'
        else:
            gauge_color = '#FF1708'
        fig = go.Figure(go.Indicator(
            mode = "gauge+number",
            value = int(dist_ridden['total_distance'][st.session_state.time]),
            domain = {'x': [0, 1], 'y': [0, 1]},
            number = {"suffix": " km", "valueformat": ",i"},
            title = {'text': "Distance Ridden Today"},
            gauge = {
                'axis': {'range': [0, 5465600]},
                'bar' : {'color': gauge_color},
            }
        ))
        fig.update_layout(
            autosize=False,
            margin=dict(l=15, r=15, t=0, b=150)
        )
        st.plotly_chart(fig, use_container_width=True)
    with columns[1]:
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
        with stylable_container(key="reverse", 
                                css_styles="""
                                [data-testid="stMetric"] {
                                    background-color: black;
                                    color: green;
                                }
                                """):
            st.metric("Total Distance in Reverse", numerize.numerize(11195927))
    with columns[2]:
        with stylable_container(key="MWh", 
                                css_styles=["""
                                [data-testid="stMetric"] {
                                    background: linear-gradient(120deg, rgb(246, 255, 5), rgb(255, 209, 56));
                                    color: black;
                                    text-align: right;
                                }
                                """, """
                                [data-testid="stMetricLabel"] {
                                    display: flex; 
                                    justify-content: flex-end
                                    color: black;
                                }
                                ""","""
                                [data-testid="stMarkdownContainer"] {
                                    color: black;
                                }]
                                ""","""
                                [data-testid="stVerticalBlock"] {
                                    gap: 0;
                                }
                                """]):
            st.metric("Total Energy Dispensed via Fast Charging", numerize.numerize(3037065) + "Wh")
        with stylable_container(key="chargingSession", 
                                css_styles="""
                                [data-testid="stMetric"] {
                                    background-color: black;
                                    color: red;
                                }
                                """):
            st.metric("Total Number of Charging Session", numerize.numerize(66172555))

with st.container():
    columns = st.columns([1, 2])
    with columns[0]:
        with stylable_container(key="liveCharging", 
                                    css_styles="""
                                    [data-testid="stMetric"] {
                                        background-color: black;
                                        color: green;
                                        margin-top: -168px;
                                    }
                                    """):
            st.metric("Total no of scooters getting juiced", numerize.numerize(290))
    with columns[1]:
       with stylable_container(key="CO2", 
                            css_styles="""
                            [data-testid="stMetric"] {
                                background-image: url("https://img.freepik.com/premium-photo/green-background-with-leafy-background_832479-5100.jpg");
                                background-size: cover;
                                margin-top: -210px;
                            }
                            """):
            st.metric("Kilograms of CO₂ Saved", numerize.numerize(56640074985))  
     

if not "sleep_time" in st.session_state:
    st.session_state.sleep_time = 2

if not "auto_refresh" in st.session_state:
    st.session_state.auto_refresh = True

#auto_refresh = st.sidebar.checkbox('Auto Refresh?', st.session_state.auto_refresh)

auto_refresh = True

if auto_refresh:
    number = st.session_state.sleep_time#st.sidebar.number_input('Refresh rate in seconds', value=st.session_state.sleep_time)
    st.session_state.sleep_time = number

if auto_refresh:
    time.sleep(number)
    st.session_state.time = st.session_state.time + 2
    st.rerun()