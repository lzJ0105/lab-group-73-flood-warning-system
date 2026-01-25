from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance

def run():
    """Demonstration for task 1B"""

    # Get the list of all stations
    stations = build_station_list()
    cambridge_center = (52.2053, 0.1218)

    # Sort the stations by distance
    sorted_stations = stations_by_distance(stations, cambridge_center)

    # Print the 10 closest stations
    print("10 closest stations from Cambridge:")
    print("-----------------------------------")
    
    # We only want the first 10 items in the list
    first_10 = sorted_stations[:10]
    
    for entry in first_10:
        station = entry[0]
        dist = entry[1]
        print(station.name, dist)


    # 5. Print the 10 furthest stations
    print("\n10 furthest stations from Cambridge:")
    print("------------------------------------")
    
    last_10 = sorted_stations[-10:]
    
    for entry in last_10:
        station = entry[0]
        dist = entry[1]
        print(station.name, dist)


if __name__ == "__main__":
    print("*** Task 1B ***")
    run()