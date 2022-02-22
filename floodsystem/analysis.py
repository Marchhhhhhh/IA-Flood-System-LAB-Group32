import matplotlib
import numpy as np

def polyfit(dates, levels, p):

    x = matplotlib.dates.date2num(dates)
    y = levels

    p_coeff = np.polyfit(x-x[0], y, p)

    poly = np.poly1d(p_coeff)

    d0 = x[0]

    return (poly, d0)
