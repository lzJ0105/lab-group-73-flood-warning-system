from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold

def run():
    """Requirements for Task 2B"""

    # Build list of stations, update water levels (Must do to get current data), find stations over tol
    stations = build_station_list()

    update_water_levels(stations)

    tol = 0.8
    result_list = stations_level_over_threshold(stations, tol)

    # Print the top 10
    print(f"Stations with relative water level > {tol}")
    print("------------------------------------------")
    
    for entry in result_list[:10]:
        station = entry[0]
        level = entry[1]
        
        # Printing nicely with 2 decimal places
        print(f"{station.name} {level:.2f}")


if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    run()