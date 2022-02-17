import matplotlib.pyplot as plt
import matplotlib
import datetime
from floodsystem.datafetcher import fetch_measure_levels

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