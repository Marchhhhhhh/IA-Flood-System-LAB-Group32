from os import times
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.analysis import polyfit
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level
import datetime


def run():

    stations = build_station_list()
    update_water_levels(stations)

    stations_to_plot = stations_highest_rel_level(stations, 5)

    for item in stations_to_plot:
        dates, levels = fetch_measure_levels(item.measure_id, datetime.timedelta(days=2))
        plot_water_level_with_fit(item, dates, levels, 4)
    
    print([(station.name, station.relative_water_level()) for station in stations_to_plot])
    

if __name__ == "__main__":
    print("*** Task 2F: CUED Part IA Flood Warning System ***")
    run()
