import numpy as np
from sklearn.cluster import KMeans
from sklearn import preprocessing
import pandas as pd
import matplotlib.pyplot as plt

data = [[1,2], [1,4], [1,0], [4,2], [4,4], [4,0], [50,40], [51,53], [47, 58], [45,2], [46,8], [4,48], [5,75], [9,55]]

X = np.array(data)

kmeans = KMeans(n_clusters=2, random_state=0).fit(X)

cluster1 = []
cluster2 = []
cluster3 = []

for k in range(len(data)):
    cluster = kmeans.predict(data[k])
    if cluster == 0:
        cluster1.append(data[k])
    elif cluster == 1:
        cluster2.append(data[k])
    elif cluster == 2:
        cluster3.append(data[k])    

print data
print cluster1
print cluster2
print cluster3

print len(data)
print len(cluster1)
print len(cluster2)
print len(cluster3)

plt.plot(cluster1, 'g^')
plt.plot(cluster2, 'r^')
plt.plot(cluster3, 'y^')
plt.show()






