import matplotlib
import numpy as np

def polyfit(dates, levels, p):

    """Function that returns a fitting  polynomial and amount it is shfited to match data.
    
    Args: dates (list of datetime objects for the past), levels (list of water levels corresponding to dates), p (order of polynomial to fit)
    
    Return: poly (a numpy polynomial that fits the data), d0 (amount of shift due to dates being very large numbers), as a tuple"""

    #convert datetime objects to integers
    x = matplotlib.dates.date2num(dates)
    y = levels

    #find polynomial coefficients that match the shifted data (because the new dates are measured in days since year 2000)
    p_coeff = np.polyfit(x-x[0], y, p)

    #convert to polynomial
    poly = np.poly1d(p_coeff)

    #defines shift
    d0 = x[0]

    return (poly, d0)
