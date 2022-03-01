from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.plot import plot_water_level_with_fit
import datetime
import matplotlib.pyplot as plt
from floodsystem.station import MonitoringStation
from floodsystem.analysis import polyfit


def run():
    #Build a list of stations
    stations = build_station_list()

    #Select 55 stations with highest relative values and update current water levels in five days
    most_at_risk_stations = stations_highest_rel_level(stations, 55)
    update_water_levels(stations)
    dt = 5

    #Creating empty lists of stations with various risk levels
    Severe = []
    High = []
    Moderate = []
    Low = []
    

    for station in most_at_risk_stations:
        dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
    
        #Removing stations with insufficient data
        if len(levels) < 15 or station.name == None:
            stations.remove(station)
    
        else:
            a = len(levels)
            counter = 0

            #Counting amount of increases between given data points
            for n in range(0, a):
                if levels[a-n-1] > levels[a-n-2]:
                    counter += 1
                else:
                    break

            #Severe is defined as 7 increases with total increase of 0.3   
            if counter >= 7 and levels[a-1] - levels[a-1-counter] > 0.3:
                Severe.append(station.town)

            #High is defined as 5 increases with total increase of 0.1
            elif counter >= 5 and levels[a-1] - levels[a-1-counter] > 0.1:
                High.append(station.town)

            #Modereate is defined as 3 increases with tital increase of 0.05
            elif counter >= 3 and levels[a-1] - levels[a-1-counter] > 0.05:
                Moderate.append(station.town)

            #Everything else is Low
            else:
                Low.append(station.town)


    print(Severe, ": Severe")
    print(High, ": High")
    print(Moderate, ": Moderate")
    print(Low, ": Low")
        


if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")

    run()
