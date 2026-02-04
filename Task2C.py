from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level

def run():
    """Requirements for Task 2C"""

    stations = build_station_list()
    update_water_levels(stations)

    N = 10
    high_risk_list = stations_highest_rel_level(stations, N)

    #Print them
    print(f"Top {N} stations with highest relative water levels:")
    print("----------------------------------------------------")
    
    for entry in high_risk_list:
        station = entry[0]
        level = entry[1]
        
        print(f"{station.name} {level:.2f}")


if __name__ == "__main__":
    print("*** Task 2C: CUED Part IA Flood Warning System ***")
    run()