def get_ranked(unique , list_deg_centrality , list_cc_value , enhanced_degree_centrality):

    ok = []
    
    list_deg_centrality.sort()
    list_cc_value.sort()
    enhanced_degree_centrality.sort()

    for k in range(len(unique)):
        data1 = unique[k]
        data = data1[0]

        total = 0.0

        for m in range(len(list_deg_centrality)):
            t = list_deg_centrality[m]
            if data == t[1]:
                total = total + m
                break

        for m in range(len(list_cc_value)):
            t = list_cc_value[m]
            if data == t[1]:
                total = total + m
                break

        for m in range(len(enhanced_degree_centrality)):
            t = enhanced_degree_centrality[m]
            if data == t[1]:
                total = total + m
                break

        data1.append(total)
        ok.append([total , data])
        total = 0.0

    ok.sort()
    return ok


    
    





def get_unique(list_deg_centrality , list_cc_value , enhanced_degree_centrality):
    uni = []

    for k in range(len(list_deg_centrality)):
        data = list_deg_centrality[k]
        uni.append(data[1])

    for k in range(len(list_cc_value)):
        data = list_cc_value[k]
        uni.append(data[1])

    for k in range(len(enhanced_degree_centrality)):
        data = enhanced_degree_centrality[k]
        uni.append(data[1])

    uni = list(set(uni))


    uniq = []

    for k in range(len(uni)):
        uniq.append([uni[k]])

    return uniq
    


##########################################################################

## step-4
## calculating the CC_Value
def get_row(edge_list, element):
    z = []
    k = 0
    for k in range(len(edge_list)):
        m = edge_list[k]
        if m[0] == element:
            z = m
    return z


def compare(entry, row):
    k = 0
    count = 0
    for k in range(len(entry)-1):
        l = entry[k+1]
        m = 0
        for m in range(len(row)-1):
            n = row[m+1]
            if l == n:
                count = count + 1
    return count


def CC_Value(edge_list):
    # read each entry
    # as we have recieved the total edge list
    k = 0
    cc_vlaue_list = []
    for k in range(len(edge_list)):
        # variable to hold cc value 
        cc_val = 0.0
        # this is used to read each entry
        entry = edge_list[k]
        # all child nodes in each entry are
        # read and searched
        l = 0
        count = 0.0
        for l in range(len(entry)-1):
            if len(entry) == 1:
                cc_value = 100
            else:
                element = entry[l+1]
                row = get_row(edge_list, element)
                count = count + compare(entry, row)
        count = float(count/2)
        # claculating total possible edges between childern
        total_possible = float(len(entry)-1)
        total_possible = float((total_possible*(total_possible-1))/2)
        if total_possible == 0:
            cc_value = 100.0
        else:
            cc_value = float(count / total_possible)
        cc_vlaue_list.append([cc_value , entry[0]])
    cc_vlaue_list.sort()
    return cc_vlaue_list

#######################################################################

## calculating the degree centrality
def Degree_Centrality(edge_list):
    # find all the unique nodes in the edge list
    # unique_node holds all the unique nodes present
    # in the edge list
    k = 0
    unique_node = []
    for k in range(len(edge_list)):
        el = edge_list[k]
        l = 0
        for l in range(len(el)):
            unique_node.append(el[l])
    unique_node = list(set(unique_node))
    unique_node.sort()

    # finding the node with hightest degree
    # largest holds the value of highest
    # degree of a node in the edge list
    k = 0
    largest = 0
    for k in range(len(edge_list)):
        if len(edge_list[k]) > largest:
            largest = len(edge_list[k])

    # finding the numarator for degree centrality
    # numarator = a - b
    # a = largest * number of chids of that node
    # b = sum of degree of all child nodes of a node
    # and the data will be stored in the form
    # [[degree centrality, node number], [], [],.........., []]
    # first numarator will be calculated then
    # denominator then they will be divided
    k = 0
    list_degree_centrality = []
    
    # travarsing all the recorde in the edge list
    for k in range(len(edge_list)):
        row = edge_list[k]
        numarator = 0
        denominator = 0.0
        d_centrality = 0.0

        # if the node is not even connected to a single node
        # then it dont contribute anythng to the graph
        # so degree centrality of such node is 0
        if len(row) == 1:
            d_centrality = 100.0

        # else if it is connected to other nodes then we
        # calculate numarators and denominators
        else:
            l = 0
            su = 0

            # rach element of a record is travarsed
            # each element is taken and then its degree is
            # added up in the su variable
            for l in range(len(row)-1):
                each = row[l+1]
                m = 0
                for m in range(len(edge_list)):
                    rr = edge_list[m]
                    if rr[0] == each:
                        su = su + len(rr) - 1
            # claculating the numarator and denominator
            denominator = abs(float(largest * (len(row) - 1) - su))
            numarator = abs(float((len(row) - 1) * (len(row) - 1) - su))
            if denominator == 0:
                d_centrality = 100.0
            else:
                d_centrality = numarator / denominator
        list_degree_centrality.append([d_centrality , row[0]])
    list_degree_centrality.sort()
    return list_degree_centrality


