from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.plot import plot_water_level_with_fit
import datetime


def run():
    stations = build_station_list()
    update_water_levels(stations)

    most_at_risk_stations = stations_highest_rel_level(stations, 80)

    for item in most_at_risk_stations:
        if item.name == None:
            most_at_risk_stations.remove(item)
        if item.latest_level > 5:
            print(item.town, ' : severe')
        elif item.latest_level > 3:
            print(item.town, ' : high')
        elif item.latest_level > 1:
            print(item.town, ' : moderate')
        else:
            print(item.town, ': low')


if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")

    run()