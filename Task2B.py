from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.station import MonitoringStation
from floodsystem.flood import stations_level_over_threshold


def run():
    """Requirements for Task2B"""

    # Build list of stations
    stations = build_station_list()
    update_water_levels(stations)
    tol = 0.8
    present = stations_level_over_threshold(stations, tol)
        

    for station in present:
        print("{} {}".format(station[0].name, station[1]))


if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")

    run()