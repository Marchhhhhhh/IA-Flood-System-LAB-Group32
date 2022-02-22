import matplotlib.pyplot as plt
import matplotlib
import datetime
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.analysis import polyfit
import numpy as np

def plot_water_levels(station, dates, levels):

    t, level = fetch_measure_levels(
    station.measure_id, dt=datetime.timedelta(days=dates))

    typ_low = [levels[0]]*len(t)
    typ_high = [levels[1]]*len(t)

    # Plot
    plt.plot(t, level)
    plt.plot(t, typ_low)
    plt.plot(t, typ_high)

    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('Date')
    plt.ylabel('Water level (m)')
    plt.xticks(rotation=45)
    plt.title(station.name)

    plt.tight_layout()

    plt.show()


def plot_water_level_with_fit(station, dates, levels, p):

    polynomial_fit = polyfit(dates, levels, p)[0]
    #shift = polyfit(dates, levels, p)[1]

    x = matplotlib.dates.date2num(dates)
    y = levels

    x1 = np.linspace(x[0], x[-1], 30)
    
    plt.plot(x-x[0], y, '.')
    plt.plot(x1-x[0], polynomial_fit(x1-x[0]))

    plt.title(station.name)

    plt.show()

