from floodsystem.geo import rivers_with_stations
from floodsystem.geo import stations_by_river
from floodsystem.stationdata import build_station_list

def run():

    """Print the number of rivers with at least one station, and the first 10 rivers in that list"""
    
    # Build a list of MonitoringStation objects
    stations = build_station_list()

    # Create a set of rivers with at least one station using rivers_with_stations
    rivers_monitored = rivers_with_stations(stations)

    # Find the number of rivers with at least one station
    number_of_rivers = len(rivers_monitored)

    # Sort the list of rivers alphabetically
    rivers_alphabetically = sorted(rivers_monitored)

    # Print the number of rivers with at least one station and the first ten of these alphabetically.
    print(number_of_rivers, "rivers with at least 1 station. First 10 -", rivers_alphabetically[0:10])


def run2():

    """Print a list of station's names that are on the River Aire, River Cam and River Thames"""

    # Build a list of MonitoringStation objects
    stations = build_station_list()

    # Create a dictionary using river names as keys to a list of stations on that river
    stations_with_river = stations_by_river(stations)

    # Create and print a list of station names on the River Aire
    Aire_station_list = []
    for station in stations_with_river["River Aire"]:
        Aire_station_list.append(station.name)
    
    print(sorted(Aire_station_list))

    # Create and print a list of station names on the River Cam
    Cam_station_list = []
    for station in stations_with_river["River Cam"]:
        Cam_station_list.append(station.name)
        
    print(sorted(Cam_station_list))

    # Create and print a list of station names on the River Thames
    Thames_station_list = []
    for station in stations_with_river["River Thames"]:
        Thames_station_list.append(station.name)
        
    print(sorted(Thames_station_list))




if __name__ == "__main__":
    print("*** TASK D ***")
    run()
    run2()
