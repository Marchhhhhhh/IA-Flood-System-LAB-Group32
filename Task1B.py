from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list


def run():
    """Producing 10 closest and the 10 furthest stations from the Cambridge city centre"""
    
    # Building list of stations
    stations = build_station_list()

    ##applying the function, finding the distance between stations and the coordinate
    x = stations_by_distance(stations,(52.2053, 0.1218))

    #Closest 10
    print(x[:10])

    #Furthest 10
    print(x[-10:])

if __name__ == "__main__":
    print("*** Task 1B  ***")
    run()
