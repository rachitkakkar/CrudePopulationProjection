# AUTHOR: RACHIT KAKKAR
# GOAL: PROVIDE A "MIDDLE-OF-THE-ROAD" PROJECTION FOR ANY POPULATION, WHICH HOLDS THAT RATES STAY 
# THE SAME INSTEAD OF INCREASING/DECREASING

import matplotlib.pyplot as plt

# Fill out following info
startingPop = 127834233 
birthRate = 8.7 # per 1000
deathRate = 9.1 # per 1000
netMigration = 0 # per 1000
numberOfYears = 10
currentYear = 2011
countryName = 'Japan'

# Project population and print projected population (in millions) for each year
populationProjection = [startingPop / 1000000]
years = [currentYear]

lastYearPop = startingPop
for year in range(1, numberOfYears + 1):
    thisYearPop = round(lastYearPop + (((birthRate - deathRate) * (lastYearPop / 1000)) + (netMigration * (lastYearPop / 1000))))
    print(f'Year {year + currentYear}: {thisYearPop / 1000000} million people')
    populationProjection.append(thisYearPop / 1000000)
    years.append(year + currentYear)
    lastYearPop = thisYearPop

# Plot population (in millions) for each year
plt.plot(years, populationProjection)
plt.ylabel('Population (in millions)') 
plt.xlabel('Year') 
plt.title(f'Projected Population of {countryName}')
plt.show()