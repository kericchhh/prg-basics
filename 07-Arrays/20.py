arr = [ 8, 2, 5, 1, 9 ]

squared = [x ** 2 for x in arr]

print("Array:", ' '.join(map(str, arr)))
print("Squared:", ' '.join(map(str, squared)))