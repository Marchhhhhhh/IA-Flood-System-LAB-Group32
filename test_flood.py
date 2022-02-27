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

def test_stations_level_over_threshold():
    stations = []
    for n in range(4):
        stations.append(create_test_monitoring_station(n))
    stations[0].latest_level=4
    stations[1].latest_level=1
    stations[2].latest_level=None
    stations[3].latest_level=16
    results = stations_level_over_threshold(stations,0.1)
    a = []
    for s in results:
      a.append("{} {}".format(s[0].name, s[1]))
    assert a == ['Station 3 5.233333333333333', 'Station 1 0.9']
    assert len(results) == 2