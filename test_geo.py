from turtle import st
from floodsystem.geo import stations_within_radius, rivers_with_stations, stations_by_river, stations_by_distance, rivers_by_station_number
from floodsystem.stationdata import build_station_list
from floodsystem.station import MonitoringStation

def create_test_monitoring_station(n):

    "A function which creates test monitoring station objects for use in other tests"

    # Create a test station (not real)
    s_id = "test-{}-id".format(n)
    m_id = "test-{}-id".format(n)
    label = "Station {}".format(n)
    coord = (-2.0*n, 4.0*n)
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


def test_stations_within_radius():
    
    "A test for the function used in Task1C.py called stations_within_radius"

    centre = (2.0, 2.0)
    radius = 20000
    stations_for_test = []

    for i in range(3):
        stations_for_test.append(create_test_monitoring_station(i))
    
    assert stations_within_radius(stations_for_test, centre, radius) == ["Station 0", "Station 1", "Station 2"]



def test_rivers_with_stations():

    "A test for the function used in Task1D.py called rivers_with_stations"

    stations_for_test = []

    for i in range(8):
        stations_for_test.append(create_test_monitoring_station(i))
    
    stations_for_test[0].river = "Amazon"
    stations_for_test[1].river = "Euphrates"
    stations_for_test[2].river = "Thames"
    stations_for_test[3].river = "Nile"
    stations_for_test[4].river = "Thames"
    stations_for_test[5].river = "Mississippi"
    stations_for_test[6].river = "Nile" 
    stations_for_test[7].river = "Thames" 

    a = sorted(rivers_with_stations(stations_for_test))

    assert a == ['Amazon', 'Euphrates', 'Mississippi', 'Nile', 'Thames']




