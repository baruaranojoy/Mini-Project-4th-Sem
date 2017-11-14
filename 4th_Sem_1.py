f_source = open("Edge_List_1.txt","r")

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

print len(data)
print len(unique_element)

################################################################################

##import numpy as np
##from sklearn.cluster import KMeans
##from sklearn import preprocessing
##import pandas as pd
##import matplotlib.pyplot as plt
##
##
##X = np.array(data)
##
##kmeans = KMeans(n_clusters=4, random_state=0).fit(X)
##
##cluster1 = []
##cluster2 = []
##cluster3 = []
##cluster4 = []
##
##for k in range(len(data)):
##    cluster = kmeans.predict(data[k])
##    if cluster == 0:
##        cluster1.append(data[k])
##    elif cluster == 1:
##        cluster2.append(data[k])
##    elif cluster == 2:
##        cluster3.append(data[k])
##    elif cluster == 3:
##        cluster4.append(data[k])
##
##plt.plot(cluster1, 'go' , label = 'Cluster-1')
##plt.plot(cluster2, 'ro' , label = 'Cluster-2')
##plt.plot(cluster3, 'bo' , label = 'Cluster-3')
##plt.plot(cluster4, 'yo' , label = 'Cluster-4')
##
##
##
##plt.xlabel('Source (Green: Cluster-1, Red: Cluster-2, Blue: Cluster-3, Yellow: Cluster-4)')
##plt.ylabel('Destination')
##
##plt.show()
##
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
    
################################################################################

edge_list = []

element = 0

for k in range(len(unique_element)):
    doc = []
    element = unique_element[k]
    doc = [element]
    for l in range(len(data)):
        k = data[l]
        if k[0] == element:
            doc.append(k[1])
    edge_list.append(doc)
    
## printing the edge list
#print "Edge List"
edge_list.sort()

#f_final = [t_time , edge_list]

#f_destination.write(str(f_final))

for k in range(len(edge_list)):
    kk = edge_list[k]
    f_destination.write(str(kk) + "\n")
    #print kk
    
f_destination.close()

