import scipy
import colorsys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import mpl_toolkits
from mpl_toolkits.basemap import Basemap
from sklearn.cluster import KMeans

# Load in the data using the 'read_csv' function.
taxi_data = pd.read_csv('green_tripdata_2016-01.csv')

# Pretty-prints the first 5 rows of the DataFrame.
print taxi_data.head(5)

# What columns are there to begin with?
for idx, column in enumerate(taxi_data.columns.values):
    print idx + 1, ':', column

print '\n'

# Rename columns with odd or strangely formatted names.
taxi_data = taxi_data.rename(index=str, columns={'lpep_pickup_datetime' : 'pickup_time','Lpep_dropoff_datetime' : 'dropoff_time','Pickup_longitude' : 'pickup_longitude','Pickup_latitude' : 'pickup_latitude','Dropoff_longitude' : 'dropoff_longitude','Dropoff_latitude' : 'dropoff_latitude','Passenger_count' : 'passengers','Trip_distance' : 'distance','Fare_amount' : 'fare','Tip_amount' : 'tip'})

# Select columns of interest and drop the rest
interesting_columns = ['pickup_time','dropoff_time','pickup_longitude', 'pickup_latitude','dropoff_longitude', 'dropoff_latitude', 'passengers', 'distance', 'fare', 'tip']
taxi_data = taxi_data[interesting_columns]

# Which columns remain?
for idx, column in enumerate(taxi_data.columns.values):
    print idx + 1, ':', column

# Remove all taxi rides which don't begin or end within New York City
taxi_data = taxi_data[(taxi_data['pickup_longitude'] >= -74.025) & (taxi_data['pickup_longitude'] <= -73.76) & \
                     (taxi_data['dropoff_longitude'] >= -74.025) & (taxi_data['dropoff_longitude'] <= -73.76) & \
                     (taxi_data['pickup_latitude'] >= 40.63) & (taxi_data['pickup_latitude'] <= 40.85) & \
                     (taxi_data['dropoff_latitude'] >= 40.63) & (taxi_data['dropoff_latitude'] <= 40.85)]

print taxi_data.head(5), '\n'

#Calculating some statistics
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

plt.rcParams["figure.figsize"] = (16, 16)

#Mapping:
#Here's a sample of 25,000 taxicab pick-up locations on a map of New York City. 
#We use matplotlib.basemap.Basemap in combination with the ArcGIS service (webpage) in order to make the plots 
#on a background of New York City.
m = Basemap(projection='hammer', llcrnrlon=-74.025, llcrnrlat=40.63, urcrnrlon=-73.76, urcrnrlat=40.85, epsg=4269)
m.arcgisimage(service='World_Street_Map', xpixels=2000, dpi=400)

samples = np.random.choice(taxi_data.index, 25000, replace=False)
plt.scatter(taxi_data['pickup_longitude'][samples], taxi_data['pickup_latitude'][samples], c='b', alpha=0.75)
plt.show()

#Now, let's look at the drop-off locations of those same 25,000 samples.
m = Basemap(projection='hammer', llcrnrlon=-74.025, llcrnrlat=40.63, urcrnrlon=-73.76, urcrnrlat=40.85, epsg=4269)
m.arcgisimage(service='World_Street_Map', xpixels=2000, dpi=400)

samples = np.random.choice(taxi_data.index, 25000, replace=False)

plt.scatter(taxi_data['dropoff_longitude'][samples], taxi_data['dropoff_latitude'][samples], c='r', alpha=0.75)
plt.show()

#Let's cluster the pick-up locations to make sense of where green taxicabs get their business.
sample_pickups = np.array(zip(taxi_data['pickup_longitude'][samples], taxi_data['pickup_latitude'][samples]))
n_clusters = 15 # How many clusters to use.
model = KMeans(n_clusters=n_clusters).fit(sample_pickups)

#Plot clusters
m = Basemap(projection='hammer', llcrnrlon=-74.025, llcrnrlat=40.63, urcrnrlon=-73.76, urcrnrlat=40.85, epsg=4269)
m.arcgisimage(service='World_Street_Map', xpixels=2000, dpi=400)

