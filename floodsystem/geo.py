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
    stations = build_station_list()
    