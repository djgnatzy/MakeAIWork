# ts1 = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
# ts2 = [[0, 1, 0], [1, 0, 1], [0, 1, 0]]
# ts3 = [[0, 1, 0], [1, 1, 1], [0, 1, 0]]
# ts4 = [[1, 0, 1], [0, 1, 0], [1, 0, 1]]

# weights = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
# print(type(weights))

# ms4 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# for rowIndex in range(len(ts4)):
#     for columnIndex in range(len(weights[0])):
#         for termIndex in range(len([weights])):
#             ms4[rowIndex][columnIndex] += ts4[rowIndex][termIndex] * weights[termIndex][columnIndex]
            
# for result in ms4:
#     print(result)
    
    
# x4    

# 2

# Program to multiply two matrices using nested loops
# print()

# # # 3x3 matrix
# X = [[12,7,3],
#     [4 ,5,6],
#     [7 ,8,9]]
# # # 3x4 matrix
# Y = [[5,8,1,2],
#     [6,7,3,0],
#     [4,5,9,1]]
# # # result is 3x4
# result = [[0,0,0,0],
#          [0,0,0,0],
#          [0,0,0,0]]

# # iterate through rows of X
# for i in range(len(X)):
#    # iterate through columns of Y
#    for j in range(len(Y[0])):
#        # iterate through rows of Y
#        for k in range(len(Y)):
#            result[i][j] += X[i][k] * Y[k][j]

# for r in result:
   
#    print(r)
   
   
   
#    # 3
# print()   
# Program to multiply two matrices using list comprehension

# 3x3 matrix
# X = [(12,7,3),
#     (4 ,5,6),
#     (7 ,8,9)]



X = (
        (1, 1, 1),
        (1, 0, 1),
        (1, 1, 1)
    )

# 3x4 matrix
# Y = [(5,8,1,2),
#     (6,7,3,0),
#     (4,5,9,1)]

Y = [(1,1,1),
    (1,1,1),
    (1,1,1)]

# result is 3x4
result = [[sum(a*b for a,b in zip(X_row,Y_col)) for Y_col in zip(*Y)] for X_row in X]

print(result)  

for r in result:
   print(r)   
    
# for rowIndex in range(len(ts4)):
#     for columnIndex in range(len(weights[0])):
#         for termIndex in range(len(ts4[rowIndex])):
#             ms1[rowIndex][columnIndex] += ts4[rowIndex][termIndex] * weights[termIndex][columnIndex]
            
# for result in ms1:
#     print(result)  


# tuple >(,)NOPE

# ts1 = [(1, 1, 1), (1, 0, 1), (1, 1, 1)]
# ts2 = [[0, 1, 0], [1, 0, 1], [0, 1, 0]]
# ts3 = [[0, 1, 0], [1, 1, 1], [0, 1, 0]]
# ts4 = [[1, 0, 1], [0, 1, 0], [1, 0, 1]]

# weights = [(1, 1, 1), (1, 1, 1), (1, 1, 1)]

# ms1 = [(0, 0, 0), (0, 0, 0), (0, 0, 0)]

# for rowIndex in range(len(ts1)):
#     for columnIndex in range(len(weights[0])):
#         for termIndex in range(len(ts1[rowIndex])):
#             ms1[rowIndex][columnIndex] += ts1[rowIndex][termIndex] * weights[termIndex][columnIndex]
            
# for result in ms1:
#     print(result)  
