# matrixA = [[0, 3], [1, 4], [2, 5]]
# matrixB = [[9, 7], [8, 6]]
# matrixC = [] # final result

# for rowA in range(len(matrixA)):
#     # print ('\nlen(matrixA):', len(matrixA))
#     # print ('rowA:', rowA)
#     rowC = [] # the new row in new matrix
#     for rowB in range(len(matrixB[0])):
#         # print ('\nlen(matrixB):', len(matrixB))
#         # print ('rowB:', rowB)
#         productC = 0 # the new element in the new row
#         for column in range(len(matrixA[rowA])):
#             productC += matrixA[rowA][column] * matrixB[column][rowB]
#             # print ('\nlen(matrixA[rowA]):', len(matrixA[rowA]))
#             # print ('rowC:', rowC)
#             # print ('productC:', productC)

#         rowC.append(productC) # append sum of product into the new row

#     matrixC.append(rowC) # append the new row into the final result


# print('\nmatrixC:', matrixC)

# #-------------------------------------------------#

# class Matrix():
    
#     def __init__(self, list):
    
#     self.mat = list
#     self.dim = (len(list), len(list[0]))
#     self.rows=[lst[i][:] for i in range(self.dim[0])]
#     self.columns=[[lst[i][j] for i in range(self.dim[0])] for j in range(self.dim[1])]

    
#     def matrixMul(self):
        
#         matrixA = [[0, 3], [1, 4], [2, 5]]
#         matrixB = [[9, 7], [8, 6]]
#         matrixC = [] 

#         for rowA in range(len(matrixA)):
#             rowC = [] 
            
#             for rowB in range(len(matrixB[0])):
#                 productC = 0 
                
#                 for column in range(len(matrixA[rowA])):
#                     productC += matrixA[rowA][column] * matrixB[column][rowB]
#                     rowC.append(productC) 
#                     matrixC.append(rowC) 


# matrixA = 
# matrixB =

# object = matrixMul()


# print('\nmatrixC:', matrixC)


class Matrix:

    def __init__(self, matList):
        self.mat = matList
        self.lenght = (len(matList), len(matList[0]))
        self.rows = [matList[a][:] for a in range(self.lenght[0])]
        self.columns = [[matList[a][b] for a in range(self.lenght[0])] for b in range(self.lenght[1])]

    # def get(self, a, b):
    #     if (a) <= self.lenght[0] and (b) <= self.lenght[1]:
    #         return self.mat[a-1][b-1]
    #     else:
    #         print("index not in matrix!")
    #         return None

    def __multList(self, list1, list2):
        if len(list1) == len(list2):
            return sum([list1[a]*list2[a] for a in range(len(list1))])

    def mult(self, other):
        matrixC = []
        for a in range(len(self.rows)):
            rows = []
            for b in range(len(other.columns)):
                rows.append(self.__multList(other.columns[b],self.rows[a]))
            matrixC.append(rows)
        return Matrix(matrixC)


A = Matrix([[0, 3], [1, 4], [2, 5]])
B = Matrix([[9, 7], [8, 6]])

C = A.mult(B)

print('\nMatrixC: ', C.mat)