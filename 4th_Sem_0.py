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
for k in range(2000):
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
cluster5 = []
collect = []

for k in range(len(data_1)):
    cluster = kmeans.predict(data_1[k])
    if cluster == 0:
        cluster1.append(data_1[k])
        collect.append(data_1[k])
    elif cluster == 1:
        cluster2.append(data_1[k])
        collect.append(data_1[k])
    elif cluster == 2:
        cluster3.append(data_1[k])
        collect.append(data_1[k])
    elif cluster == 3:
        cluster4.append(data_1[k])
        collect.append(data_1[k])
    else:
        cluster5.append(data_1[k])
        collect.append(data_1[k])

plt.plot(cluster1, 'go' , label = 'Cluster-1')
plt.plot(cluster2, 'ro' , label = 'Cluster-2')
plt.plot(cluster3, 'bo' , label = 'Cluster-3')
plt.plot(cluster4, 'yo' , label = 'Cluster-4')

print kmeans.cluster_centers_
print len(data_1)
print len(cluster1) + len(cluster2) + len(cluster3) + len(cluster4)
print len(cluster5)

#plt.plot(collect, 'r^')
data_1.sort()
collect.sort()

ello = 0
for k in range(len(collect)):
    if collect[k] != data_1[k]:
        print "True"
        ello = 1
        break
print ello

plt.xlabel('Source (Green: Cluster-1, Red: Cluster-2, Blue: Cluster-3, Yellow: Cluster-4)')
plt.ylabel('Destination')



plt.show()


plt.plot(data_1, 'ro')
plt.show()

print cluster3

for k in range(len(cluster3)):
    l = cluster3[k]
    plt.plot(l, 'ro')
plt.show()

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



