
# Werkt, maar kan vast makkelijker.

class Matrix:

    def __init__(self, matList):
        
        self.mat = matList
        self.lenght = (len(matList), len(matList[0]))
        self.rows = [matList[a][:] for a in range(self.lenght[0])]
        self.columns = [[matList[a][b] for a in range(self.lenght[0])] for b in range(self.lenght[1])]

    def get(self, a, b):
        if (a) <= self.lenght[0] and (b) <= self.lenght[1]:
            return self.mat[a-1][b-1]
        else:
            print("index not in matrix!")
            return None

    def __multList(self, matList1, matList2):
        
        if len(matList1) == len(matList2):
            return sum([matList1[a] * matList2[a] for a in range(len(matList1))])

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
E = Matrix([[1, 2], [5, 6]])

C = A.mult(B)

print('\nMultiplication Matrix C: ', C.mat)
