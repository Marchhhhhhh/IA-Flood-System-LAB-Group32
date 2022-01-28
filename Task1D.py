from floodsystem.geo import rivers_with_stations
from floodsystem.stationdata import build_station_list

def run():

    """Requirements for Task 1D"""
    
    stations = build_station_list()

    rivers_monitored = rivers_with_stations(stations)

    number_of_rivers = len(rivers_monitored)

    rivers_alphabetically = sorted(rivers_monitored)

    print(number_of_rivers, "stations. First 10 - ", rivers_alphabetically[0:9])


if __name__ == "__main__":
    print("*** TASK D ***")
    run()

