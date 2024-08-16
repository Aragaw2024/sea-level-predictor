import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Load data
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='Data')

    # Create line of best fit for all data
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    plt.plot(df['Year'], slope * df['Year'] + intercept, color='red', label='Fit Line')

    # Filter data from 2000 onwards
    df_recent = df[df['Year'] >= 2000]

    # Create line of best fit for recent data
    slope_recent, intercept_recent, r_value_recent, p_value_recent, std_err_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    plt.plot(df_recent['Year'], slope_recent * df_recent['Year'] + intercept_recent, color='green', label='Fit Line (2000+)')

    # Add labels, title, and legend
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()

    # Save and show the plot
    plt.savefig('sea_level_predictor.png')
    plt.show()

draw_plot()
