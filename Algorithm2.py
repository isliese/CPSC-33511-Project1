def find_starting_city(city_distances, fuel, mpg):
    starting_city_index = 0
    # represents the amount of fuel available in the vehicle in terms of miles
    current_fuel = 0

    # for loop iterates through each city i along the circular route
    for i in range(len(city_distances)):
        # calculates how far in miles the car can travel with fuel available in the current city 
        current_fuel += fuel[i] * mpg

        # calculates how much fuel is left in miles after travelling to the next city
        current_fuel -= city_distances[i]

        # checks if the vehicle can make it back to the starting city
        # if at any point current_fuel < 0 the car will not be able to reach the starting city
        # current_fuel is then reset to 0 before checking the next index for a valid starting city
        if current_fuel < 0:
            starting_city_index = i + 1
            current_fuel = 0

    return starting_city_index

# represents the distances between each city in order
city_distances = [5, 25, 15, 10, 15]
# represents the amount of gas available at each city
fuel = [1, 2, 1, 0, 3]
# used to calculate fuel in terms of miles
mpg = 10


print(f"The preferred starting city is: {find_starting_city(city_distances, fuel, mpg)}")
