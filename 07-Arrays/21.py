# Input array
array = [-15, 8, -31, 47, -2, 19]

# Initialize maximum and minimum with the first element of the array
maximum = array[0]
minimum = array[0]

# Iterate through the array to find max and min
for num in array:
    if num > maximum:
        maximum = num  # Update maximum if the current number is greater
    if num < minimum:
        minimum = num  # Update minimum if the current number is smaller

# Display the results
print("Array: ", array)
print("Maximum number: ", maximum)
print("Minimum number: ", minimum)
