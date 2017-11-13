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
taxi_data = taxi_data.rename(index=str, columns={'lpep_pickup_datetime' : 'pickup_time','Lpep_dropoff_datetime' : 'dropoff_time','Pickup_longitude' : 'pickup_longitude','Pickup_latitude' : 'pickup_latitude','Dropoff_longitude' : 'dropoff_longitude','Dropoff_latitude' : 'dropoff_latitude','Passenger_count' : 'passengers','Trip_distance' : 'distance','Fare_amount' : 'fare','Tip_amount' : 'tip'})

# Select columns of interest and drop the rest
interesting_columns = ['pickup_time', 'dropoff_time', 'pickup_longitude', 'pickup_latitude','dropoff_longitude', 'dropoff_latitude', 'passengers', 'distance', 'fare', 'tip']
taxi_data = taxi_data[interesting_columns]