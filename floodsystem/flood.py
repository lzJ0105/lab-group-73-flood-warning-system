from .utils import sorted_by_key

def stations_level_over_threshold(stations, tol):
    """
    Returns a list of tuples (station, relative_level) where the relative level
    is above the tolerance (tol).
    
    Args:
        stations (list): List of MonitoringStation objects
        tol (float): Tolerance level (e.g., 0.8)
        
    Returns:
        list: List of (station, relative_level) sorted by relative_level (descending)
    """
    
    output_list = []
    
    for station in stations:
        
        # Check if the station has valid data
        # Must have "typical_range" and "latest_level" to do any calculations
        # Also use the helper method .typical_range_consistent() from Task 1A
        if not station.typical_range_consistent():
            continue
            
        if station.latest_level is None:
            continue
            
        #Get the numbers needed for the calculation
        current_level = station.latest_level
        low_level = station.typical_range[0]
        high_level = station.typical_range[1]
        
        # Calculate relative level
        # Formula: (current - low) / (high - low)
        
        range_diff = high_level - low_level
        
        # Avoid dividing by zero if high and low are the same
        if range_diff == 0:
             continue
             
        relative_level = (current_level - low_level) / range_diff
        
        # Check against the (tol)
        if relative_level > tol:
            output_list.append((station, relative_level))
            
    # Sort the list
    # Want the highest water level first (descending order), sorted_by_key sorts ascending by default, so use reverse=True
    # The relative_level is the second item in the tuple (index 1)
    sorted_list = sorted_by_key(output_list, 1, reverse=True)
    
    return sorted_list



def stations_highest_rel_level(stations, N):
    """
    Returns a list of the N stations with the highest relative water levels.
    
    Args:
        stations (list): List of MonitoringStation objects
        N (int): The number of stations to return
        
    Returns:
        list: List of tuples (MonitoringStation, relative_level), sorted descending
    """
    
    # Create a list to store all valid stations and their levels
    stations_with_levels = []
    
    for station in stations:
        
        # Check consistency
        if not station.typical_range_consistent():
            continue
            
        if station.latest_level is None:
            continue
            
        # Calculate relative level
        low = station.typical_range[0]
        high = station.typical_range[1]
        diff = high - low
        
        if diff == 0:
            continue
            
        rel_level = (station.latest_level - low) / diff
        
        # Add to list
        stations_with_levels.append((station, rel_level))
        
    # Sort the list by level (index 1), descending
    sorted_stations = sorted_by_key(stations_with_levels, 1, reverse=True)
    
    # Return the top N tuples directly
    return sorted_stations[:N]