from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list

def test_station_by_distance():
    stations = build_station_list()
    a = stations_by_distance(stations, (52.2053, 0.1218))
    b = [('Cambridge Jesus Lock', 'Cambridge', 0.840237595667494), ('Bin Brook', 'Cambridge', 2.502277543239629)]
    c = [('Penzance Alverton', 'Penzance', 458.57727568406375), ('Penberth', 'Penberth', 467.53431870130544)]
    assert a[:2] == b
    assert a[:-2] == c
    

