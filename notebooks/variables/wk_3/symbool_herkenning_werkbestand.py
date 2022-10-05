import math as mt
from math import exp
from re import I

# Define symbols

symbolVecs = {'o': (1, 0), 'x': (0 ,1)} # voor cost functie
symbolChars = dict((value, key) for key, value in symbolVecs.items ())

# Define datasets (training should normally be much larger than test set for best results)

trainingSet = (
    ((
        (1, 1, 1),
        (1, 0, 1),
        (1, 1, 1)
    ),  'o'),
    ((
        (0, 1, 0),
        (1, 0, 1),
        (0, 1, 0)
    ),  'o'),
    ((
        (0, 1, 0),
        (1, 1, 1),
        (0, 1, 0)
    ),  'x'), 
    ((
        (1, 0, 1),
        (0, 1, 0),
        (1, 0, 1)
    ),  'x'),
)     


# result list initialization
# result = []
 
# for tuple in trainingSet:
#     for elements in tuple:
#         result.append(elements)
 
# printing output
# print(result[0])
# print(type(result))

# tSet1 = []

# for numbers in result[0]:
#     for singleNumber in numbers:
#         tSet1.append(singleNumber)
        
# print(tSet1)        
# print(type(tSet1))


# print(type(trainingSet))

# myit = iter(trainingSet)

# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))


# trainingSet1 = list(trainingSet)
# print((trainingSet1))
# tSetOne = list(trainingSet1)
# print(tSetOne)
# print(type(tSetOne))


# result list initialization
# result = []
 
# for tuple in trainingSet:
#     for elements in tuple:
#         result.append(elements)

#     # return result

# # printing output
# print(result[0])
# print(type(result))

# trainingSetList = result

# tSet = []

# for tuple in trainingSetList:
#     tSet += list(trainingSetList)

# print(tSet)

# tSet = []

# for numbers in trainingSet[3][0]: # met [][] kan de eerste stap overgeslagen worden en het alleen de matrix teruggegeven worden
#     for singleNumber in numbers:
#         tSet.append(singleNumber)

    
# print('Trainingset 01: ', tSet)   
   
# # print(type(tSet1))

# trainingLabel = []

# for label in trainingSet[3][1]:
#     for signifier in label:
#         trainingLabel.append(signifier)

    
# print('Label set 01:   ', trainingLabel)   
# tSet = []

# for tuple in trainingSet:
#     tSet += list(trainingSet)

mList = [[0, 0, 1],
         [1, 1, 1],
         [1, 0, 0]]


eList = mList[0][0]

mTup = ((0, 0, 1),
        (1, 1, 1),
        (1, 0, 0))

eTup = mTup[0][0]

print('mTup: ', mTup)

def mat2vec(mat):

    # Convert 3 x 3 to 9 x 1
    vec = []

    rows = len(mat)
    
    for row in range(0, rows):

        cols = len(mat[row])

        for col in range(0, cols):

            vec.append(mat[row][col])

    return vec

print(mTup)

# v = mat2vec(mTup)

# print(v)

# def in2out(input, weights):
#     pass

s =((
        (0, 0, 1),
        (1, 1, 1),
        (1, 0, 0)
    ), 'X')

# print(s[0])
# print(s[1])


def initWeights(vec):
    n = len(vec)
    weights = []
    for i in range(0,n):
        weights.append(0.5)
    return weights

vec = mat2vec(s[0])
weights = initWeights(vec)

print ('weights: ', weights)    


def in2out(vec, weights):
    
    # Compute vec[i] * weights[i]
   
    n = len(vec)
    
    Sum = 0.0
    
    for i in range(0, n):

        Sum += vec[i] * weights[i]
    
        return mt.sqrt(Sum)
    
#     # TODO:            
#     # Return softmax
        
vec = mat2vec(s[0])
weights = initWeights(vec)  
out = in2out(vec, weights)   

print('output: ', out)     

        
# print(tSet)    

# res = list(map(list, trainingSet))

# # print(res)
# # print(type(res))

# res2 = list(map(list, res[0]))

# print(res2[0])
# print(type(res2))

# trainingSet1Tuple1 = trainingSet1[0]
# # print(trainingSet1Tuple1[0:3])
# # print(trainingSet1Tuple1[2])

# trainingSet1Tuple1Elements = list(trainingSet1Tuple1[0:3])
# # print(trainingSet1Tuple1Elements)
# print('===========')
# for i0_1 in trainingSet1Tuple1Elements:
#     print ('i0_1: ', i0_1)
# print('===========')    

