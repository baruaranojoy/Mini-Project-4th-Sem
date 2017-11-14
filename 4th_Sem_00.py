f_source = open("streamed_data.txt","r")

destination = open("Edge_List.txt","w")
destination.close()
f_destination = open("Edge_List.txt","a")

data = []
unique_element = []

for line in f_source:
    v1,v2 = map(int,line.rstrip().split())
    final = [v1, v2]
    unique_element.append(v1)
    unique_element.append(v2)
    data.append(final)

f_source.close()

data.sort()
unique_element = list(set(unique_element))

################################################################################

data_1 = []
for k in range(len(data)):
    data_1.append(data[k])

import numpy as np
from sklearn.cluster import KMeans
from sklearn import preprocessing
import pandas as pd
import matplotlib.pyplot as plt


X = np.array(data_1)

kmeans = KMeans(n_clusters=4).fit(X)

cluster1 = []
cluster2 = []
cluster3 = []
cluster4 = []


for k in range(len(data_1)):
    cluster = kmeans.predict(data_1[k])
    if cluster == 0:
        cluster1.append(data_1[k])
    elif cluster == 1:
        cluster2.append(data_1[k])
    elif cluster == 2:
        cluster3.append(data_1[k])
    elif cluster == 3:
        cluster4.append(data_1[k])


x_1 = []
y_1 = []
for k in range(len(cluster1)):
    dop = cluster1[k]
    x_1.append(dop[0])
    y_1.append(dop[1])
plt.scatter(x_1, y_1, color=['red'])


x_2 = []
y_2 = []
for k in range(len(cluster2)):
    dop = cluster2[k]
    x_2.append(dop[0])
    y_2.append(dop[1])
plt.scatter(x_2, y_2, color=['yellow'])

x_3 = []
y_3 = []
for k in range(len(cluster3)):
    dop = cluster3[k]
    x_3.append(dop[0])
    y_3.append(dop[1])
plt.scatter(x_3, y_3, color=['blue'])

x_4 = []
y_4 = []
for k in range(len(cluster4)):
    dop = cluster4[k]
    x_4.append(dop[0])
    y_4.append(dop[1])
plt.scatter(x_4, y_4, color=['green'])


plt.xlabel('Source (Green: Cluster-1, Red: Cluster-2, Blue: Cluster-3, Yellow: Cluster-4)')
plt.ylabel('Destination')



plt.show()


plt.plot(data_1, 'ro')
plt.show()


print  kmeans.cluster_centers_

##f_open_1 = open("Cluster_1.txt","w")
##f_open_2 = open("Cluster_2.txt","w")
##f_open_3 = open("Cluster_3.txt","w")
##f_open_4 = open("Cluster_4.txt","w")
##
##for k in range(len(cluster1)):
##    kk = cluster1[k]
##    f_open_1.write(str(kk[0]) + " " + str(kk[1]) + "\n")
##    
##for k in range(len(cluster2)):
##    kk = cluster2[k]
##    f_open_2.write(str(kk[0]) + " " + str(kk[1]) + "\n")
##    
##for k in range(len(cluster3)):
##    kk = cluster3[k]
##    f_open_3.write(str(kk[0]) + " " + str(kk[1]) + "\n")
##
##for k in range(len(cluster4)):
##    kk = cluster4[k]
##    f_open_4.write(str(kk[0]) + " " + str(kk[1]) + "\n")
##    
##################################################################################
##f_open_5 = open("Edge_List.txt","w")
##for k in range(len(data)):
##    kk = data[k]
##    f_open_5.write(str(kk[0]) + " " + str(kk[1]) + "\n")
##
##f_open_1.close()
##f_open_2.close()
##f_open_3.close()
##f_open_4.close()
##f_open_5.close()

print len(cluster1)
print len(cluster2)
print len(cluster3)
print len(cluster4)



import numpy as np
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

k = np.genfromtxt('Road networks/californial coordinates.txt', dtype= None)

clust1 = []
clust2 = []
clust3 = []
clust4 = []

for p in range(len(cluster1)):
    data = cluster1[p]
    one = data[0]
    for m in range(len(k)):
        qwe = k[m]
        if qwe[0] == one:
            clust1.append([qwe[1], qwe[2]])
            break

for p in range(len(cluster2)):
    data = cluster2[p]
    one = data[0]
    two = data[1]
    for m in range(len(k)):
        qwe = k[m]
        if qwe[0] == one:
            clust2.append([qwe[1], qwe[2]])
            break

for p in range(len(cluster3)):
    data = cluster3[p]
    one = data[0]
    two = data[1]
    for m in range(len(k)):
        qwe = k[m]
        if qwe[0] == one:
            clust3.append([qwe[1], qwe[2]])
            break


for p in range(len(cluster4)):
    data = cluster4[p]
    one = data[0]
    two = data[1]
    for m in range(len(k)):
        qwe = k[m]
        if qwe[0] == one:
            clust4.append([qwe[1], qwe[2]])
            break


print len(k)
print len(clust1)
print len(clust2)
print len(clust3)
print len(clust4)


m = Basemap(projection='mill',
            llcrnrlat = 25,
            llcrnrlon = -130,
            urcrnrlat = 50,
            urcrnrlon = -60,
            resolution = 'f')
#m.bluemarble()
m.drawcoastlines()
m.drawcountries(linewidth=2)
m.drawstates(color = 'b')

for y in range(len(clust1)):
    data = clust1[y]
    lon = data[0]
    lat = data[1]
    NYClat , NYClon = lat , lon
    xpt , ypt = m(NYClon , NYClat)
    m.plot(xpt , ypt , 'r*' , markersize=2 , label = 'Most Influential Point')

#plt.show()

for y in range(len(clust2)):
    data = clust2[y]
    lon = data[0]
    lat = data[1]
    NYClat , NYClon = lat , lon
    xpt , ypt = m(NYClon , NYClat)
    m.plot(xpt , ypt , 'y^' , markersize=5 , label = 'Most Influential Point')

#plt.show()

for y in range(len(clust2)):
    data = clust2[y]
    lon = data[0]
    lat = data[1]
    NYClat , NYClon = lat , lon
    xpt , ypt = m(NYClon , NYClat)
    m.plot(xpt , ypt , 'b*' , markersize=2 , label = 'Most Influential Point')

#plt.show()

for y in range(len(clust4)):
    data = clust4[y]
    lon = data[0]
    lat = data[1]
    NYClat , NYClon = lat , lon
    xpt , ypt = m(NYClon , NYClat)
    m.plot(xpt , ypt , 'g*' , markersize=2 , label = 'Most Influential Point')

plt.show()







    
