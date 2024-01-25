# Getting Energy Usage/Person
import matplotlib.pyplot as plt

def createEnergyandCityLists():
    cities = []
    city_energy = []
    pop = []
    energy_per_person = []
    file = open("Monthly-Electricity-Consumption-for-Major-US-Cities.csv")
    split_character = ','
    for line in file:
        data_line = line.split(split_character)  # split each line
        cities.append(data_line[0])  # add first element, name of city, in order
        city_energy.append(float(data_line[1]))  # add second element, energy usage of city (in gigawatts), in order
        data_line[2] = data_line[2].strip("\n")  # get rid of \n character on end of each element
        pop.append(float(data_line[2]))  # add third element, population (millions of people), in order
    file.close()
    i = 0  # counter
    while i < len(city_energy):
        energy = city_energy[i]
        population = pop[i]*1000000  # gives exact population
        en_use_per_person = (energy/population)*1000  # gives energy use per person in megawatts
        energy_per_person.append(en_use_per_person)
        i += 1
    return cities, city_energy, pop, energy_per_person
    
#cities, city_energy, pop, energy_per_person = createEnergyandCityLists()

def graphEnergyData(cities, city_energy, energy_per_person):
    x = 0,1,2,3,4,5,6,7,8,9,10,11,12,13
    plt.figure(figsize=(15, 5))
    plt.bar(x, energy_per_person, align='center', tick_label=cities)
    xlabel = plt.xlabel("Cities")
    xlabel.set_color("red")
    ylabel = plt.ylabel("Energy Use/Person (MegaWatts)")
    ylabel.set_color("red")
    title = plt.title("Energy Usage per Person in Major Cities")
    title.set_color("green")
    plt.show()

#graphEnergyData(cities, city_energy, energy_per_person)