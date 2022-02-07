from floodsystem.station import inconsistent_typical_range_stations
from floodsystem.stationdata import build_station_list

def run():
    """"Provides a list of the names of stations with inconsistent range data, in alphabetical order"""

    # Creates a list of MonitoringStation objects
    stations = build_station_list()

    # Creates a list of station objects with inconsistent range data
    inconsistent_stations = inconsistent_typical_range_stations(stations)

    # Prints a list of station names corresponding to station of objects with inconsistent range data, alphabetically sorted.
    print(sorted([station.name for station in inconsistent_stations]))

if __name__ == "__main__":
    print("*** TASK F ***")
    run()
