matrix = [
   [0,0,0],
   [0,0,0],
   [0,0,0]
]

for i in range(len(matrix)):
    matrix[i][i] = 1

print('Modified Matrix:')
for row in matrix:
    print(" ".join(map(str, row)))