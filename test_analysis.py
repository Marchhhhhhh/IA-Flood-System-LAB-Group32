from floodsystem.analysis import polyfit
import numpy as np

def test_polyfit():
    
    x = np.linspace(0, 10, 50)
    y = np.empty(50)

    for i in range(50):
        y_value = (x[i])**4 + 5*(x[i])**2 + 6
        np.append(y, y_value)

    a = polyfit(x, y, 4)
    
    assert a == (np.poly1d([ 2.82381470e-282, -7.39084539e-292,  6.58076555e-302,
       -2.26916550e-312,  2.47032823e-323]), 0.0)