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
    
    a = stations_within_radius(stations_for_test, centre, radius)
    b = []

    for item in a:
        b.append(item.name)
    
    assert b == ["Station 0", "Station 1", "Station 2"]



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


def test_stations_by_river():

    "A test for the function used in Task1D.py called stations_by_river"

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

    # a is a dictionary where river name maps to a list of objects, not names
    a = stations_by_river(stations_for_test)
    
    assert a["Thames"] == [stations_for_test[2], stations_for_test[4], stations_for_test[7]]

#Test for Task1B
def test_stations_by_distance():
    stations = []
    for n in range(5):
        stations.append(create_test_monitoring_station(n))

    a = stations_by_distance(stations,(0.0, 0.0))
    b = a[:2]
    c = a[-2:]
    assert b == [('Station 0', 'My Town', 0.0), ('Station 1', 'My Town', 497.19868760742435)]
    assert c == [('Station 3', 'My Town', 1489.6476396668857), ('Station 4', 'My Town', 1983.9070100764739)]

#Test for Task1E
def test_rivers_by_station_number():

    stations = []
    for i in range(50):
        stations.append(create_test_monitoring_station(i))
        
    for i in range(11):
        stations[i].river = "River Thames"

    for i in range(11):
        stations[i].river = "River Thames"

    for i in range(11, 13):
        stations[i].river = "River Nile"

    for i in range(13, 20):
        stations[i].river = "River Cam"

    for i in range(20, 27):
        stations[i].river = "River Danube"

    for i in range(27, 32):
        stations[i].river = "River Seine"

    for i in range(32, 39):
        stations[i].river = "River Mississippi"

    for i in range(39, 50):
        stations[i].river = "River Amazon"

    a = rivers_by_station_number(stations, 3)


    assert a == [("River Thames", 11), ("River Amazon", 11), ("River Mississippi", 7), ("River Danube", 7), ("River Cam", 7)]