# Get the (longitude, latitude) coordinates of the cluster centers found by the KMeans algorithm.
cluster_longitudes, cluster_latitudes = model.cluster_centers_[:, 0], model.cluster_centers_[:, 1]

# Get 'n_clusters' distinct colors for visualizing clusters.
HSVs = [(x*1.0/n_clusters, 0.5, 0.5) for x in range(n_clusters)]
RGBs = map(lambda x: colorsys.hsv_to_rgb(*x), HSVs)

# Plot each group of taxicab pickups in turn by cluster identity.
for idx in xrange(n_clusters):
    plt.scatter(taxi_data['pickup_longitude'][samples][model.labels_ == idx], \
        taxi_data['pickup_latitude'][samples][model.labels_ == idx], c=RGBs[idx], alpha=0.25)

plt.scatter(cluster_longitudes, cluster_latitudes, s=250, marker='+', c='r')
plt.show()

#Now that we have a clustering of this month's taxicab pickup locations and have visualized it on our map of NYC, 
#let's calculate some quantities of interest per cluster. 
#For example, based on which cluster we are located in, what is the average value of the cab fare?

plt.rcParams["figure.figsize"] = (10, 5)

# Get the fares from the taxicab trips previously sampled from the entire data.
fare_samples = np.array(taxi_data['fare'][samples])

average_fares = []
# Loop through each cluster by index.
for cluster_idx in xrange(n_clusters):
    # Calculate the average value of the fare based on the cluster index.
    average_fares.append(np.mean(fare_samples[np.where(model.labels_ == cluster_idx)]))

plt.bar(xrange(n_clusters), average_fares), plt.xticks(xrange(n_clusters))
plt.title('Average fare paid per cluster')
plt.show()

# Get the distances from the taxicab trips previously sampled from the entire data.
distance_samples = np.array(taxi_data['distance'][samples])

average_distances = []
# Loop through each cluster by index.
for cluster_idx in xrange(n_clusters):
    # Calculate the average value of the distance based on the cluster index.
    average_distances.append(np.mean(distance_samples[np.where(model.labels_ == cluster_idx)]))

plt.bar(xrange(n_clusters), average_distances), plt.xticks(xrange(n_clusters))
plt.title('Average distance traveled per cluster')
plt.show()

# Get the tips from the taxicab trips previously sampled from the entire data.
tip_samples = np.array(taxi_data['tip'][samples])

average_tips = []
# Loop through each cluster by index.
for cluster_idx in xrange(n_clusters):
    # Calculate the average value of the tip based on the cluster index.
    average_tips.append(np.mean(tip_samples[np.where(model.labels_ == cluster_idx)]))

plt.bar(xrange(n_clusters), average_tips), plt.xticks(xrange(n_clusters))
plt.title('Average tip paid per cluster')
plt.show()

#Let's plot the average values of the tips per cluster on the map of New York City along with 
#text annotations with the average tip on the cluster centers.

plt.rcParams["figure.figsize"] = (16, 16)

m = Basemap(projection='hammer', llcrnrlon=-74.025, llcrnrlat=40.63, urcrnrlon=-73.76, urcrnrlat=40.85, epsg=4269)
m.arcgisimage(service='World_Street_Map', xpixels=2000, dpi=400)

# Plot each group of taxicab pickups in turn by cluster identity.
# for idx in xrange(n_clusters):
#     plt.scatter(taxi_data['pickup_longitude'][samples][model.labels_ == idx], \
#         taxi_data['pickup_latitude'][samples][model.labels_ == idx], c=RGBs[idx], alpha=0.1)

# Annotate each cluster center with the average tip value.

for idx, average_tip in enumerate(average_tips):
    plt.annotate('{0:.2f}'.format(average_tip), xy=(model.cluster_centers_[idx][0], \
                                    model.cluster_centers_[idx][1]))

plt.scatter(cluster_longitudes, cluster_latitudes, s=250, marker='+', c='r')
plt.show()

#Export dataframe as csv again
taxi_data.to_csv('out.csv')