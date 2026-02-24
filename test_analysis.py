"""Unit test for the analysis module"""

import datetime
import numpy as np
from floodsystem.analysis import polyfit

def test_polyfit():
    """Test the polyfit function returns correct types"""
    
    #Create dummy dates (3 consecutive days) and levels
    dates = [
        datetime.datetime(2026, 1, 1),
        datetime.datetime(2026, 1, 2),
        datetime.datetime(2026, 1, 3)
    ]
    levels = [1.0, 2.0, 3.0]
    
    #Run the function (degree 1 = straight line)
    poly, d0 = polyfit(dates, levels, 1)
    
    #Check that the outputs are the correct type
    assert isinstance(poly, np.poly1d)
    assert isinstance(d0, float)