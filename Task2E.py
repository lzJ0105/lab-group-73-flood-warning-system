import datetime
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.plot import plot_water_levels

def run():
    """Requirements for Task 2E"""
    
    # 1. Build list of stations and explicitly call to update water levels
    stations = build_station_list()
    
    update_water_levels(stations)
    
    # Get Top 5 stations by reusing function from task 2C
    top_5_stations = stations_highest_rel_level(stations, 5)
    
    # Loop through each station and plot
    dt = 10
    
    for entry in top_5_stations:
        # stations_highest_rel_level returns list of (station, level) tuples
        station = entry[0] 
        
        print(f"Plotting data for {station.name}...")
        
        # fetch history
        dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
        
        # Plot
        # Check if actually have data before plotting
        if len(dates) > 0:
            plot_water_levels(station, dates, levels)
        else:
            print(f"No history found for {station.name}")

if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()