# lineInMatrix1_0 = i0_1
# print('===========')
# print(lineInMatrix1_0)  
# print('lineInMatrix1_0: ', lineInMatrix1_0)

# (1, 1, 1),
# (1, 0, 1),
# (1, 1, 1)
      
# trainingSet4 = trainingSet[3] 
# # print((trainingSet4))
# # print(len(trainingSet))

# trainingSet4Tuple = trainingSet4[0]
# # print(trainingSet4Tuple[0:3])
# # print(trainingSet4Tuple[2])

# trainingSet4TupleElements = trainingSet4Tuple[0:3]
# # print(trainingSet4TupleElements)
# print('===========')
# for ix_2 in trainingSet4TupleElements:
#     print ('ix_2: ',ix_2)
    
# print('===========')   

# setFour = list(ix_2)            
# print(setFour) # [1, 0, 1]
# print(type(setFour))


# trainingSet bestaat uit tuples: trainingSet1_0 (incl. label) + 
#                                 trainingSet2_0 (incl. label) + 
#                                 trainingSet3_x (incl. label) + 
#                                 trainingSet4_x (incl. label)
#
# trainingSet1_0 = (((1, 1, 1), (1, 0, 1), (1, 1, 1)), '0')

# lineInMatrix1_0 = (1, 1, 1) - no label







# Two possible Outputs thus, matrix (1,2) 2-nodes, therefore we need matrix Input (trainingSet) (3,3) or (9,1) 9-nodes * matrix Weight (2,9) 18-links

# input nodes do not get input from the links, output nodes get input from the links


# Epoch 

#================================================#

# class Node: 
# def __init__(self):
#     self.value = None # (is X or 0?)
#     self.inLinks = [self.inNode?] * self.weight  # 9 links = input links > is voor de Output dus moet 2 waardes worden?

# for rowIndex in range(len(self.inNode1_0)):                                                            #  9x doorlopen
#     for columnIndex in range(len(self.weight[0])):                                                   # 2x doorlopen
#         for termIndex in range(len(self.inNode[1])):                                                #  1x doorlopen
#             'matrixC'[rowIndex][columnIndex] += self.inNode[rowIndex][termIndex] * self.weight[termIndex][columnIndex]

# Node()

#================================================#

# class Link:
# def __init__(self, inNode, outNode):
#     self.weight = 0.5
#     self.newWeight = 0.4
#     self.inNode = # trainingSet                                                                > 9x
#     self.outNode = sum.float(self.inLinks.items * self.weight.items) - for all elements self.inNode if is X or 0    > 2x
#
#  ?  self.weightMatrix = (
#                          (0.5, 0.5, 0.5),
#                          (0.5, 0.5, 0.5),
#                          (0.5, 0.5, 0.5)
#                         )  
# Link()

#================================================#

# Add to output - https://machinelearningmastery.com/softmax-activation-function-with-python/
# def Softmax():
#
# transform values into probabilities
#    from math import exp, done
# calculate each probability
#
# probability1 = exponential(1) / (exponential(1) + exponential(2))
# probability2 = exponential(2) / (exponential(1) + exponential(2))
#
# report probabilities

# print(probability1, probability2)

# report sum of probabilities

# print(probability1 + probability2)


# import math

# def soft_max(x):
#     exponents = []
#     for element in x:
#         exponents.append(math.exp(element))
#     summ = sum(exponents)
#     for i in range(len(exponents)):
#         exponents[i] = exponents[i] / summ 
#     return exponents 

# if __name__=="__main__":
#     arr = [0.844521, 0.147048]
#     output = soft_max(arr)
#     print(output)
#================================================#

# def Loss()

# Cost function is mean squared error: (4 x)
# Compute differences between the observed values and the predictions.  answerX = (y - y^), answer0 = (y - y^)
# Square each of these differences > use math.exp(y - y^)
# Add all these squared differences together > 4x .add? + + voor alle input matrices
# Divide this sum by the sample length > len() /4
#
# mse = (1/len(trainingSet)) * math.exp(Oy_predicted - Oy_actual_observed)
# mse = (1/len(trainingSet)) * math.exp(Xy_predicted - Xy_actual_observed) ???
#
#


#================================================#

# for rowIndex in range(len(trainingSet)):
#     for columnIndex in range(len(matrixB[0])):
#          for termIndex in range(len(trainingSet[rowIndex])):
#              matrixC[rowIndex][columnIndex] += trainingSet[rowIndex][termIndex] * matrixB[termIndex][columnIndex]
#
# for result in matrixC:
#    print(result)