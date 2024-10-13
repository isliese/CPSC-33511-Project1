def find_starting_city(city_distances, fuel, mpg):
    # 1. Initialization of variables
    starting_city_index = 0
    # represents the amount of fuel currently available in the vehicle at a city index in terms of miles
    current_fuel = 0
    # represents the total amount of fuel available in all cities
    total_fuel = 0
    # represents the total distance the car must cover to complete the route
    total_distance = 0

    # 2. Error handling 
    if len(city_distances) == 0 or len(fuel) == 0:
        raise ValueError("The input lists for cities and fuel cannot be empty")

    if len(city_distances) != len(fuel):
        raise ValueError("The input lists for cities and fuel must be the same length")
    
    if mpg <= 0: 
        raise ValueError("Miles per gallon must be a positive number greater than 0")
    

    # for loop iterates through each city i along the circular route
    # loop calculates the total fuel (converted to miles) and the total distance of the entire route
    # if the total fuel is less than the total distance the trip cannot be made by the car
    for i in range(len(city_distances)):
        total_fuel += fuel[i] * mpg
        total_distance += city_distances[i]

    # raise error if car cannot complete trip
    if total_fuel < total_distance: 
        raise ValueError("No valid starting city exists. Insufficient fuel to complete trip.")
    

    # 3. Algorithm
    # for loop iterates through each city i along the circular route
    # loop finds the valid starting city by calculating the remaining fuel after the car travels to each city 
    for i in range(len(city_distances)):

        # calculates how far in miles the car can travel with fuel available in the current city 
        current_fuel += fuel[i] * mpg

        # calculates how much fuel is left in miles after travelling to the next city
        current_fuel -= city_distances[i]

        # if at any point current_fuel < 0 the car will not be able to reach the starting city
        # current_fuel is then reset to 0 before checking the next index for a valid starting city
        if current_fuel < 0:
            starting_city_index = i + 1
            current_fuel = 0

    return starting_city_index

# represents the distances between each city in order
city_distances = [5, 25, 15, 10, 15]
# represents the amount of gas available at each city in gallons
fuel = [1, 2, 1, 0, 3]
# used to calculate fuel in terms of miles
mpg = 10


print(f"The preferred starting city is: {find_starting_city(city_distances, fuel, mpg)}")
