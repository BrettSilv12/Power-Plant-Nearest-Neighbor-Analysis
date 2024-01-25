"""This is the python file that your instructors will run to test your code
make sure it runs correctly when someone downloads your repository. You 
might want to test this on a classmates computer to be sure it works!"""

# This files should not contain any function defitions


# IMPORT STATEMENTS
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 16:13:38 2019

"""
import numpy as np
import csv
import matplotlib.pyplot as plt

csv_file = open('Latitude and Longitude of major us cities.csv')
total_row = sum(1 for row in csv_file)

def readData(): ###Reads the file that you set as csv_file and write in line 16
    line_count = 0
    index = 0
    with open('Latitude and Longitude of major us cities.csv') as csvfile:
        reader = csv.reader(csvfile)
        Cities = []
        Latitude = np.zeros((total_row,))
        Longitude = np.zeros((total_row,))
        Population = np.zeros((total_row,))
        B_T_U = np.zeros((total_row,))
        for row in reader:
            if row[5] != "0":
                Cities.append(row[0])
                Latitude[index] = ((float(row[1]) - 25)/(47 - 25))
                Longitude[index] = ((float(row[2]) + 71)/(122 - 71))
                Population[index] = float(row[5])
                B_T_U[index] = ((302000000 / 12) * (Population[index] * (10 ** 3)))
                line_count += 1
                index += 1
    return (Cities, Latitude, Longitude, Population, B_T_U)
        
Cities, Latitude, Longitude, Population, B_T_U = readData()

###Following 5 lines ask for and set latitude and longitude points of the area you want to test, then ask for a K value (How many nearby cities will you analyze?)
test_lat = input("What is the latitude of the point you want to test? (Choose a point between 25 and 47) ")
test_lat = ((float(test_lat) - 25)/(47-25))
test_lon = input("What is the longitude of the point you want to test? (Choose a point between 71 and 122) ")
test_lon = (-1) * ((float(test_lon) - 71)/(122 - 71))
K = int(input("What is your desired K value (How many nearby cities would you like to power?)"))

###Finds the k nearest cities to your test point's coordinates
def kNearestNeighborClassifier(k, Cities, Latitude, Longitude, Population, test_lon, test_lat):
    distancesKN = np.zeros(len(Population))
    distancesKN = np.sqrt((Longitude - test_lon)**2+(Latitude - test_lat)**2)
    sorted_indices = np.argsort(distancesKN)
    k_indices = sorted_indices[:k]
    print(k_indices)
    index = 0
    Kpop = np.zeros(len(k_indices))
    for i in k_indices:
        Kpop[index] = Population[k_indices[index]]
        index += 1
    Kpopval = sum(Kpop)
    print(Kpop)
    print("The population of the " + str(k) + " nearest cities is: " + str(Kpopval))
    return (distancesKN, k_indices, Kpop, Kpopval)

distancesKN, k_indices, Kpop, Kpopval = kNearestNeighborClassifier(K, Cities, Latitude, Longitude, Population, test_lon, test_lat)
#following line calculates monthly btu to power knearest cities
monthlybtu = Kpopval * (320000000/12)
print("The estimated Btu production to power these cities for a month would be " + str(monthlybtu) + " Btu.")

#following graphs the cities and test point
def graphData(Latitude, Longitude, test_lon, test_lat):
    plt.plot(test_lon, test_lat, 'r.', label = 'Test Point')
    plt.plot(Longitude, Latitude, 'g.', label = 'Cities', markersize = 0.1)
    plt.legend()
    plt.ylabel('Latitude')
    plt.xlabel('Longitude')
    plt.suptitle('Map of US Cities')
    plt.show()
    
graphData(Latitude, Longitude, test_lon, test_lat)