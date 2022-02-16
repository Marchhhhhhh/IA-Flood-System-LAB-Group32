# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data

"""


class MonitoringStation:
    """This class represents a river level monitoring station"""

    def __init__(self, station_id, measure_id, label, coord, typical_range,
                 river, town):

        self.station_id = station_id
        self.measure_id = measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self.name = label
        if isinstance(label, list):
            self.name = label[0]

        self.coord = coord
        self.typical_range = typical_range
        self.river = river
        self.town = town

        self.latest_level = None

    def __repr__(self):
        d = "Station name:     {}\n".format(self.name)
        d += "   id:            {}\n".format(self.station_id)
        d += "   measure id:    {}\n".format(self.measure_id)
        d += "   coordinate:    {}\n".format(self.coord)
        d += "   town:          {}\n".format(self.town)
        d += "   river:         {}\n".format(self.river)
        d += "   typical range: {}".format(self.typical_range)
        return d
    
    def typical_range_consistent(self):
        """Method which returns False if typical range data is inconsistent and True if it is consistent, from an object input"""

        if self.typical_range == None:
            return False
        elif self.typical_range[0] > self.typical_range[1]:
            return False
        else:
            return True

    def relative_water_level(self):
        try:
            a_0 = self.typical_range[0]
            a_1 = self.typical_range[1]
            result = 0
            if self.latest_level and a_1 > a_0:
                result = (self.latest_level - a_0)/(a_1-a_0)
            return result
        except:
            return None        



def inconsistent_typical_range_stations(stations):
    """Creates a list of station objects (MonitoringStation) which have inconsistent range data.
    
    Args: stations (list of MonitoringStation objects)
    
    Returns: inconsistent_stations (list of stations with inconsistent range data"""

    # Creates an empty list for stations with inconsistent range data.
    inconsistent_stations = []

    # adds stations with inconsistent range data to the list.
    for station in stations:
        if MonitoringStation.typical_range_consistent(station) == False:
            inconsistent_stations.append(station)

    return inconsistent_stations
