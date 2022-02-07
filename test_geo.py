from floodsystem.geo import stations_within_radius, rivers_with_stations, stations_by_river, stations_by_distance, rivers_by_station_number
from floodsystem.stationdata import build_station_list
from floodsystem.station import MonitoringStation

def test_station_by_distance():
    stations = build_station_list()
    a = stations_by_distance(stations, (52.2053, 0.1218))
    b = [('Cambridge Jesus Lock', 'Cambridge', 0.840237595667494), ('Bin Brook', 'Cambridge', 2.502277543239629)]
    c = [('Penzance Alverton', 'Penzance', 458.57727568406375), ('Penberth', 'Penberth', 467.53431870130544)]
    d = [('Cambridge Jesus Lock', 'Cambridge', 0.840237595667494), ('Bin Brook', 'Cambridge', 2.502277543239629), ("Cambridge Byron's Pool", 'Grantchester', 4.07204948005424)]
    e = [('Penzance Tesco', 'Penzance', 456.38638836619003), ('Penzance Alverton', 'Penzance', 458.57727568406375), ('Penberth', 'Penberth', 467.53431870130544)]
    assert a[:2] == b
    assert a[-2:] == c
    assert a[:3] == d
    assert a[-3:] == e

def test_stations_within_radius():
    stations = build_station_list()
    r = 10
    centre = (51.5326, 0.0376)
    a = sorted(stations_within_radius(stations, centre, r))
    assert a[:4] == ["Chingford", "Lea Bridge", "Manor House Gardens", "Redbridge"]

def test_rivers_with_stations():
    stations = build_station_list()
    a = len(rivers_with_stations(stations))
    b = sorted(rivers_with_stations(stations))
    assert a == 950
    assert b[:4] == ['Addlestone Bourne', 'Aire Washlands', 'Alconbury Brook', 'Aldingbourne Rife']


