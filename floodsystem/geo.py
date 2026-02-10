# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
from math import radians, cos, sin, asin, sqrt

def haversine(coord1, coord2):
    """
    This function calculate the distance between two points on earth using the haversine formula.

    Args:
        coord1 (tuple): The first coordinate as (latitude, longitude)
        coord2 (tuple): The second coordinate as (latitude, longitude)

    Returns:
        float: the distance in kilometer
    """
    
    # Get the latitude and longitude from the inputs
    lat1 = coord1[0]
    lon1 = coord1[1]
    lat2 = coord2[0]
    lon2 = coord2[1]


    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)


    d_lat = lat2 - lat1
    d_lon = lon2 - lon1

    # Apply the haversine formula
    part1 = sin(d_lat / 2)**2
    part2 = cos(lat1) * cos(lat2) * sin(d_lon / 2)**2
    
    a = part1 + part2
    c = 2 * asin(sqrt(a))
    
    # Radius of the earth in km
    r = 6371
    
    # The final distance
    distance = c * r
    
    return distance


def stations_by_distance(stations, p):
    """
    This function sorts a list of stations by distance from a point p.

    Args:
        stations (list): A list of MonitoringStation objects
        p (tuple): The coordinate (latitude, longitude) we want to measure from

    Returns:
        list: A list of tuples. Each tuple looks like (station, distance).
              The list is sorted by distance (closest first).
    """
    
    # Create an empty list to store the results
    results = []
    
  
    for station in stations:
        
        distance = haversine(station.coord, p)
        entry = (station, distance)
        results.append(entry)
        
    # Now sort the list using the function 'sorted_by_key' given to us in utils.py.
    sorted_results = sorted_by_key(results, 1)
    
    return sorted_results


def stations_within_radius(stations, centre, r):
    """
    Returns a list of all stations within radius r of a geographic coordinate x.

    Args:
        stations (list): List of MonitoringStation objects
        centre (tuple): Coordinate (latitude, longitude) of the centre point
        r (float): Radius in kilometers

    Returns:
        list: List of MonitoringStation objects within the radius, sorted by name
    """
    
    # Create empty list to keep the matching stations
    matching_stations = []
    
    # Loop through all stations, calculate distance, check is distance < r
    for station in stations:

        dist = haversine(station.coord, centre)
        
        if dist < r:
            matching_stations.append(station)
            
    # Sort the list alphabetically by name using a lambda function shortcut
    matching_stations.sort(key=lambda x: x.name)
    
    return matching_stations





def rivers_with_station(stations):
    """
    Returns a set of river names (strings) that have at least one monitoring station.
    
    Args:
        stations (list): List of MonitoringStation objects
    
    Returns:
        set: A set of river names
    """

    # Create an empty set. 
    # Use a 'set' to automatically handle duplicates.

    rivers = set()
    
    #Loop through every station
    for station in stations:
        
        # Add the river name to the set
        if station.river:
            rivers.add(station.river)
            
    return rivers

def stations_by_river(stations):
    new_dict = {} #create a dictionary
    for station in stations:
        riv=station.river
        sta=station
        #check if river is in the dict
        if riv in new_dict:
            new_dict[riv].append(sta)
        #if not
        else:
            new_dict.setdefault(riv,[]).append(sta)
    return new_dict

def rivers_by_station_number(stations,N):
    list_num=[] #create a list to store the numbers of rivers
    dict_names=stations_by_river(stations)
    for key in dict_names:
        a=(key, len(dict_names[key]))
        list_num.append(a)
    #sort the list
    sorted_list=sorted(list_num, key=lambda x:x[1])
    list_N=sorted_list[-N:]
    for count in range(N+1,len(list_num)):
        if list_num[-count]==list_num[-(count-1)]:
            dict_N=sorted_list[-count:]
        else:
            break
    return(list_N)
    


       
