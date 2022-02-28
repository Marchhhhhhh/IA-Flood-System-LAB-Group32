from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list, update_water_levels

def run():

    "Returns tuples of top 10 stations (by realtive water level), displaying station name and relative water levels"

    #create list of stations and update their water levels
    stations = build_station_list()
    update_water_levels(stations)

    #create a new list of the top 10 stations by relative water level
    top_stations = stations_highest_rel_level(stations, 10)

    #print tuples for each station
    for item in top_stations:
        print(item.name, item.relative_water_level())


if __name__ == "__main__":
    print("*** Task 2C: CUED Part IA Flood Warning System ***")
    run()
