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

    for station in stations:
        if station.river in river_dict:
            river_dict[station.river].append(station.name)
            river_dict[station.river].sort()
        else:
            river_dict[station.river] = [station.name]

    return river_dict
    
