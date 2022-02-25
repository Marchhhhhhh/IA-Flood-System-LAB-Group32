from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.plot import plot_water_level_with_fit
import datetime


def run():
    stations = build_station_list()
    update_water_levels(stations)

    most_at_risk_stations = stations_highest_rel_level(stations, 50)

    for item in most_at_risk_stations:
        if item.coord[0] > 50:
            print(item.name + ' : severe')
        elif item.coord[0]>40:
            print(item.name+' : high')
        elif item.coord[0]>30:
            print(item.name+' : moderate')
        else:
            print(item.name+': low')


if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")

    run()