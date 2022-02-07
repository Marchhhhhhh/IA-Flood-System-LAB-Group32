from floodsystem.geo import rivers_with_stations
from floodsystem.geo import stations_by_river
from floodsystem.stationdata import build_station_list

def run():

    """Print the number of rivers with at least one station, and the first 10 rivers in that list"""
    
    stations = build_station_list()
    rivers_monitored = rivers_with_stations(stations)

    number_of_rivers = len(rivers_monitored)

    rivers_alphabetically = sorted(rivers_monitored)

    print(number_of_rivers, "stations. First 10 -", rivers_alphabetically[0:10])


def run2():

    """Print a list of station's names that are on the River Aire, River Cam and River Thames"""
    
    stations = build_station_list()
    stations_with_river = stations_by_river(stations)

    Aire_station_list = []
    for station in stations_with_river["River Aire"]:
        Aire_station_list.append(station.name)
    
    print(sorted(Aire_station_list))


    Cam_station_list = []
    for station in stations_with_river["River Cam"]:
        Cam_station_list.append(station.name)
        
    print(sorted(Cam_station_list))


    Thames_station_list = []
    for station in stations_with_river["River Thames"]:
        Thames_station_list.append(station.name)
        
    print(sorted(Thames_station_list))




if __name__ == "__main__":
    print("*** TASK D ***")
    run()
    run2()
