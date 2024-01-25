"""This is the python file that your instructors will run to test your code
make sure it runs correctly when someone downloads your repository. You 
might want to test this on a classmates computer to be sure it works!"""

# This files should not contain any function defitions


# IMPORT STATEMENTS
import EnergyandPopulationData as epd
import ReadDataFinal as rdf
import EnergyComparisons as ecp

# CODE

###Energy Usage per City
cities, city_energy, pop, energy_per_person = epd.createEnergyandCityLists()
epd.graphEnergyData(cities, city_energy, energy_per_person)
        
Cities, Latitude, Longitude, Population, B_T_U = rdf.readData()

###Following 5 lines ask for and set latitude and longitude points of the area you want to test, then ask for a K value (How many nearby cities will you analyze?)
test_lat = input("What is the latitude of the point you want to test? (Choose a point between 25 and 47) ")
test_lat = ((float(test_lat) - 25)/(47-25))
test_lon = input("What is the longitude of the point you want to test? (Choose a point between 71 and 122) ")
test_lon = (-1) * ((float(test_lon) - 71)/(122 - 71))
K = int(input("What is your desired K value (How many nearby cities would you like to power?) "))

###Finds the k nearest cities to your test point's coordinates

distancesKN, k_indices, Kpop, Kpopval = rdf.kNearestNeighborClassifier(K, Cities, Latitude, Longitude, Population, test_lon, test_lat)
#following line calculates monthly btu to power knearest cities
monthlybtu = Kpopval * (320000000/12)
print("The estimated Btu production to power these cities for a month would be " + str(monthlybtu) + " Btu.")

#following graphs the cities and test point    
rdf.graphData(Latitude, Longitude, test_lon, test_lat)

###gives the energy comparison for each city
cities, city_lats, city_longs, plant_lats, plant_longs, plant_energy_prod, city_energy_usage = ecp.createLists()
city_classifications = ecp.cityClassifications(cities, city_lats, city_longs, plant_lats, plant_longs)
difference = ecp.productionUsageComparison(cities, city_classifications, plant_energy_prod, city_energy_usage)