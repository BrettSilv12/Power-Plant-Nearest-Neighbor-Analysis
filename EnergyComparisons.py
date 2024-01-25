import numpy as np
import math

def createLists():
    split_char = ","
    cities = []
    city_lats = []
    city_longs = []
    city_energy_usage = []  #gigawatts per month
    file1 = open("Monthly-Electricity-Consumption-for-Major-US-Cities.csv")
    for line in file1:
        data_line = line.split(split_char)
        cities.append(str(data_line[0]))
        city_lats.append(float(data_line[3]))
        city_longs.append(float(data_line[4]))
        city_energy_usage.append(float(data_line[1]))
    file1.close()
    plant_lats = []
    plant_longs = []
    plant_energy_prod = []  #gigawatts per month
    file2 = open("largest nuclear power stations in the us.csv")
    for line in file2:
        data_line = line.split(split_char)
        plant_lats.append(float(data_line[2]))
        plant_longs.append(float(data_line[3]))
        plant_energy_prod.append(float(data_line[1]))
    file2.close()
    return cities, city_lats, city_longs, plant_lats, plant_longs, plant_energy_prod, city_energy_usage

def cityClassifications(cities, city_lats, city_longs, plant_lats, plant_longs):
    city_classifications = []  #city at each index will correspond to the closest city to the plant at that index
    j = 0
    for j in range(0, len(plant_lats)):
        distances = []
        i = 0
        for i in range (0, len(city_lats)):
            diff_lats = abs(city_lats[i] - plant_lats[j])
            diff_longs = abs(city_longs[i] - plant_longs[j])
            dist = math.sqrt(diff_lats**2 + diff_longs**2)
            distances.append(dist)
            i += 1
        distances_from_plant = np.asarray(distances)
        index_of_min_dist = np.argmin(distances_from_plant)
        closest_city = cities[index_of_min_dist]
        city_classifications.append(closest_city)
        j += 1
    return city_classifications

def productionUsageComparison(cities, city_classifications, plant_energy_prod, city_energy_usage):
    differences = []  #list of all monthly energy usage/production differences, gigawatts
    j = 0
    for j in range(0, len(cities)):  #going through cities list element by element (14 cities)
        city_energy_prod = 0
        indices = [i for i, x in enumerate(city_classifications) if x == cities[j]] 
            #all indicies where city name shows up in city_classification
        if indices == []:
            print(str(cities[j])+" produces no nuclear energy, but uses "+str(city_energy_usage[j])+" gigawatts per month.")
        else:
            city_energy_prod = 0
            k = 0
            for k in range(0, len(indices)):
                plant_prod = plant_energy_prod[indices[k]]  #energy produciton of plant at index k in indices list
                city_energy_prod += plant_prod
            difference = city_energy_usage[j] - city_energy_prod
            differences.append(difference)
            if difference > 0:
                print(str(cities[j])+" uses "+str(abs(difference))+" more gigawatts of total energy than it produces of nuclear energy per month.")
            if difference < 0:
                print(str(cities[j])+" produces "+str(abs(difference))+" more gigawatts of nuclear energy than it uses of total energy per month.")
            if difference == 0:
                print(str(cities[j])+" uses the same amount of energy as it produces of nuclear energy per month.")
    return differences

