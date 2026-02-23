from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold
from floodsystem.analysis import polyfit
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.station import inconsistent_typical_range_stations
import datetime
import matplotlib

#the risk of a town depends on the riskest station.
#relative value>1: increasing--severe(4), decreasing--high(3)
#1>=relative value>0.5 moderate(2)
#relative value<=0.5 low(1)
def warning_for_towns():
    stations=build_station_list()
    # Update latest level data for all stations
    update_water_levels(stations)
    # for station in stations:
    #     if station.name == "Thornborough":
    #         stations.remove(station)
    

    my_dic={}
    #severe and high
    risk34=stations_level_over_threshold(stations,1)
    
    dt=14 #make prediction based on past 2 weeks
    for sta, rl in risk34:
        dates, levels = fetch_measure_levels(sta.measure_id, dt=datetime.timedelta(days=dt))

        if len(dates) > 0:
            #print(levels)
            #print(sta.name)
            #print(levels)
            poly, d0=polyfit(dates,levels,3)
            num=matplotlib.dates.date2num(dates)
            #print(num)
            predicted=poly(num[-1]+1-d0)  #the predicted waterlevel of the nect day

            if predicted>levels[-1]: #incresing,severe,4
                my_dic[sta.town]=4
                
            else: #high,3
                if sta.town in my_dic and my_dic[sta.town]>=3:
                    pass
                else:
                    my_dic[sta.town]=3
        else:
            print(f"No history found for {sta.name}")
    #moderate
    temp_risk2=stations_level_over_threshold(stations,0.5)
    risk2=list(set(temp_risk2)-set(risk34))
    for sta, rl in risk2:
        if sta.town in my_dic and my_dic[sta.town]>=2:
            pass
        else: my_dic[sta.town]=2
    #low
    temp_risk1=[tup[0] for tup in temp_risk2] # a list of all stations whose relative level are larger than 0.5
    risk1=list(set(stations)-set(temp_risk1))
    for sta in risk1:
        if sta.town in my_dic and my_dic[sta.town]>=1:
            pass
        else: my_dic[sta.town]=1
    #print(my_dic)
    severe_lst=[key for key, val in my_dic.items() if val==3]
    print(severe_lst)
    #python return severe_lst, my_dic
    
if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    warning_for_towns()


    

