import datetime
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.plot import plot_water_level_with_fit

def run():
    """Requirements for Task 2F"""
    
    # Agains, Build list of stations and update water levels explicitly with currrent data
    stations = build_station_list()
    
    update_water_levels(stations)
    
    # Again, get the top 5 stations with highest relative water levels, using Task 2C Function
    top_5_stations = stations_highest_rel_level(stations, 5) 
    # Plot history for each station
    dt = 2   # Fetch data for past 2 days
    p = 4    # Polynomial degree 4
    
    print(f"Plotting polynomial fit (Degree {p}) for top 5 at-risk stations...")
    
    for entry in top_5_stations:
        # Task 2C returns a list of tuples (station, level),only need the station object (index 0) for here
        station = entry[0]
        
        # Fetch history
        dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
        
        # Only plot if have data
        if len(dates) > 0:
            print(f"Plotting {station.name}...")
            plot_water_level_with_fit(station, dates, levels, p)
        else:
            print(f"No history found for {station.name}")

if __name__ == "__main__":
    print("*** Task 2F: CUED Part IA Flood Warning System ***")
    run()