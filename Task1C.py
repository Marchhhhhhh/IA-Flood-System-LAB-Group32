from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list

def run():

    """ Requirements for Task 1C """

    stations = build_station_list()
    centre = (52.2053, 0.1218)
    r = 5

    print(stations_within_radius(stations, centre, r))


if __name__ == "__main__":
    print("*** Task C ***")
    run()