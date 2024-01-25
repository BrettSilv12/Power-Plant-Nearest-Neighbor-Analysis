# Analysis of energy production and usage - Team Megabrett

In this project we analyzed energy usage per city by creating a spreadsheet of cities, their coordinates,
    and their populations, then applying estimates for monthly personal energy usage to deduce the 
    energy needed to power different cities. We then included a Knearest neighbor classification system 
    that will tell you the knearest cities to a certain coordinate point that the user chooses, and 
    calculates how much energy is required to power those Knearest cities. In addition, we utilized a 
    nearest neighbor function to see what cities were over consuming energy, producing 'extra' energy, 
    breaking even, or not producing any energy.

## Instructions

All that the user needs to do is open the file "main.py", run it in a python editor that will allow 
    graphing, and run the program. Follow the prompts that appear on the console to input your desired 
    coordinate points and K value, and then the computer will automatically tell you the Knearest cities 
    and their energy requirements. It will also give a graph for the average energy usage per person 
    in these cities, and whether these cities are over using enrgy or producing extra energy.

## File List

README - instructions
main.py - the actual code that you need to run
EnergyandPopulationData.py - functions for producing the graph that gives the energy usage per person in the 14 
    cities looked at
ReadDataFinal.py - Contains the functions for parsing "Latitude and Longitude of major us cities.csv", and carrying
	out the knearest neighbor analysis of cities and their energy requirements
EnergyComparisons.py - funcitons to find the comparison of energy consumption and energy produciton for
    each city
Latitude and Longitude of major us cities.csv - spreadsheet including the coordinate and population data for major US cities
largest nuclear power stations in the us.csv - spreadsheet including energy produciton (in gigawatts)
    and locations (latitude and longitude) of 46 nuclear power plants in the US
Monthly-Electricity-Consumption-for-Major-US-Cities.csv - spreadsheet including energy consumption (in 
    gigawatts), population (in millions of people), and locations of (latitude/longitude) of 14 major
    US cities


