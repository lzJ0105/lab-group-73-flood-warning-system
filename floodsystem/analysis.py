import matplotlib.dates as mdates
import numpy as np

def polyfit(dates, levels, p):
    """
    Computes a least-squares polynomial fit of degree p to water level data,
    given the history of levels.

    Args:
        dates (list): List of datetime objects
        levels (list): List of water levels (floats)
        p (int): Degree of polynomial (e.g., 4)

    Returns:
        tuple: (polynomial_object, time_shift)
               The polynomial object can be called like a function: poly(x).
               The time_shift is the value subtracted from the dates to avoid rounding errors.
    """
    
    # HINT 1 in instructions: Convert dates to floats (days since year 0001)
    x = mdates.date2num(dates)
    y = np.array(levels)

    # CAUTION in Instructions: "RankWarning: Polyfit may be poorly conditioned"
    # The dates (x) are huge numbers (e.g., 738000 days). Raising them to power p
    # causes massive rounding errors.
    # SOLUTION: Shift the x-axis by subtracting the start date (x[0]).
    # Fit the polynomial to the *relative* time, not the absolute time.
    p_coeff = np.polyfit(x - x[0], y, p)

    # HINT 2 in instructions: Convert coefficients into a polynomial object
    poly = np.poly1d(p_coeff)

    # Return the polynomial AND the shift so the plotter knows how to use it.
    return poly, x[0]