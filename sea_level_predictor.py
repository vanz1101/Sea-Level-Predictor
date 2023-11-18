import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
  df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
  x = df['Year']
  y = df['CSIRO Adjusted Sea Level']

  plt.scatter(x,y)

    # Create first line of best fit
  slope, intercept, r_value, p_value, std_err = linregress(x, y)
  x_fit = list(range(min(x), 2051))
  y_fit = [slope * i + intercept for i in x_fit]
  plt.plot(x_fit, y_fit, color='red')

    # Create second line of best fit
  new_df = df[df.Year >= 2000]
  x1 = new_df['Year']
  y1 = new_df['CSIRO Adjusted Sea Level']

  slope, intercept, r_value, p_value, std_err = linregress(x1, y1)
  x_fit1 = list(range(min(x1), 2051))
  y_fit = [slope * j + intercept for j in x_fit1]
  plt.plot(x_fit1, y_fit, color='blue')

    # Add labels and title
  plt.xlabel('Year')
  plt.ylabel('Sea Level (inches)')
  plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
  plt.savefig('sea_level_plot.png')
  return plt.gca()