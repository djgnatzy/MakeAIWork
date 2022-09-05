matrixA = [[0, 3], [1, 4], [2, 5]]
matrixB = [[9, 7], [8, 6]]
matrixC = [] # final result

for rowA in range(len(matrixA)):
    # print ('\nlen(matrixA):', len(matrixA))
    # print ('rowA:', rowA)
    rowC = [] # the new row in new matrix
    for rowB in range(len(matrixB[0])):
        # print ('\nlen(matrixB):', len(matrixB))
        # print ('rowB:', rowB)
        productC = 0 # the new element in the new row
        for column in range(len(matrixA[rowA])):
            productC += matrixA[rowA][column] * matrixB[column][rowB]
            # print ('\nlen(matrixA[rowA]):', len(matrixA[rowA]))
            # print ('rowC:', rowC)
            # print ('productC:', productC)

        rowC.append(productC) # append sum of product into the new row

    matrixC.append(rowC) # append the new row into the final result


print('\nmatrixC:', matrixC)
