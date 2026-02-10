from floodsystem.station import inconsistent_typical_range_stations
from floodsystem.stationdata import build_station_list
def run():
    stations=build_station_list()
    lst=inconsistent_typical_range_stations(stations)
    lst_names = []
    for a in lst:
        lst_names.append(a.name)
    print(sorted(lst_names))
    
    

if __name__ == "__main__":
    run()