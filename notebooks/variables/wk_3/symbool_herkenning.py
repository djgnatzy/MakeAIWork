import math as mt
from math import exp

# Define symbols

symbolVecs = {'o': (1, 0), 'x': (0 ,1)} # voor cost functie
symbolChars = dict((value, key) for key, value in symbolVecs.items ())

# Define datasets (training should normally be much larger than test set for best results)

# trainingSet = (
#     ((
#         (1, 1, 1),
#         (1, 0, 1),
#         (1, 1, 1)
#     ),  'o'),
#     ((
#         (0, 1, 0),
#         (1, 0, 1),
#         (0, 1, 0)
#     ),  'o'),
#     ((
#         (0, 1, 0),
#         (1, 1, 1),
#         (0, 1, 0)
#     ),  'x'), 
#     ((
#         (1, 0, 1),
#         (0, 1, 0),
#         (1, 0, 1)
#     ),  'x'),
# )     

X = [
    [
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1]
    ],
    [
        [0, 1, 0],
        [1, 0, 1],
        [0, 1, 0]
    ],
    [
        [0, 1, 0],
        [1, 1, 1],
        [0, 1, 0]
    ],
    [
        [1, 0, 1],
        [1, 1, 1],
        [1, 0, 1]
    ],
    ]    

# mList = [[1, 1, 1],
#           [1, 0, 1],
#           [1, 1,1]]


# eList = mList[0][0]

mTup = ((1, 1, 1),
        (1, 0, 1),
        (1, 1, 1),
       )

#  'o'

# eTup = mTup[2][0]

# print('mTup: ', mTup)
# print('eTup: ', eTup)

# def mat2vec(mat):

#     # Convert 3 x 3 to 9 x 1
#     vec = []

#     rows = len(mat)
    
#     for row in range(0, rows):

#         cols = len(mat[row])

#         for col in range(0, cols):

#             vec.append(mat[row][col])

#     return vec

# print(mTup)

# # v = mat2vec(mTup)

# # print(v)

# # def in2out(input, weights):
# #     pass

# s =((
#         (1, 1, 1),
#         (1, 0, 1),
#         (1, 1, 1)
#     ), 'O')

# print('s[0]: ', s[0])
# print('s[1]: ', s[1])


# def initWeights(vec):
#     n = len(vec)
#     weights = []
#     for i in range(0,n):
#         weights.append(0.5)
#     return weights

# vec = mat2vec(s[0])
# weights = initWeights(vec)

# print ('weights: ', weights)    


# def in2out(vec, weights):
    
#     # Compute vec[i] * weights[i]
   
#     n = len(vec)
    
#     Sum = 0.0
    
#     for i in range(0, n):

#         Sum += vec[i] * weights[i]
    
#         return mt.sqrt(Sum)
    
# #     # TODO:            
# #     # Return softmax
        
# vec = mat2vec(s[0])
# weights = initWeights(vec)  
# outTO1 = in2out(vec, weights)   

# print('output Tuple1: ', outTO1)     



# Two possible Outputs thus, matrix (1,2) 2-nodes, therefore we need matrix Input (trainingSet) (3,3) or (9,1) 9-nodes * matrix Weight (2,9) 18-links

# input nodes do not get input from the links, output nodes get input from the links


# Epoch 

#================================================#

# class Node: 
# def __init__(self):
value = [] # (is X or 0?)
# self.inLinks = [self.inNode?] * self.weight  # 9 links = input links > is voor de Output dus moet 2 waardes worden?
Y = [
                   [1, 1, 1],
                   [1, 1, 1],
                   [1, 1, 1]
]  
# inNode = trainingSet
    
# for rowIndex in range(len(inNode)):                                                            #  9x doorlopen
#     for columnIndex in range(len(weight[0])):                                                   # 2x doorlopen
#         for termIndex in range(len(inNode[1])):                                                #  1x doorlopen
#             value[rowIndex][columnIndex] += inNode[rowIndex][termIndex] * weight[termIndex][columnIndex]

