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
    "A function which given an input of a list of stations (Type Monitoring Station), a centre co-ordinate and a radius, returns all station names within the radius of the centre."

    stations_within_range = []
    # Create empty list to store names of stations within the radius
    
    # iterates through all stations, finding their distances (using .coord property) to centre using the haversine formula
    for item in stations:
        distance = haversine(centre, item.coord)

        if distance < r:
            stations_within_range.append(item)
    
    return stations_within_range


def rivers_with_stations(stations):
    "A function which given a list of stations, creates a set of rivers with at least on monitroing station."

    rivers_monitored = set()

    for station in stations:
        rivers_monitored.add(station.river)
    
    return rivers_monitored



def stations_by_river(stations):
    "A function which given a list of stations, creates a dictionary mapping a river to a list of stations monitoring that river"

    river_dict = {}

    for item in stations:
        if item.river in river_dict:
            river_dict[item.river].append(item)
            
        else:
            river_dict[item.river] = [item]

    return river_dict

#Function for Task1B    
def stations_by_distance(stations, p):

    #Creating a list of stations
    final_list = []

    for item in stations:
        distance = haversine(p, item.coord)
        distance_tuple = (item.name,item.town,distance)
        final_list.append(distance_tuple)

    #Sorting by distance
    final_list=sorted_by_key(final_list,2)

    return final_list

#Function needed for Task1E

def rivers_by_station_number(stations, N):
    output = []
    river_numbers = []
    for s in stations:
        if s.river in river_numbers.keys():
            river_numbers[s.river] += 1
        else:
            river_numbers.update({s.river:1})
    unique_nums = sorted(set(river_numbers.values()), reverse=True)[0:N]
    for item in river_numbers:
        if river_numbers[item] in unique_nums:
            output.append([item, river_numbers[item]])
    output = sorted(output, key = lambda x: x[1], reverse = True)
    return output





   