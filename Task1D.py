from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river

def run():
    """Demonstration for Task 1D"""

    # Build list of stations, get the set of rivers
    stations = build_station_list()
    rivers = rivers_with_station(stations)

    # Print total number of rivers and the first 10 rivers
    print(f"Number of rivers with at least one station: {len(rivers)}")

    print("\nFirst 10 rivers (alphabetically):")
    print("---------------------------------")
    
    # Convert set to a sorted list so it can be sliced
    sorted_rivers = sorted(rivers)
    
    for river in sorted_rivers[:10]:
        print(river)

    my_dict=stations_by_river(stations)
    river1='River Aire'
    river2='River Cam'
    river3='River Thames'
    lst1=my_dict[river1]
    lst2=my_dict[river2]
    lst3=my_dict[river3]
    print(sorted([station.name for station in lst1]))
    print(sorted([station.name for station in lst2]))
    print(sorted([station.name for station in lst3]))




if __name__ == "__main__":
    print("*** Task 1D ***")
    run()