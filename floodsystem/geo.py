# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
from floodsystem.stationdata import build_station_list
from .utils import sorted_by_key  # noqa

from haversine import haversine, Unit


# Building function for Task 1C
def stations_within_radius(stations, centre, r):
    """Creates a list of station objects within a given radius of a co-ordinate. Used in Task1C.py
    
    Args: stations (list of MonitoringStation objects), centre (tuple, lat-long co-ordinate), r (radius in km)
    
    Returns: stations_within_range (list of MonitoringStationObjects within the radius)"""

    # Create empty list to store names of stations within the radius
    stations_within_range = []
    
    # iterates through all stations, finding their distances (using .coord property) to centre using the haversine formula
    for item in stations:
        distance = haversine(centre, item.coord)

        # station object added to list if distance is within radius r
        if distance < r:
            stations_within_range.append(item)
    
    return stations_within_range


def rivers_with_stations(stations):
    """Creates a set of names of rivers which have at least one station. Used in Task1D.py
    
    Args: stations (list of MonitoringStation objects)

    Returns: rivers_monitored (set of names of rivers)"""
    
    # Create empty set to store the names of rivers monitored (set used to avoid duplicates)
    rivers_monitored = set()

    # station attribute river added to set for all stations in list
    for station in stations:
        rivers_monitored.add(station.river)
    
    return rivers_monitored



def stations_by_river(stations):
    """Creates a dictionary, using river names as keys to station objects on that river. Used in Task1D.py
    
    Args: stations (list of MonitoringStation objects)
    
    Returns: river_dict (dictionary with river names as keys to station objects"""

    # Create an empty dictionary
    river_dict = {}

    # If river already in the dictionary, add the station object to a list under that key
    for item in stations:
        if item.river in river_dict:
            river_dict[item.river].append(item)

    # If river not in dictionary, add a new entry with river as key and station object mapped by it
        else:
            river_dict[item.river] = [item]

    return river_dict




#Function for Task1B    
def stations_by_distance(stations, p):
    """Creating a list of stations, calculating distance between stations and certain points and rearranging using sort functions (only with respect to distance) to give output with n furthest/closest stations"""

    #Creating a list of stations (empty)
    final_list = []

    #Calculating distance between station and a certain point before creating a tuple
    for item in stations:
        distance = haversine(p, item.coord)
        distance_tuple = (item.name,item.town,distance)
        final_list.append(distance_tuple)

    #Sorting by distance
    final_list=sorted_by_key(final_list,2)

    return final_list



#Function needed for Task1E
def rivers_by_station_number(stations, N):
    """Creating tuples with rivers and numbers of stations they have, thus producing all rivers with n biggest number of stations"""

    #Importing stations and creating empty list and dictionary for storing rivers and station numbers
    stations = build_station_list()
    output = []
    river_numbers = {}

    #Adding number of stations into a set and counting till N
    for s in stations:
        if s.river in river_numbers.keys():
            river_numbers[s.river] += 1
        else:
            river_numbers.update({s.river:1})
    unique_nums = sorted(set(river_numbers.values()), reverse=True)[0:N]

    #Numbers of stations included in the n biggest number os stations 
    print(unique_nums)

    #Putting corresponding river names and numbers of stations in tuples
    for item in river_numbers:
        if river_numbers[item] in unique_nums:
            output.append((item, river_numbers[item]))
    output = sorted(output, key = lambda x: x[1], reverse = True)


    return output





   