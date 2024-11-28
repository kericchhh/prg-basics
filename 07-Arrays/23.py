array = [15, 8, 31, 47, 2, 19]

total_sum = 0
index = 0

# Use a while loop to calculate the sum of the array
while index < len(array):
    total_sum += array[index]  # Add the current element to total_sum
    index += 1  # Move to the next index

# Calculate the arithmetic mean
arithmetic_mean = total_sum / len(array)

# Display the array and the arithmetic mean
print("Array: ", array)
print("Arithmetic Mean: ", arithmetic_mean) 