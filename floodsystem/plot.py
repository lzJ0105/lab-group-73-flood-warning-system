import matplotlib.pyplot as plt


def plot_water_levels(station, dates, levels):
    """
    Displays plot of the water level data against time for a station.
    Also plot the typical low and high levels.
    """
    
    # Use the example matplotlib code from instructions
    # Plot the water level data
    plt.plot(dates, levels, label="Water Level")
    
    # Add the Typical Low and High lines
    low = station.typical_range[0]
    high = station.typical_range[1]
    
    plt.axhline(y=low, color='g', linestyle='--', label="Typical Low")
    plt.axhline(y=high, color='r', linestyle='--', label="Typical High")
    
    # Add labels and title
    plt.xlabel('Date')
    plt.ylabel('Water Level (m)')
    plt.title(f"Station: {station.name}")
    plt.xticks(rotation=45)  
    plt.legend()            
    plt.tight_layout()   
    
    # Show plot
    plt.show()


import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
from .analysis import polyfit  # Import the new analysis function wrote in Task 2F


def plot_water_level_with_fit(station, dates, levels, p):
    """
    Plots the water level data and the best-fit polynomial.
    
    Args:
        station (MonitoringStation): The station object
        dates (list): List of datetime objects
        levels (list): List of water levels
        p (int): Degree of polynomial
    """
    
    # Get the polynomial and the shift
    # Need the shift (d0) because the polynomial expects inputs like (0, 0.1, 0.2...), not (738000, 738000.1...)
    poly, d0 = polyfit(dates, levels, p)

    # Plot the original data points
    plt.plot(dates, levels, '.', label="Measured Data")

    # Plot the polynomial fit, create a smooth range of 30 points from start to end
    x_dates_num = mdates.date2num(dates)
    x1 = np.linspace(x_dates_num[0], x_dates_num[-1], 30)

    # Subtract the shift (d0) before passing x1 to the polynomial
    # Then convert back to dates for the plot
    plt.plot(mdates.num2date(x1), poly(x1 - d0), label=f"Fit (Degree {p})")

    # Again, add Typical Low/High lines
    low = station.typical_range[0]
    high = station.typical_range[1]
    plt.axhline(low, color='g', linestyle='--', label="Typical Low")
    plt.axhline(high, color='r', linestyle='--', label="Typical High")

    # Styling
    plt.xlabel('Date')
    plt.ylabel('Water Level (m)')
    plt.title(f"Station: {station.name}")
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()


    plt.show()