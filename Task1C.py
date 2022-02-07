from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list


def run():

    """ Prints a list of station names sorted alphabetically, within 10 km of central Cambridge (the co-ordinates given) """

    # Build list of stations, and specify centre co-ordinate (lat, lon) and radius r (km)
    stations = build_station_list()
    centre = (52.2053, 0.1218)
    r = 10

    # Sorts the list of stations within the given radius alphabetically
    stations_within_range = stations_within_radius(stations, centre, r)
    station_names = []

    for station in stations_within_range:
        station_names.append(station.name)
    
    print(sorted(station_names))

if __name__ == "__main__":
    print("*** TASK 1C ***")
    run()