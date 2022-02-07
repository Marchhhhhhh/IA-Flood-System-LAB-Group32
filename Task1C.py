from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list
from test_geo import test_stations_within_radius

def run():

    """ Requirements for Task 1C """
    test_stations_within_radius()

    # Build list of stations, and specify centre co-ordinate (lat, lon) and radius r (km)
    stations = build_station_list()
    centre = (52.2053, 0.1218)
    r = 10

    # Sorts the list of stations within the given radius alphabetically
    alphabetical_stations = sorted(stations_within_radius(stations, centre, r))
    print(alphabetical_stations)

if __name__ == "__main__":
    print("*** TASK 1C ***")
    run()