from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list, update_water_levels

def run():

    stations = build_station_list()
    update_water_levels(stations)

    top_stations = stations_highest_rel_level(stations, 10)

    for item in top_stations:
        print(item.name, item.relative_water_level())
        


run()