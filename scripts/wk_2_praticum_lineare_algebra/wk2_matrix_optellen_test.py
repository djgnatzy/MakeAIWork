
matrixA = [[4, 0, 3], [1, -1, 7], [-3, 3, 2]]
matrixB = [[-2, 3, 1], [2, -3, -5], [4, 0, 7]]

matrixC = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for rowIndex in range(len(matrixA)):

             matrixC[rowIndex] += matrixA[rowIndex] + matrixB

for result in matrixC:
   print(result)
