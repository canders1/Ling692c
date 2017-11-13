import scipy
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans

# Load in the data using the 'read_csv' function.
taxi_data = pd.read_csv('taxi_data.csv')

# Pretty-prints the first 5 rows of the DataFrame.
print taxi_data.head(5)

# What columns are there to begin with?
for idx, column in enumerate(taxi_data.columns.values):
    print idx + 1, ':', column

print '\n'

# Rename columns with odd or strangely formatted names.
taxi_data = taxi_data.rename(index=str, columns={'lpep_pickup_datetime' : 'pickup_time','lpep_dropoff_datetime' : 'dropoff_time','PULocationID' : 'pickup_location','DOLocationID' : 'dropoff_location','passenger_count' : 'passengers','trip_distance' : 'distance','fare_amount' : 'fare','tip_amount' : 'tip'})

# Select columns of interest and drop the rest
interesting_columns = ['pickup_time','dropoff_time','pickup_location','dropoff_location','passengers', 'distance', 'fare', 'tip']
taxi_data = taxi_data[interesting_columns]

#Drop columns without known locations for pick-up and drop-off
taxi_data = taxi_data[(taxi_data['pickup_location'] < 264) & (taxi_data['dropoff_location'] < 264)]

# Which columns remain?
for idx, column in enumerate(taxi_data.columns.values):
    print idx + 1, ':', column

# Pretty-prints the first 5 rowso of the DataFrame.
print taxi_data.head(5),'\n'

#Data exploration
print '- Number of observations (datapoints) in the dataset:', len(taxi_data.index), '\n'
print '- Mean distance traveled (in miles):', taxi_data['distance'].mean(), '\n'
print '- Mean fare:', taxi_data['fare'].mean(), '\n'
print '- Mean tip:', taxi_data['tip'].mean(), '\n'
print '- Mean number of passengers:', taxi_data['passengers'].mean(), '\n'

#Histograms

plt.rcParams['figure.figsize'] = (10, 10)

plt.hist(taxi_data['distance'], bins=25, range=[0, 15]); plt.xlabel('Trip distance (mi)')
plt.ylabel('No. of observations'); plt.title('Histogram of taxicab trips by distance')
plt.show()

plt.hist(taxi_data['fare'], bins=25, range=[0, 75]); plt.xlabel('Trip fair (USD)')
plt.ylabel('No. of observations'); plt.title('Histogram of taxicab trips by fare')
plt.show()

plt.hist(taxi_data['tip'], bins=25, range=[0, 15]); plt.xlabel('Trip tip (USD)')
plt.ylabel('No. of observations'); plt.title('Histogram of taxicab trips by tip')
plt.show()