from .utils import sorted_by_key
from floodsystem.station import MonitoringStation

def stations_level_over_threshold(stations, tol):
    final_list = []
    for item in stations:
        if item.name == "Letcombe Bassett" or "Hayes Basin":
            stations.remove(item)
        a = item.relative_water_level()
        if isinstance(a, int) or isinstance(a, float):
            if a > tol:
                final_list.append((item, a))
                
    
    a = sorted_by_key(final_list, 1, reverse=True)
    return a