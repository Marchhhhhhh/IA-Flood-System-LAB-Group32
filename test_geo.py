from floodsystem.geo import stations_within_radius, rivers_with_stations, stations_by_river, stations_by_distance, rivers_by_station_number
from floodsystem.stationdata import build_station_list
from floodsystem.station import MonitoringStation

def create_test_monitoring_station(n):

    # Create a station
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
    
    centre = (2.0, 2.0)
    radius = 20000
    stations_for_test = []

    for i in range(3):
        stations_for_test.append(create_test_monitoring_station(i))
    
    assert stations_within_radius(stations_for_test, centre, radius) == ["Station 0", "Station 1", "Station 2"]
    

    

 

