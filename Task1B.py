from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list


def run():
    """Requirements for Task 1B"""
    
    # Building list of stations
    stations = build_station_list()
    x = stations_by_distance(stations,(52.2053, 0.1218))
    print(x[:10])
    print(x[-10:])

if __name__ == "__main__":
    print("*** Task 1B  ***")
    run()
