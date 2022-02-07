from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list

def test_station_by_distance():
    stations = build_station_list()
    a = stations_by_distance(stations, (52.2053, 0.1218))
    b = [('Cambridge Jesus Lock', 'Cambridge', 0.840237595667494), ('Bin Brook', 'Cambridge', 2.502277543239629)]
    c = [('Boscadjack', 'Wendron', 440.00325604140033), ('Gwithian', 'Gwithian', 442.0555261735786), ('Helston County Bridge', 'Helston', 443.3788620846717)]
    assert a[:2] == b
    assert a[:-2] == c
    

