# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""

from floodsystem.station import MonitoringStation, inconsistent_typical_range_stations


def test_create_monitoring_station(n):

    # Create a station
    s_id = "test-{}-id".format(n)
    m_id = "test-{}-id".format(n)
    label = "Station {}".format(n)
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    assert s.station_id == s_id
    assert s.measure_id == m_id
    assert s.name == label
    assert s.coord == coord
    assert s.typical_range == trange
    assert s.river == river
    assert s.town == town

    return s


def test_inconsistent_typical_range_stations():

    "A test for the function used in Task1F.py called inconsistent_typical_range"

    stations_for_test = []

    for i in range(4):
        stations_for_test.append(test_create_monitoring_station(i))
    
    stations_for_test[0].typical_range = (-2.3, 3.4445)
    stations_for_test[1].typical_range = (5, 3)
    stations_for_test[2].typical_range = None
    stations_for_test[3].typical_range = (2, 3)

    a = inconsistent_typical_range_stations(stations_for_test)
    
    b = []

    for item in a:
        b.append(item.name)
    
    assert b == ["Station 1", "Station 2"]


