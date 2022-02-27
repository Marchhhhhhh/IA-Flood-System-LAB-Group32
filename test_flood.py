from floodsystem.utils import sorted_by_key
from floodsystem.station import MonitoringStation
from floodsystem.flood import stations_level_over_threshold

def create_test_monitoring_station(n):

    "A function which creates test monitoring station objects for use in other tests"

    # Create a test station (not real)
    s_id = "test-{}-id".format(n)
    m_id = "test-{}-id".format(n)
    label = "Station {}".format(n)
    coord = (-2.0*n, 4.0*n)
    trange = (0.1*n, 1.1*n)
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

#result = []
#def test_stations_level_over_threshold():
#    stations_for_test = []
#    for n in range(4):
#        stations_for_test.append(create_test_monitoring_station(n))
 #   a = stations_level_over_threshold(stations_for_test, 0.01)
#
 #   for station in a:
 #       global result 
  #      result.append("{} {}".format(station[0].name, station[1]))
  #  a = result
#   assert a == 1


