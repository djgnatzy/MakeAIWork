class Matrix:

    def __init__(self, matList):
        
        self.mat = matList
        # self.lenght = (len(matList), len(matList[0]))
        self.rows = [matList[a][:] for a in range(self.lenght[0])]
        self.columns = [[matList[a][b] for a in range(self.lenght[0])] for b in range(self.lenght[1])]

    # def get(self, a, b):
    #     if (a) <= self.lenght[0] and (b) <= self.lenght[1]:
    #         return self.mat[a-1][b-1]
    #     else:
    #         print("index not in matrix!")
    #         return None

    def __multList(self, matList1, matList2):
        
        if len(matList1) == len(matList2):
            return sum([matList1[a] * matList2[a] for a in range(len(matList1))])

    def mult(self, other):
        
        for i in range(len(matList1)):
            for j in range(len(other[0])):
                for k in range(len(matList1[i])):
                    matrixC[i][j] += matList1[i][k] * other[k][j]
            
        return Matrix(matrixC)
        # result = Matrix(matrixC)
    

matrixA = [[4, 0, 3], [1, -1, 7], [-3, 3, 2]]
matrixB = [[-2, 3, 1], [2, -3, -5], [4, 0, 7]]

matrixC = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

print(matrixC)


#-----------------------------------------------------------------#




matrixC = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for i in range(len(matrixA)):
    for j in range(len(matrixB[0])):
         for k in range(len(matrixA[i])):
             matrixC[i][j] += matrixA[i][k] * matrixB[k][j]
             
             
             
             
#-------------------------------------------------#

# class MatrixAdd:

#     def __init__(self, matList):
        
#         self.mat = matList
#         self.lenght = (len(matList))
#         # self.rows = [matList[a][:] for a in range(self.lenght[0])]
        
#     def __addList(self, matList1, matList2):
        
#         if len(matList1) == len(matList2):
#             for a in range(len(matList1)):
#                 return append([matList1[a] + matList2[a]]) 

#     def add(self, other):
          
#         matrix_G = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        
#         for a in range(0, len(matList1)):
          
#             return MatrixAdd(matList1.append(matList2))
        
    
    
# # print(matrixG)

# E = MatrixAdd([[4, 0, 3], [1, -1, 7], [-3, 3, 2]])
# F = MatrixAdd([[-2, 3, 1], [2, -3, -5], [4, 0, 7]])

# G = MatrixAdd([[0, 0, 0], [0, 0, 0], [0, 0, 0]])

# # G = E + (F)

# # G = matrixG 

# # print('\nAddition Matrix G: ', matrix_G)    
   
# # print(result)



