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
    for i in range(len(stations)):
        distance = haversine(centre, stations[i].coord)

        if distance < r:
            stations_within_range.append(stations[i].name)
    
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
            river_dict[item.river].append(item.name)
            river_dict[item.river].sort()
        else:
            river_dict[item.river] = [item.name]

    return river_dict
    
def stations_by_distance(stations, p):
    final_list = []
    for item in stations:
        distance = haversine(p, item.coord)
        distance_tuple = (item.name,item.town,distance)
        final_list.append(distance_tuple)
    final_list=sorted_by_key(final_list,2)
    return final_list