#######################################################################

import ast
edge_list = []
list_deg_centrality = []
list_cc_value = []
enhanced_degree_centrality = []


f_source = open("Edge_List.txt","r")
while 1:
    data = f_source.readline()
    if not data:
        break
    data = ast.literal_eval(data)
    #print data
    #print data[0]
    edge_list.append(data)
    
f_source.close()


# sending edge_list for calculating
# degree_centrality
# saving it in a file
f_degree_centrality = open("Result\Degree_Centrality_With_Time_Stamp.txt","w")
f_degree_centrality.close()
f_degree_centrality = open("Result\Degree_Centrality_With_Time_Stamp.txt","a")
list_deg_centrality = Degree_Centrality(edge_list)
f_degree_centrality.write(str(list_deg_centrality) + "\n")
f_degree_centrality.close()


# sending data to calculate CC_Values
f_cc_value = open("Result\CC_Value_With_Time_Stamp.txt","w")
f_cc_value.close()
f_cc_value = open("Result\CC_Value_With_Time_Stamp.txt","a")
list_cc_value = CC_Value(edge_list)
f_cc_value.write(str(list_cc_value) + "\n")
f_cc_value.close()


# calculating the Enhanced degree centrality
k = 0
mult = 0.0
for k in range(len(list_deg_centrality)):
    a = list_deg_centrality[k]
    b = list_cc_value[k]
    if a[0] == 100.0 or b[0] == 100.0:
        mult = 100.0
    else:
        mult = float(float(a[0])*float(b[0]))
    enhanced_degree_centrality.append([mult , a[1]])
enhanced_degree_centrality.sort()
# storing it in the file
f_enhanced_degree_centrality = open("Result\Enhanced_Degree_Centrality.txt","w")
f_enhanced_degree_centrality.close()
f_enhanced_degree_centrality = open("Result\Enhanced_Degree_Centrality.txt","a")
f_enhanced_degree_centrality.write(str(enhanced_degree_centrality) + "\n")
f_enhanced_degree_centrality.close()


# list_deg_centrality
# list_cc_value
# enhanced_degree_centrality

unique = get_unique(list_deg_centrality , list_cc_value , enhanced_degree_centrality)

ranked = get_ranked(unique , list_deg_centrality , list_cc_value , enhanced_degree_centrality)

data = ranked[0]
print "The most influential node according to the calculation is : (", data[1],") with a cummalative rank of : (" , data[0] , ")."

most = data[1]



## drawing the graph
import numpy as np
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

k = np.genfromtxt('Road networks/californial coordinates.txt', dtype= None)

for m in range(len(k)):
    da = k[m]
    ele = da[0]
    lon = da[1]
    lat = da[2]
    #print da
    if ele == data[1]:
        print "Longitude : ", lon
        print "Latitude : ", lat 
        m = Basemap(projection='mill',
            llcrnrlat = 25,
            llcrnrlon = -130,
            urcrnrlat = 50,
            urcrnrlon = -60,
            resolution = 'l')
        m.drawcoastlines()
        m.drawcountries(linewidth=2)
        m.drawstates(color = 'b')
        NYClat , NYClon = lat , lon
        xpt , ypt = m(NYClon , NYClat)
        m.plot(xpt , ypt , 'r*' , markersize=10 , label = 'Most Influential Point') 
        plt.legend(loc=4)
        plt.title('Maps')
        plt.show()

        break






# print list_deg_centrality
# print list_cc_value
#print enhanced_degree_centrality

for k in range(len(list_deg_centrality)):
    da = list_deg_centrality[k]
    if most == da[1]:
        print "Degree centrality : ", da[0]

for k in range(len(list_cc_value)):
    da = list_cc_value[k]
    if most == da[1]:
        print "CC_Value centrality : ", da[0]

for k in range(len(enhanced_degree_centrality)):
    da = enhanced_degree_centrality[k]
    if most == da[1]:
        print "Enhanced Degree Centrality : ", da[0]






















