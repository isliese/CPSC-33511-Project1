def minSwapsCouples(row):
    n = len(row) // 2  
    couple_map = {}  
    swaps = 0 

    # Initialize the map with current positions
    for i in range(len(row)):
        couple_map[row[i]] = i

    # Iterate through the row in steps of 2 (checking each couple)
    for i in range(0, len(row), 2):
        first_person = row[i] 
        second_person = row[i + 1]  
        couple_id = first_person ^ 1 

        # If the second person isn't the partner of the first person
        if second_person != couple_id:
            swaps += 1  
            swap_pos = couple_map[couple_id]  

            # Swap the second person with the partner
            row[i + 1], row[swap_pos] = row[swap_pos], row[i + 1]

            # Update the couple_map with the new positions
            couple_map[second_person] = swap_pos
            couple_map[couple_id] = i + 1

    return swaps


# Input: list of people in the row as a Python list string
row = eval(input("Enter the row as a list : "))

# Output the result
print("Answer:", minSwapsCouples(row))
