from os import times
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.analysis import polyfit
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.stationdata import build_station_list
from floodsystem.flood import stations_highest_rel_level
import datetime

def run():

    # Cam just being used as a test example for the polyfit function developed in analysis module.
    stations = build_station_list()
    station_name = "Cam"

    for station in stations:
        if station.name == station_name:
            station_cam = station
            break

    dates, levels = fetch_measure_levels(station_cam.measure_id, datetime.timedelta(days=2))

    polynomial_fit = polyfit(dates, levels, 4)

    return polynomial_fit


def run2():

    stations = build_station_list()
    station_name = "Castle Foregate"

    for station in stations:
        if station.name == station_name:
            station_cam = station
            break
    
    dates, levels = fetch_measure_levels(station_cam.measure_id, datetime.timedelta(days=2))

    plot_water_level_with_fit(station_cam, dates, levels, 4)

print(run())
run2()


def realrun():

    stations = build_station_list()
    stations_to_plot = stations_highest_rel_level(stations, 5)

    for item in stations_to_plot:
        dates, levels = fetch_measure_levels(item.measure_id, datetime.timedelta(days=2))
        plot_water_level_with_fit(item, dates, levels, 4)
    
    
