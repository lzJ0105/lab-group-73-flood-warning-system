import streamlit as st
import pandas as pd
import datetime

from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.datafetcher import fetch_measure_levels

# Set up the page title
st.set_page_config(page_title="Flood Warning System", page_icon="🌊")
st.title("🌊 Real-Time Flood Warning System")
st.write("Welcome to the CUED Part IA Flood Warning System Web Interface By Lab Group 73.")

# Data Loading
# @st.cache_data tells Streamlit to only load this once, so app don't freeze every time a button is clicked
@st.cache_data
def load_data():
    stations = build_station_list()
    update_water_levels(stations)
    return stations

st.sidebar.header("System Status")
with st.spinner("Fetching live data from Environment Agency..."):
    stations = load_data()
st.sidebar.success(f"System Online: Tracking {len(stations)} stations.")



# FUNCTION 1: View Top N At-Risk Stations

st.header("1. Stations Most at Risk")
st.write("Use the slider to select how many high-risk stations you want to see.")

# An interactive slider
N = st.slider("Number of stations:", min_value=1, max_value=20, value=5)

# Get the data using Task 2C function
top_stations_tuples = stations_highest_rel_level(stations, N)

# Format it
table_data = []
for entry in top_stations_tuples:
    station = entry[0]
    level = entry[1]
    table_data.append({"Station Name": station.name, "Town": station.town, "Relative Water Level": round(level, 2)})

st.table(pd.DataFrame(table_data))


# FUNCTION 2: Interactive Water Level Graph
st.header("2. Live Water Level History")
st.write("Select a station from the high-risk list above to view its 2-day history.")

# An interactive dropdown menu
station_names = [entry[0].name for entry in top_stations_tuples]
selected_name = st.selectbox("Choose a station to plot:", station_names)

# Find the station object that matches the name
selected_station = next(entry[0] for entry in top_stations_tuples if entry[0].name == selected_name)

if st.button("Fetch and Plot Data"):
    with st.spinner(f"Downloading history for {selected_name}..."):
        # Fetch 2 days of history
        dates, levels = fetch_measure_levels(selected_station.measure_id, dt=datetime.timedelta(days=2))
        
        if len(dates) > 0:
            # Create a dataframe for the graph, draw chart, show typical range below graph
            chart_data = pd.DataFrame({"Water Level (m)": levels}, index=dates)
            
            st.line_chart(chart_data)
        
            st.info(f"**Typical Range for {selected_name}:** {selected_station.typical_range[0]}m to {selected_station.typical_range[1]}m")
        else:
            st.error("No historical data available for this station right now.")