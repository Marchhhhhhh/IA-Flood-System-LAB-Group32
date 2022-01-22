from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list

def run():

    """ Requirements for Task 1C """

    stations = build_station_list()
    centre = (52.2053, 0.1218)
    r = 5
    stations_within_range = []

    stations_within_radius(stations, centre, r)

    print(stations_within_range)
    return stations_within_range

run()

