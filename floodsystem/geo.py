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
    stations = build_station_list()

    stations_within_range = []
    
    for i in range(len(stations)):
        distance = haversine(centre, stations[i].coord)

        if distance < r:
            stations_within_range.append(stations[i].name)
    
    return stations_within_range
