from floodsystem.geo import rivers_by_station_number
from floodsystem.stationdata import build_station_list


def run():
    """Finding rivers with the greatest n numbers of stations"""
    
    #Building list of stations
    stations = build_station_list()
    

    #Applying the function to find rivers with 9 highest numbers of stations
    b = rivers_by_station_number(stations, 9)
    
    print(b)


if __name__ == "__main__":
    print("*** Task 1E: CUED Part IA Flood Warning System ***")
    run()