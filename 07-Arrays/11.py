# Bubble sort implementation
def bubble_sort(arr):
    n = len(arr)  # Get the length of the array
    for i in range(n):  # Outer loop to track the number of passes
        for j in range(n - 1 - i):  # Inner loop to compare adjacent elements
            if arr[j] > arr[j + 1]:  # Compare adjacent elements
                # Swap the elements if they are in the wrong order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Data to be sorted
car_fuel_consumption = [7.2, 6.8, 7.5, 7.0, 7.1, 6.9, 7.3]
print("Original car fuel consumption:", car_fuel_consumption)
sorted_car_fuel_consumption = bubble_sort(car_fuel_consumption[:])  # Sort a copy to keep original unchanged
print("Sorted car fuel consumption:", sorted_car_fuel_consumption)

bank_transactions = [-150, -20, 300, -45, -60, 500, -120]
print("Original bank transactions:", bank_transactions)
sorted_bank_transactions = bubble_sort(bank_transactions[:])  # Sort a copy to keep original unchanged
print("Sorted bank transactions:", sorted_bank_transactions)
