from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius

def run():
    """Demonstration for Task 1C"""

    # Build list of stations
    stations = build_station_list()

    cambridge_center = (52.2053, 0.1218)

    # Find stations within 10 km
    stations_in_10km = stations_within_radius(stations, cambridge_center, 10.0)


    print(f"Number of stations found: {len(stations_in_10km)}")
    print("--------------------------")
    
    for station in stations_in_10km:
        print(station.name)


if __name__ == "__main__":
    print("*** Task 1C ***")
    run()