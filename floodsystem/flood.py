from .utils import sorted_by_key
from floodsystem.station import MonitoringStation

def stations_level_over_threshold(stations, tol):
    final_list = []
    for item in stations:
        a = item.relative_water_level()
        if isinstance(a, int) or isinstance(a, float):
            if a > tol and a < 100:
                final_list.append((item, a))
                
    
    a = sorted_by_key(final_list, 1, reverse=True)
    return a



def stations_highest_rel_level(stations, N):

    """Creates list of the N station objects (Type MonitoringStation) with the greatest relative water levels, sorted in order.
    
    Args: stations (list of objects), N (number of stations to return)
    
    Returns: output (list of top N relative water level stations) """

    #Create empty list
    stations_for_ordering = []
    
    #Filter out stations with no relative water levels up to date, or an infeasible (broken) value
    for station in stations:
        if station.relative_water_level() != None and station.relative_water_level() < 50:
            stations_for_ordering.append(station)
    
    #Sort these stations by their relative water levels
    output = sorted(stations_for_ordering, key = lambda x: x.relative_water_level(), reverse = True)

    #Return the first N items of the sorted list
    return output[:N]