result = [[sum(a*b for a,b in zip(X_row,Y_col)) for Y_col in zip(*Y)] for X_row in X]

print(result)  

for r in result:
   print(r)   

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

#---------------E X P L A N A T I O N-----------------#

def softmax(outputs):

    exponentials = []

    for item in outputs:
        exponentials.append(mt.exp(item))
        # >>> exponentials = [exp(7), exp(9)]

    sumExponentials = sum(exponentials) # <<< met 'sum' kan de lijst direct opgeteld worden

    probabilities = []

    for item in exponentials:
        probabilities.append(item/sumExponentials)
    return probabilities 


probabilities = softmax([7, 9])

print(probabilities)


# softmax([7, 9]) # < "7, 9" zijn voorbeelden, bij weight = 1.
# prob1 = exp(7) / exp(7) + exp(9) = ~
# prob2 = exp(9) / exp(7) + exp(9) = ~

#---------------E X P L A N A T I O N-----------------#


## transform values into probabilities
##    from math import exp, done
## calculate each probability

# outTX1 = 1 - outTO1
  
# print('outTX1: ', outTX1)

  
# prob1 = mt.exp(outTO1) / (mt.exp(outTO1) + mt.exp(outTX1))
# prob2 = mt.exp(outTX1) / (mt.exp(outTO1) + mt.exp(outTX1))
#
## report probabilities

# print('Probability 1: ', prob1,
#       '\nProbability 2: ', prob2)

## report sum of probabilities

# print('Sum of probabilities: ', prob1 + prob2)

#------------------------------------------------#

# import math
#
# def soft_max(x):
#     exponents = []
#     for element in x:
#         exponents.append(mt.exp(element))
#     summ = sum(exponents)
#     for i in range(len(exponents)):
#         exponents[i] = exponents[i] / summ 
#     return exponents 
#
# if __name__=="__main__":
#     arr = [0.844521, 0.147048]
#     output = soft_max(arr)
#     print(output)
#

#================================================#

# Mean Squared Error

#---------------E X P L A N A T I O N-----------------#

def lossFunction(probabilities, labels): # < rondje of kruisje, label < om te checken hoever je van de waarheid af zit voor 1 datapunt

    loss = 0
    # - if statemenent als safety-check om de lengtes te vergelijken - 
    # if len(probabilities) != len(labels):
        # raise IndexError ("Labels zijn niet even lang!")
          
    for i in range(len(probabilities)):
        
        error = labels[i]-probabilities[i]
        squaredError = error**2
        loss += squaredError
        
    return loss

outputs = [9, 7]
probabilities = [0.8 , 0.2] 
labels = [1, 0]             

print('Loss: ', lossFunction(softmax(outputs), labels))

#---------------E X P L A N A T I O N-----------------#

# OF

#---------------E X P L A N A T I O N-----------------#




# probabilities = [0.11 , 0.88]
# labels = [0, 1]

# probabilities - labels = [0.11 , 0.88] - [0, 1] = [0.11, -0.12]


# subtracted = list()

# for item1, item2 in zip(probabilities, labels):
#     subtracted.append(item1 - item2) 
# return subtracted
      
# print('Subtracted:', subtracted)
# print(sum(subtracted))
# print(mt.exp(sum(subtracted)))

# loss = mt.exp(sum(subtracted))

# print('Loss:', loss)


# symbolVecs = {'o': (1, 0), 'x': (0 ,1)} # voor cost functie
# symbolChars = dict((value, key) for key, value in symbolVecs.items ())

# return loss

# Cost function is mean squared error: (4 x)
# Compute differences between the observed values and the predictions.  answerX = (y - y^), answer0 = (y - y^)
# Square each of these differences > use math.exp(y - y^)
# Add all these squared differences together > 4x .add? + + voor alle input matrices
# Divide this sum by the sample length > len() /4
#
# mse = mt.exp(prob1 - 1)
# mse = (1/len(trainingSet)) * mt.exp(Xy_observed - Xy_predicted) ???
#
# print('MSE:', mse)

#================================================#
