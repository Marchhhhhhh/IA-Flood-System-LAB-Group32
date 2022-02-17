from floodsystem.plot import plot_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list, update_water_levels


def run():
    """Requirements for Task 2E"""

    # Build list of stations
    stations = build_station_list()

    update_water_levels(stations)
    N = 5
    shortlist = stations_highest_rel_level(stations, N)


    for station in shortlist:
        if station.relative_water_level() > 500:
            print("WARNING: Station {} has erroneous data and will not be plotted".format(station.name))
            N += 1

    newlist = flood.stations_highest_rel_level(stations, N)

    for station in newlist:

        if station.relative_water_level() > 500:
            pass
        else: 
            plot_water_levels(station, 10, station.typical_range)        
    

if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()