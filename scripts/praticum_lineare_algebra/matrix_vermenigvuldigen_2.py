
matrixA = [[4, 0, 3], [1, -1, 7], [-3, 3, 2]]
matrixB = [[-2, 3, 1], [2, -3, -5], [4, 0, 7]]

matrixC = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for rowIndex in range(len(matrixA)):
    for columnIndex in range(len(matrixB[0])):
         for termIndex in range(len(matrixA[rowIndex])):
             matrixC[rowIndex][columnIndex] += matrixA[rowIndex][termIndex] * matrixB[termIndex][columnIndex]

for result in matrixC:
   print(result)
